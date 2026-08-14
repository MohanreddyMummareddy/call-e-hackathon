# CALL-E Hackathon: Public Deployment Guide
# Free hosting options for judge testing (required by rules)

## ⚠️ CRITICAL: Rules Requirement
> "The Entrant must make the Project available free of charge and without any restriction, 
> for testing, evaluation and use by the Sponsor, Administrator and Judges until the Judging Period ends."
> 
> "If Entrant's website is private, Entrant must include login credentials in its testing instructions."

Your project **must be publicly accessible** during the Judging Period (Sep 30 - Oct 13, 2026).

---

## � Option 1: PythonAnywhere (RECOMMENDED)
### Most straightforward for Flask + Python projects

### Free Tier Features:
- 1 web app (always-on)
- 1 scheduled task
- 1 GB storage
- Custom domain (optional)
- Python 3.11+

### Setup Steps:

#### 1. Create Account
1. Go to: https://www.pythonanywhere.com/signup/
2. Choose "Free" plan
3. Verify your email

#### 2. Upload Your Code
1. Log into PythonAnywhere dashboard
2. Go to "Files" tab
3. Click "Upload a file"
4. Upload your `app.py`, `requirements.txt`, `.env` (if needed)
5. Or use Git integration: "Consoles" → `git clone your-repo-url`

#### 3. Install Dependencies
1. Go to "Consoles" → "Bash"
2. Install packages:
   ```bash
   pip install -r requirements.txt
   ```
   *Note: May need to install google-auth libraries first*

#### 4. Configure Web App
1. Go to "Web" tab → "Add a new web app"
2. Choose "Manual configuration"
3. Python version: 3.11 (or whatever you're using)
4. Working directory: `/home/yourusername/your-repo/`

#### 5. Set Up Web App (WSGI)
1. Click the ">" next to your web app
2. Click the "" (code icon) for "WSGI configuration file"
3. Edit to point to your app:
   ```python
   import sys
   import os
   path = '/home/yourusername/call-e-hackathon'
   if path not in sys.path:
       sys.path.insert(0, path)
   
   os.chdir(path)
   from app import app as application
   ```
   *Replace `yourusername` and `call-e-hackathon` with your actual paths*

#### 6. Set Up Virtual Environment (Recommended)
1. In Consoles:
   ```bash
   mkvirtualenv call-e-hackathon --python=python3.11
   workon call-e-hackathon
   pip install -r requirements.txt
   ```

#### 7. Add Static File Server (if needed)
1. Web tab → "The virtualenv and static files for your web app"
2. Check "Serve static files"
3. Set "URL": `/static/`
4. Set "Directory": `/home/yourusername/call-e-hackathon/static/`

#### 8. Reload Web App
1. Web tab → "Reload your web app"
2. Visit: `https://yourusername.pythonanywhere.com/`

#### 9. Configure Environment Variables
1. Go to "Accounts" → "Environment variables"
2. Add:
   ```
   CALL_E_API_KEY=your_call_e_api_key
   GOOGLE_CLIENT_ID=your_google_client_id
   GOOGLE_CLIENT_SECRET=your_google_client_secret
   ```
3. **OR** hardcode in `app.py` using `os.environ.get()` (less secure but simpler for demo)

#### 10. OAuth Setup for Google Calendar
If using Google Calendar integration:

1. In Google Cloud Console:
   - Set authorized redirect URI: `https://yourusername.pythonanywhere.com/oauth2callback`

2. In your app.py:
   - The OAuth callback should work as-is
   - Credentials will be stored in user_token.json in the home directory

3. Test by visiting: `https://yourusername.pythonanywhere.com/oauth2callback`

---

## � Option 2: Render.com
### Modern platform, good free tier

### Free Tier Features:
- 750 hours/month free (always-on web service)
- Custom domains
- Free SSL (HTTPS)
- Deploy from GitHub

### Setup Steps:

#### 1. Create Account
1. Go to: https://render.com/
2. Sign up with GitHub
3. Verify email

#### 2. New Web Service
1. New → Web Service
2. Connect your GitHub repository
3. Repository: `your-username/call-e-hackathon` (or your repo)
4. Branch: `main`
5. Build Command: `pip install -r requirements.txt`
6. Start Command: `python app.py`

#### 2.1 Service Settings
- Name: `call-e-hackathon` (or your choice)
- Root Directory: `/` (if repo root has app.py)
- Plan: Free

#### 3. Environment Variables
1. After service creates, go to "Environment" tab
2. Add variables:
   ```
   CALL_E_API_KEY=your_api_key
   GOOGLE_CLIENT_ID=your_client_id
   GOOGLE_CLIENT_SECRET=your_client_secret
   ```

#### 4. Deploy
1. Click "Create Web Service"
2. Wait 2-3 minutes for first deploy
3. Visit the generated URL (e.g., `https://call-e-hackathon.onrender.com`)

#### 5. Wake Up Frequency
- Free apps sleep after 15 minutes of inactivity
- First request takes 30-60 seconds to "wake up"
- **Solution**: Add a cron job or use a paid plan for always-on

#### 6. Google Calendar OAuth
1. In Google Cloud Console:
   - Add redirect: `https://call-e-hackathon.onrender.com/oauth2callback`

2. The OAuth flow should work similarly to PythonAnywhere

#### 7. Important: Keep Awake
- Free Render apps sleep after inactivity
- **Solution**: Use a "cron" job (free tier supports 1 cron job)
- Or: Accept that judges may need to "wake" the app on first request

---

## � Option 3: Heroku (Classic but Reliable)
### Most well-known Python hosting

### Free Tier Features:
- 550 dyno hours/month (approx. 23 days)
- Custom domains
- Free SSL
- Heroku CLI for easy deployment

### Setup Steps:

#### 1. Create Account
1. Go to: https://heroku.com/
2. Sign up (free)
3. Install Heroku CLI

#### 2. Prepare Your App
1. Create `Procfile` (no extension):
   ```
   web: python app.py
   ```

2. Ensure `requirements.txt` is correct

3. Create `runtime.txt` (optional):
   ```
   python-3.11.0
   ```

#### 3. Create Heroku App
```bash
heroku create call-e-hackathon
# Or: heroku create https://github.com/your-username/call-e-hackathon
```

#### 4. Set Environment Variables
```bash
heroku config:set CALL_E_API_KEY=your_api_key
heroku config:set GOOGLE_CLIENT_ID=your_client_id
heroku config:set GOOGLE_CLIENT_SECRET=your_client_secret
```

#### 5. Deploy
```bash
git push heroku main
# Or push your hackathon branch
git push heroku hackathon-2026-your-name:main
```

#### 6. Open App
```bash
heroku open
# Or visit: https://call-e-hackathon.herokuapp.com
```

#### 7. Google Calendar OAuth
1. In Google Cloud Console:
   - Add redirect: `https://call-e-hackathon.herokuapp.com/oauth2callback`

2. Heroku should handle OAuth similarly

#### 8. Keep Awake
- Free dyno sleeps after 30 days (not hours!)
- Actually: 550 hours/month = ~23 days of continuous use
- After that, manually start: `heroku ps:scale web=1` then `heroku ps:restart`

---

## � Option 4: Railway.app
### Newer, developer-friendly option

### Free Tier Features:
- $5 credit/month (enough for small Flask app)
- Unlimited projects
- Custom domains
- Easy GitHub deployment

### Setup Steps:

#### 1. Create Account
1. Go to: https://railway.app/
2. Sign up with GitHub
3. Get $5 free credit

#### 2. New Project
1. New Project → Deploy from GitHub
2. Connect your repository
3. Railway auto-detects Python/Flask

#### 3. Service Settings
- Root Directory: `/` (if app.py is in root)
- Build Command: `pip install -r requirements.txt`
- Start Command: `python app.py`

#### 4. Environment Variables
1. Go to "Variables" tab
2. Add:
   ```
   CALL_E_API_KEY=your_api_key
   GOOGLE_CLIENT_ID=your_client_id
   GOOGLE_CLIENT_SECRET=your_client_secret
   ```

#### 5. Deploy
1. Railway auto-deploys on push
2. Visit generated URL (e.g., `https://call-e-hackathon.up.railway.app`)

#### 6. Google Calendar OAuth
1. In Google Cloud Console:
   - Add redirect: `https://call-e-hackathon.up.railway.app/oauth2callback`

#### 7. Credit Management
- Free tier gives $5/month
- Flask + Python app typically uses < $1/month
- Monitor in dashboard to avoid charges

---

## � Comparison Table

| Feature | PythonAnywhere | Render.com | Heroku | Railway |
|---------|---------------|------------|--------|---------|
| **Free Tier** | 1 always-on web app | 750 hrs/month | 550 hrs/month | $5 credit/month |
| **Always-On?** | Yes (free) | No (sleeps after 15 min) | Yes (23 days continuous) | Yes (within credit) |
| **Setup Difficulty** | Medium | Easy | Medium | Easy |
| **SSL (HTTPS)** | Included | Included | Included | Included |
| **Google OAuth** | Works | Works | Works | Works |
| **Best For** | Reliable always-on | Quick deployment | Familiar ecosystem | Developer-friendly |
| **Judge Experience** | Fast, consistent | May need "wake" | Reliable | Reliable |

---

## � My Recommendation: PythonAnywhere

**For your hackathon project, I recommend PythonAnywhere because:**

1. ✅ **Always-on on free tier** - Judges can access anytime without "waking up"
2. ✅ **Python-specific** - Best compatibility with CALL-E SDK and Google APIs
3. ✅ **Simple setup** - Less configuration than Heroku
4. ✅ **No credit card required** - Important if you're concerned about fees
5. ✅ **Good for demonstrations** - Consistent experience for all judges

**Alternative: Render.com** if you prefer modern UI and don't mind the sleep/wake behavior.

---

## � Deployment Checklist

### Before Deploying:
- [ ] Test locally: `python app.py` works on localhost:8000
- [ ] Google Calendar OAuth tested (or commented out if using demo mode)
- [ ] CALL-E SDK integration works (test with mock data)
- [ ] All environment variables configured
- [ ] No debug mode in production (debug=False)
- [ ] Error handling for missing credentials

### After Deploying:
- [ ] Visit URL and verify app loads
- [ ] Test `/` route (demo page)
- [ ] Test `/lead-submission` POST with sample data
- [ ] Test OAuth flow if using Google Calendar
- [ ] Verify HTTPS is working (all three platforms provide this)
- [ ] Test on mobile browser (judges may use tablets/iPads)

### For Judging Period:
- [ ] Project remains accessible Oct 1-13, 2026
- [ ] No authentication required (or provide credentials if private)
- [ ] Free of charge (no payment required to access)
- [ ] Works without restrictions
- [ ] Monitor for any downtime/issues
- [ ] Have backup URL or be prepared to quickly redeploy

---

## ⚠️ Critical Rules Compliance

### Testing Access Requirements:
| Requirement | Your Status | Action Needed |
|------------|-------------|---------------|
| Project available free of charge | Check | Ensure no paid access required |
| Available without restrictions | Check | Remove any auth barriers for judges |
| Testing instructions included | Check | Add to Devpost submission |
| Login credentials if private | Check | Either make public OR provide credentials |
| Available until Judging Period ends | Check | Oct 13, 2026 deadline |
| Judges can evaluate solely on description/video | Check | Ensure project is usable |

### If Using Localhost Only (Not Recommended):
- Must provide working credentials for judges to test
- Must explain in Devpost how judges can test
- Risk: Judges may not invest time to set up localhost
- **Better**: Deploy to public URL ASAP

---

## � Quick Start: PythonAnywhere (30-minute summary)

1. Sign up at pythonanywhere.com (Free)
2. Upload your project files
3. `pip install -r requirements.txt` in Consoles
4. Set up Web App, point to app.py
5. Add environment variables in Accounts
6. Reload web app
7. Visit your URL
8. Test all endpoints
9. Update Devpost with URL
10. Submit CALL-E PR with repo URL

---

## � Final Notes

**Deadline Awareness:**
- Submission Period ends: September 14, 2026 (11:45 am SGT)
- Judging Period: September 30 - October 13, 2026
- **Deploy ASAP** - Don't wait until last week

**Judge Experience:**
- Make it easy for judges to test your project
- The easier you make it, the better your Technical Implementation score
- Provide clear testing instructions in all submissions

**Backup Plan:**
- If your free tier app goes down during judging
- Have a quick redeployment plan
- Provide alternative testing method in Devpost submission
- Screenshot working app as part of submission

---