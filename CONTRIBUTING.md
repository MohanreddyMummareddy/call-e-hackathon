# CALL-E: awesome-phone-call-agents Contribution Guidelines

## How to Submit Your Hackathon Project

Follow these steps to submit your CALL-E integration via pull request:

---

## Step 1: Fork & Clone

```bash
# Fork the repository at https://github.com/CALLE-AI/awesome-phone-call-agents
# Then clone your fork
git clone https://github.com/YOUR-USERNAME/awesome-phone-call-agents.git
cd awesome-phone-call-agents
```

---

## Step 2: Create a New Branch

```bash
# Always create a new branch for your contribution
git checkout -b hackathon-2026-your-name
# Example: git checkout -b hackathon-2026-john-doe
```

---

## Step 3: Add Your Integration

Follow the existing repository structure. Based on your hybrid project:

### For Python SDK Integrations:
Place your integration in the appropriate directory:

```bash
# Example structure (adjust based on actual repo)
/agent_skills/          # Custom CALL-E skills/plugins
/workflow_plugins/      # Workflow integrations
/integrations/          # Third-party API connections

# Your Google Calendar integration would go in:
/integrations/google_calendar/
# Or within /agent_skills/ as a new skill
```

### Create Your Integration File:
```python
# example: agent_skills/google_calendar_followup.py
"""
CALL-E Google Calendar Follow-up Skill
Integrates CALL-E with Google Calendar for automated appointment scheduling.
"""

from call_e_sdk import CALL_EHandler

def google_calendar_followup(call_data):
    """
    Process CALL-E call data and schedule Google Calendar event.
    
    Args:
        call_data: Dict with keys: name, email, phone, company
    
    Returns:
        Dict with scheduling result
    """
    # Import Google Calendar integration
    import sys
    sys.path.append('.')
    from app import schedule_google_calendar
    
    result = schedule_google_calendar(
        name=call_data.get("name", ""),
        email=call_data.get("email", ""),
        phone=call_data.get("phone", "+1"),
        company=call_data.get("company", "")
    )
    
    return {
        "status": result.get("status"),
        "event_id": result.get("event_id"),
        "message": "Google Calendar event scheduled" if result.get("status") == "success" else result.get("message")
    }
```

---

## Step 4: Update README (if applicable)

Add your integration to the repository README:

```markdown
## Hackathon Submissions

### Customer Follow-Up Automation
- **Integrator**: Your Name (your-email@example.com)
- **Description**: CALL-E Python SDK + Google Calendar API for automated lead follow-up
- **Features**: Outbound AI calls, timezone-aware slot offers, auto-calendar booking
- **Demo**: https://youtube.com/watch your demo video
- **CALL-E Account**: your-email@example.com
```

---

## Step 5: Test Your Integration

Ensure your code works with the CALL-E SDK:

```bash
# Run any existing tests
python -m pytest test*.py  # if tests exist

# Or manually test
python your_integration_file.py
```

**Requirements**:
- Code must work at runtime (CALL-E imported and called)
- No errors on CALL-E skill loading
- Proper error handling for missing credentials
- Clear documentation in comments

---

## Step 6: Commit & Push

```bash
# Stage your changes
git add .

# Commit with descriptive message
git commit -m "hackathon-2026: Add Google Calendar follow-up integration

- CALL-E Python SDK integration
- Google Calendar API for appointment scheduling
- Timezone-aware slot offers from live calendar availability
- Designed for CALL-E: Your Code Is Calling hackathon"
```

---

## Step 7: Create Pull Request

1. Go to: https://github.com/CALLE-AI/awesome-phone-call-agents/compare
2. **Compare branch**: `hackathon-2026-your-name` (your branch)
3. **Base branch**: `main` (or default branch)
4. **Title**: `Hackathon 2026: Google Calendar Follow-Up Integration`
5. **Description**: Fill in the PR template below

---

## Pull Request Template

```markdown
## Description
Brief description of your CALL-E integration for the hackathon.
Includes Python SDK usage and third-party API integration.

## Changes
- Added google_calendar_followup.py skill integration
- Updated README with hackathon submission details
- Tested with CALL-E outbound call flow

## How It Works
1. User receives CALL-E outbound call
2. AI agent offers available 30-min slots in the lead's timezone
3. Lead confirms the slot and timezone verbally
4. Google Calendar event is created automatically
5. Gmail confirmation sent to lead

## Technical Details
- **CALL-E SDK**: Used for outbound call functionality
- **Third-Party API**: Google Calendar API + Gmail API (OAuth 2.0)
- **Integration Type**: Agent skill for workflow automation
- **Setup Requirements**: Google Cloud credentials needed

## Testing
- Tested with real CALL-E outbound calls
- Google OAuth flow verified (setup instructions included)
- End-to-end flow: call → slot offer → timezone confirmation → calendar event → email

## Screenshots/Videos
- Demo video: https://youtube.com/watch?v YOUR_VIDEO_ID
- Screenshots of calendar event creation

## Checklist
- [ ] Code follows repository style guidelines
- [ ] Includes proper error handling
- [ ] Documentation updated
- [ ] Tested with CALL-E SDK
- [ ] No breaking changes to existing functionality
- [ ] Hackathon compliance verified (eligibility, IP, etc.)
```

---

## Step 8: Post-Submission

After creating the PR:

1. **Monitor**: Respond to reviewer comments within 24 hours
2. **Update**: Make any requested changes to your branch
3. **Keep Updated**: Pull from upstream main branch regularly
   ```bash
   git remote add upstream https://github.com/CALLE-AI/awesome-phone-call-agents.git
   git fetch upstream
   git checkout main
   git merge upstream/main
   git push origin hackathon-2026-your-name
   ```
4. **Hackathon Submission**: After PR acceptance, update your Devpost submission with the PR URL

---

## Important Notes for Hackathon Participants

### Eligibility Verification
- Ensure your GitHub account doesn't violate eligibility rules
- No residents of sanctioned countries (Brazil, Quebec, Russia, etc.)
- No promotion entity employees acting as judges

### IP & Ownership
- Your submission must be original work
- Sole ownership with no other person/entity having rights
- Open source licenses complied with (if applicable)
- Third-party assistance allowed only if you own all rights

### Judging Considerations
- PR will be evaluated during Judging Period (Sep 30 - Oct 13, 2026)
- Judges may test your integration at runtime
- Must work with CALL-E SDK at runtime (not just referenced)
- Demonstrable functionality preferred over theoretical implementation

### Submission Deadline
- **Submission Period ends**: September 14, 2026 (11:45 am SGT)
- **PR should be submitted before**: September 13, 2026 (to allow testing)
- **No changes allowed after**: Submission Period ends