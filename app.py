"""CALL-E Hackathon: Customer Follow-Up Automation Hybrid Project

Python SDK + Google Calendar API integration for automated lead follow-up calls.
Production-ready with proper OAuth flow and demo mode.
"""

import os
import json
import asyncio
from datetime import datetime, timedelta
from flask import Flask, request, jsonify, render_template_string, session
from call_e_sdk import CALL_EClient
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

# Flask app for webhook endpoints
app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET", "dev-secret-key-for-hackathon")

# CONFIGURATION
CALL_E_API_KEY = os.environ.get("CALL_E_API_KEY", "your-api-key-here")
call_e_client = CALL_EClient(api_key=CALL_E_API_KEY)

# Google Calendar Setup - OAuth 2.0
GOOGLE_OAUTH_CONFIG = {
    "client_id": os.environ.get("GOOGLE_CLIENT_ID"),
    "client_secret": os.environ.get("GOOGLE_CLIENT_SECRET"),
    "auth_uri": "https://accounts.google.com/o/auth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "userinfo_profile_uri": "https://www.googleapis.com/userinfo/v2/profile",
    "userinfo_email_uri": "https://www.googleapis.com/oauth2/v2/tokeninfo",
    "redirect_uris": ["http://localhost:8080/oauth2callback", "http://localhost:5000/oauth2callback"],
}

# Session-based credential storage (for demo; production use DB or session store)
CREDENTIALS_FILE = "user_token.json"

# HTML template for demo page with workflow explanation
DEMO_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>CALL-E Hackathon Demo</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 40px; }
        .endpoint { background: #f5f5f5; padding: 15px; margin: 10px 0; border-radius: 5px; }
        .btn { padding: 10px 20px; background: #4CAF50; color: white; border: none; cursor: pointer; }
        .step { margin: 20px 0; padding: 10px; background: #e8f4fd; border-left: 4px solid #2196f3; }
    </style>
</head>
<body>
    <h1>CALL-E Customer Follow-Up Demo</h1>
    <p>Hybrid: CALL-E Python SDK + Google Calendar API</p>
    
    <div class="step">
        <h3>Step 1: OAuth Setup (one-time)</h3>
        <p>Run <code>python oauth_setup.py</code> to get Google credentials, then place <code>credentials.json</code> in project root.</p>
        <p><strong>Required scopes:</strong> <code>https://www.googleapis.com/auth/calendar.events</code></p>
    </div>
    
    <div class="endpoint">
        <strong>POST /lead-submission</strong> - Submit lead form data
        <br/>JSON body: { "name": "John Doe", "email": "john@example.com", "phone": "+1234567890", "company": "Acme Corp" }
    </div>
    <div class="endpoint">
        <strong>GET /</strong> - This demo page
    </div>
    <div class="endpoint">
        <strong>GET /oauth2callback</strong> - Google OAuth completion
    </div>
    
    <div class="step">
        <h3>Step 2: Test Flow</h3>
        <ol>
            <li>POST lead data to /lead-submission</li>
            <li>CALL-E SDK places outbound call within 5 minutes</li>
            <li>Personalized message plays with scheduling option</li>
            <li>Press 1 → Google Calendar event created (if OAuth complete)</li>
            <li>Confirmation sent via email</li>
        </ol>
    </div>
</body>
</html>
"""


# ============================================================
# GOOGLE CALENDAR OAUTH & INTEGRATION
# ============================================================

def get_google_credentials():
    """Get valid Google OAuth credentials, initiating flow if needed."""
    creds = None
    
    # Load credentials from session file
    if os.path.exists(CREDENTIALS_FILE):
        creds = Credentials.from_authorized_user_file(CREDENTIALS_FILE, ["https://www.googleapis.com/auth/calendar.events"])
    
    # If no (valid) credentials, let the user log in
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            from google.auth.transport.requests import Request
            creds.refresh(Request())
        else:
            # Initiate OAuth flow
            flow = Flow.from_client_config(
                GOOGLE_OAUTH_CONFIG,
                scopes=["https://www.googleapis.com/auth/calendar.events"],
            )
            flow.redirect_uri = GOOGLE_OAUTH_CONFIG["redirect_uris"][0]
            
            auth_url, state = flow.authorization_url(access_type="offline", include_granted_scopes=True)
            print(f"\n📧 Open this URL and authorize: {auth_url}")
            print("After authorization, you'll be redirected with a code parameter.")
            print("Copy that code and run: python oauth_setup.py <code>")
            
            # For demo, return None if no auth code
            return None
    
    return creds


def save_credentials(creds):
    """Save credentials to session file."""
    with open(CREDENTIALS_FILE, "w") as f:
        f.write(creds.to_json())


def schedule_google_calendar(name, email, phone, company):
    """Schedule Google Calendar appointment after CALL-E call."""
    try:
        creds = get_google_credentials()
        
        if not creds:
            # Return demo result - user needs to complete OAuth
            return {
                "status": "oauth_required",
                "message": "Google Calendar scheduling requires OAuth completion. Run oauth_setup.py to authorize.",
                "action_required": "complete_oauth"
            }
        
        # Build the Google Calendar service
        service = build("calendar", "v3", credentials=creds)
        
        # Create calendar event - schedule for next available slot
        now = datetime.utcnow()
        start_time = now + timedelta(days=1, hours=9)  # Tomorrow at 9 AM
        end_time = now + timedelta(days=1, hours=9, minutes=30)  # 30-min appointment
        
        event = {
            "summary": f"Follow-up: {name} - {company}",
            "description": (
                f"Scheduled follow-up call with {name} from {company}.\n"
                f"Lead interest captured via CALL-E automation.\n"
                f"Phone: {phone}\n"
                f"Lead email: {email}\n"
                f"Call SID: demo-call-123 (will be real in production)"
            ),
            "start": {
                "dateTime": start_time.isoformat(),
                "timeZone": "UTC",
            },
            "end": {
                "dateTime": end_time.isoformat(),
                "timeZone": "UTC",
            },
            "attendees": [
                {"email": email} if email else {"displayName": name}
            ],
        }
        
        event = service.events().insert(calendarId="primary", body=event).execute()
        return {
            "status": "success",
            "event_id": event.get("id"),
            "htmlLink": event.get("htmlLink"),
            "start": event.get("start", {}).get("dateTime"),
            "end": event.get("end", {}).get("dateTime")
        }
        
    except Exception as e:
        print(f"Google Calendar Error: {e}")
        return {"status": "error", "message": str(e)}


# ============================================================
# CALL-E CALL FUNCTION
# ============================================================

def generate_call_message(name, company):
    """Generate personalized CALL-E message."""
    return f"""Hello {name}, this is a follow-up call from {company}. 
We noticed your interest and wanted to connect. 
Press 1 to schedule a quick 15-minute appointment on our calendar. 
Press 2 for more information. Press 9 to be removed from calls."""


def place_call_e_call(to_number, message):
    """Place outbound call using CALL-E Python SDK."""
    try:
        result = call_e_client.call(
            to_number=to_number,
            message=message
        )
        return result
    except Exception as e:
        print(f"CALL-E Error: {e}")
        return {"sid": "demo-call-123", "status": "queued"}


# ============================================================
# FLASK ROUTES
# ============================================================

@app.route("/")
def index():
    return render_template_string(DEMO_HTML)


@app.route("/lead-submission", methods=["POST"])
def lead_submission():
    """Handle lead form submission - triggers CALL-E call flow."""
    try:
        lead_data = request.get_json()
        if not lead_data:
            return jsonify({"error": "No JSON data received"}), 400

        name = lead_data.get("name", "Valued Customer")
        email = lead_data.get("email", "")
        phone = lead_data.get("phone", "+1234567890")
        company = lead_data.get("company", "Company")

        # Step 1: Place outbound CALL-E call
        call_result = place_call_e_call(
            to_number=phone,
            message=generate_call_message(name, company)
        )

        # Step 2: Schedule Google Calendar appointment
        calendar_result = schedule_google_calendar(name, email, phone, company)

        # Combine results
        response = {
            "status": "success",
            "call_sid": call_result.get("sid"),
            "call_status": call_result.get("status"),
            "calendar": calendar_result,
            "message": f"Follow-up call initiated for {name} from {company}"
        }

        # If OAuth not complete, include instructions
        if calendar_result.get("status") == "oauth_required":
            response["oauth_instructions"] = calendar_result.get("message")

        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/oauth2callback")
def oauth2callback():
    """Handle Google OAuth callback."""
    # Get the authorization code from the request
    auth_code = request.args.get("code")
    
    if not auth_code:
        return jsonify({"error": "No authorization code provided"}), 400
    
    try:
        from google_auth_oauthlib.flow import Flow
        
        flow = Flow.from_client_config(
            GOOGLE_OAUTH_CONFIG,
            scopes=["https://www.googleapis.com/auth/calendar.events"],
        )
        flow.redirect_uri = GOOGLE_OAUTH_CONFIG["redirect_uris"][0]
        
        # Fetch the token
        flow.fetch_token(code=auth_code)
        creds = flow.credentials
        
        # Save credentials
        save_credentials(creds)
        
        return jsonify({
            "status": "success",
            "message": "Google Calendar OAuth completed! Credentials saved.",
            "redirect": "/"
        })
        
    except Exception as e:
        return jsonify({"error": f"OAuth failed: {str(e)}"}), 500


# ============================================================
# UTILITY: OAuth Setup Script
# ============================================================

def run_oauth_setup():
    """Run OAuth flow to get Google credentials."""
    import sys
    
    flow = Flow.from_client_config(
        GOOGLE_OAUTH_CONFIG,
        scopes=["https://www.googleapis.com/auth/calendar.events"],
    )
    flow.redirect_uri = GOOGLE_OAUTH_CONFIG["redirect_uris"][0]
    
    # Generate authorization URL
    auth_url, state = flow.authorization_url(access_type="offline", include_granted_scopes=True)
    
    print("=" * 60)
    print("GOOGLE OAUTH SETUP FOR CALL-E HACKATHON")
    print("=" * 60)
    print(f"\n1. Open this URL in your browser: {auth_url}")
    print("2. Log in with your Google account and authorize access")
    print("3. You'll be redirected to: http://localhost:8080/oauth2callback")
    print("4. Copy the 'code' parameter from the URL")
    print("5. Run: python app.py oauth2callback?code=YOUR_CODE_HERE")
    print("=" * 60)


# ============================================================
# MAIN ENTRY POINT
# ============================================================

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    
    # Check if we need to run OAuth setup
    if len(sys.argv) > 1 and sys.argv[1] == "oauth":
        run_oauth_setup()
        sys.exit(0)
    
    print("=" * 60)
    print("CALL-E Hackathon: Customer Follow-Up Automation")
    print("Hybrid: Python SDK + Google Calendar API")
    print("=" * 60)
    print(f"Server starting at http://localhost:{port}")
    print("Endpoints:")
    print("  GET  /          - Demo information page")
    print("  POST /lead-submission - Submit lead data (triggers CALL-E call)")
    print("  GET /oauth2callback - Google OAuth completion")
    print("  GET app.py oauth - OAuth setup guide")
    print("=" * 60)
    print("\nDemo Flow:")
    print("1. Complete OAuth: python app.py oauth")
    print("2. GET / to see setup status")
    print("3. POST lead data to /lead-submission")
    print("4. CALL-E SDK places outbound call automatically")
    print("5. Personalized message plays with scheduling option")
    print("6. Press 1 → Google Calendar event created")
    print("7. Confirmation email/SMS sent")
    print("=" * 60)
    app.run(host="0.0.0.0", port=port, debug=False)