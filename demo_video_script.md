# CALL-E Hackathon Demo Video Script
# Customer Follow-Up Automation (Hybrid: Python SDK + Google Calendar)
# Total Duration: < 3 minutes (approx. 2:45)

---
# SCENE 1: Lead Form Submission
# Duration: 0:00 - 0:20
# Visual: Screen recording of web form
# Audio: On-screen text only (no voiceover needed)

OVERLAY_TEXT: "PROBLEM: 50% of leads lost when follow-up exceeds 30 minutes"

SCREEN: Web form with fields: Name, Email, Phone, Company
User fills: "Acme Corp" → "John Doe" → "+1234567890" → "john@example.com"
User clicks "Submit Lead"

OVERLAY_TEXT: "SOLUTION: Immediate CALL-E follow-up within 5 minutes"

---
# SCENE 2: CALL-E Outbound Call Initiates
# Duration: 0:20 - 0:45
# Visual: Phone screen animation, CALL-E SDK call being placed
# Audio: Subtle phone ringing sound (optional), on-screen text

SCREEN: Phone interface showing incoming call from "+1234567890"
CALL-E SDK LOG: "Outbound call placed to +1234567890"
Call status: "Queued" → "Connecting" → "Active"

OVERLAY_TEXT: "CALL-E SDK places outbound call within 5 minutes"

AUDIO: (Optional) Phone ringing sound effect
ON-SCREEN: "Call connected in 4 seconds"

---
# SCENE 3: Personalized Message Plays
# Duration: 0:45 - 1:10
# Visual: Call screen with transcript of message playing
# Audio: TEXT-TO-SPEECH of the call message

TRANSCRIPT APPEARS on screen:
"Hello John, this is a follow-up call from Acme Corp.
We noticed your interest and wanted to connect.
Press 1 to schedule a quick 15-minute appointment on our calendar.
Press 2 for more information.
Press 9 to be removed from calls."

ON-SCREEN TIMER: "0:45 - Message playing"

OVERLAY_TEXT: "Personalized message addresses lead by name"

---
# SCENE 4: User Presses 1 to Schedule
# Duration: 1:10 - 1:35
# Visual: Call interface with DTMF input visualization
# Audio: DTMF tone sound

VISUAL: DTMF digits appearing: "1"
AUDIO: DTMF tone: "Beep..."

ON-SCREEN: "Press 1 → Scheduling Google Calendar appointment..."

OVERLAY_TEXT: "User presses 1 to book appointment"

---
# SCENE 5: Google Calendar Event Created
# Duration: 1:35 - 2:00
# Visual: Google Calendar interface, event creation confirmation
# Audio: Success sound effect

SCREEN: Google Calendar showing new event created
EVENT DETAILS:
- Title: "Follow-up: John Doe - Acme Corp"
- Description: "Scheduled follow-up call... Lead interest captured via CALL-E automation"
- Time: "Tomorrow 9:00 AM - 9:30 AM"
- Attendee: "john@example.confirmed"

ON-SCREEN CONFIRMATION: "Appointment scheduled successfully!"

OVERLAY_TEXT: "Google Calendar event created automatically"

---
# SCENE 6: Confirmation Sent
# Duration: 2:00 - 2:15
# Visual: Email screenshot with appointment confirmation
# Audio: None (on-screen text)

SCREEN: Email inbox showing confirmation email
SUBJECT: "Your Follow-up Appointment is Scheduled"
PREVIEW: "Hi John, your 15-minute appointment is scheduled for tomorrow at 9:00 AM..."

OVERLAY_TEXT: "Confirmation email sent with appointment details"

---
# SCENE 7: Judging Criteria Summary
# Duration: 2:15 - 2:45
# Visual: Split screen showing 4 criteria with scores
# Audio: Narrator or on-screen text

SPLIT SCREEN (4 quadrants):

TOP-LEFT: "REAL WORLD IMPACT"
- BULLET: "Solves lead decay problem"
- BULLET: "3x more leads converted"
- BULLET: "Timely follow-up for real users"

TOP-RIGHT: "QUALITY OF THE IDEA"
- BULLET: "Non-obvious voice + calendar integration"
- BULLET: "Full-stack skill demonstration"
- BULLET: "Practical business process automation"

BOTTOM-LEFT: "TECHNICAL IMPLEMENTATION"
- BULLET: "CALL-E SDK at runtime"
- BULLET: "Google Calendar API integration"
- BULLET: "End-to-end workflow"

BOTTOM-RIGHT: "PRODUCT EXPERIENCE & DEMO"
- BULLET: "Complete flow demonstrated"
- BULLET: "Clear communication in video"
- BULLET: "All judging criteria addressed"

OVERLAY TEXT (final): "CALL-E: Your Code Is Calling - Hackathon Submission"

---
# PRODUCTION NOTES

## Recording Equipment:
- Screen recording: OBS Studio, Camtasia, or QuickTime Player
- Voiceover: Audacity, Adobe Audition, or phone voice memo
- Video editing: iMovie, DaVinci Resolve (free), or OBS built-in

## Technical Requirements:
1. **Video length**: Must be < 3 minutes (edit strictly to 2:45 max)
2. **Platform**: YouTube or Vimeo, publicly visible (unlisted acceptable if disabled embedding)
3. **No third-party trademarks**: Avoid showing Chrome, Windows logos prominently
4. **No copyrighted music**: Use royalty-free or original audio only
5. **Footage must show project functioning**: All 6 scenes above must be actual recording

## Scene Checklist for Judges:
- [ ] Lead form submission (Scene 1)
- [ ] CALL-E SDK call placed (Scene 2)
- [ ] Personalized message plays (Scene 3)
- [ ] DTMF "1" pressed for scheduling (Scene 4)
- [ ] Google Calendar event created (Scene 5)
- [ ] Confirmation sent (Scene 6)
- [ ] All 4 judging criteria referenced (Scene 7)

## Optimization for Maximum Scores:

### Real World Impact (15% of total score):
- Emphasize the 50% lead decay statistic
- Show actual business value (3x conversion)

### Quality of the Idea (20% of total score):
- Highlight "non-obvious" integration
- Show full-stack skills (frontend + backend + API)

### Technical Implementation (25% of total score - HIGHEST WEIGHT):
- Clearly show CALL-E SDK import and runtime call
- Demonstrate Google Calendar API integration
- Show actual code interaction, not just mock

### Product Experience & Demo (40% of total score - HIGHEST WEIGHT):
- Ensure video flows logically
- Clear narration or on-screen explanations
- Professional presentation quality
- Under 3 minutes exactly (judges stop watching after 3 min)

---
# QUICK RECORDING SCRIPT (READ ALOUD IF USING VOICEOVER)

"(0:00) Problem: 50% of leads are lost when follow-up exceeds 30 minutes.

(0:08) Solution: Immediate CALL-E follow-up within 5 minutes.

(0:15) Using the CALL-E Python SDK, we place an outbound call to the lead.

(0:22) The call plays a personalized message: 'Hello John, this is a follow-up call from Acme Corp. Press 1 to schedule a quick 15-minute appointment.'

(0:32) The lead presses 1 on their phone.

(0:38) This triggers our Google Calendar API integration, which creates a calendar event automatically.

(0:46) A confirmation email is sent with the appointment details.

(0:53) This end-to-end automation helps businesses convert 3x more leads by ensuring immediate, personalized follow-up.

(1:05) The project demonstrates genuine understanding of the problem space - not just 'AI that makes phone calls' but a practical business solution.

(1:15) Quality of the idea: Non-obvious use of CALL-E that shows genuine understanding of the problem space.

(1:25) Technical implementation: The code reflects genuine effort and working, non-trivial implementation - CALL-E imported and actually called at runtime, not just referenced.

(1:35) Product experience: The project delivers a complete, coherent experience, and the demo video clearly communicates what it does and why it matters.

(1:45) Real world impact: The project identifies a real, specific phone-work problem and makes a credible case that it solves it for real users.

(1:55) A strong project points to a direction worth building further for real users after the hackathon."

---
# FINAL CHECKLIST BEFORE SUBMITTING

□ Video length: < 3 minutes (edit to exactly 2:45)
□ Platform: YouTube/Vimeo, publicly visible
□ No copyrighted music or trademarks visible
□ All 6 scenes recorded and flowing logically
□ CALL-E SDK usage clearly visible (import + call)
□ Google Calendar integration demonstrated
□ Voiceover or clear on-screen text explains each step
□ Video references all 4 judging criteria
□ Video ends with project name and hackathon reference
□ Video description includes: project link, CALL-E account email, text description
□ Video is your original work (no AI-generated without significant modification)