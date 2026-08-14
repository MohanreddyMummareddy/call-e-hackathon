"""Simple CALL-E demo project for hackathon submission"""

import os
from call_e_sdk import CALL_EClient

# Initialize CALL-E client with your account API key
api_key = os.environ.get("CALL_E_API_KEY", "your-api-key-here")
client = CALL_EClient(api_key=api_key)


def make_phone_call(to_number, message):
    """Make a phone call using CALL-E API"""
    try:
        response = client.call(
            to_number=to_number,
            message=message
        )
        return response
    except Exception as e:
        print(f"Error making call: {e}")
        return None


def main():
    """Main entry point"""
    print("CALL-E Hackathon Demo")
    print("=" * 40)
    
    # Example usage
    to_number = os.environ.get("DEMO_PHONE_NUMBER", "+1234567890")
    message = os.environ.get("DEMO_MESSAGE", "Hello! This is a CALL-E hackathon demonstration.")
    
    print(f"Calling {to_number}...")
    print(f"Message: {message}")
    
    result = make_phone_call(to_number, message)
    
    if result:
        print(f"Call SID: {result.get('sid', 'N/A')}")
        print(f"Status: {result.get('status', 'N/A')}")
    else:
        print("Call failed. Check your API key and phone number.")


if __name__ == "__main__":
    main()