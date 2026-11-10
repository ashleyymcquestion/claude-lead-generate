# Lead capture setup: landing page to Google Sheet

Flow: visitor fills in `landing_page.html` -> the form posts to a Google Apps Script web app -> the script adds a row to your Google Sheet (same columns as `crm_tracker.csv`, plus a few extras).

## What you need
- A Google account to own the Sheet.
- A place to host `landing_page.html` (Netlify, Cloudflare Pages or GitHub Pages) and a domain.
- Your attorney's sign-off on the page text, consent wording, privacy policy and terms before any ad points at it.

## Step 1: Create the Sheet and script (about 10 minutes)
1. Go to sheets.google.com and create a blank sheet named **PFD Lead Tracker**.
2. Menu: **Extensions > Apps Script**. Delete the sample code.
3. Paste in everything from `leads/apps_script/Code.gs`.
4. Optional: set `NOTIFY_EMAIL` near the top to your email to get an alert for each new lead. The alert contains no personal data, only a link to the sheet.
5. Click **Save**, choose the function **setup** in the dropdown, and click **Run**. Approve the permissions when Google asks. This creates two tabs: **Leads** and **Raw Submissions**.

## Step 2: Publish it as a web app
1. Click **Deploy > New deployment**, choose type **Web app**.
2. Execute as: **Me**. Who has access: **Anyone**. (The page has to be able to post to it. Nobody can read your sheet through this link.)
3. Click **Deploy** and copy the **Web app URL** (it ends in `/exec`).
4. If you change the script later, use **Deploy > Manage deployments > Edit > New version** or the URL keeps running the old code.

## Step 3: Connect the page
1. Open `leads/landing_page.html` and find `var ENDPOINT = '';` near the bottom.
2. Paste your Web app URL between the quotes.
3. Fill in the placeholders on the page: legal entity name, mailing address, privacy policy and terms links. Your attorney must approve the text.
4. Upload the page to your host.

## Step 4: Test before any ad runs
1. Open the live page with tags in the link, for example `?utm_source=test&utm_campaign=test1`.
2. Submit the form with your own details. A new row should appear in **Leads** within a few seconds, with the source filled in.
3. Submit again with the same email. You should not get a second row. The existing row's notes will say "Resubmitted".
4. Look at the **Raw Submissions** tab: every attempt is logged there, including rejected ones.
5. Delete your test rows.

## What the script does
- Rejects bots (a hidden field humans never see), bad emails, short phone numbers, and submissions without both checkboxes ticked.
- Adds a row with stage **New Lead**, `accredited_verified` = **No (self-certified only)**, `dnc_checked` = **No**, the consent time, the investable-assets answer, and the ad tags (utm_source, utm_campaign, utm_term and so on).
- Logs every submission, good or bad, so you have a record of consent.

## Ad links
Add tags to each ad's link so you can see which keyword produced each lead. Example:

`https://yourdomain.com/?utm_source=google&utm_medium=cpc&utm_campaign=preferred-return&utm_term={keyword}`

## Limits to know about
- **No IP address.** Apps Script doesn't give the script the visitor's IP. If your attorney wants IP and the exact consent text stored, you'll need a different back end. The sheet records a version label for the consent text (`consent_text_version`) that you should update whenever the wording changes.
- **Sensitive data.** The sheet holds names, phone numbers and financial ranges. Keep sharing limited to people who need it, turn on 2-step verification on the Google account, and ask your attorney how long to keep data and how to handle opt-out and deletion requests.
- **Self-certification is not verification.** Everyone in the sheet must still be verified as accredited under 506(c) before investing.
- **Do not call from the sheet blindly.** Scrub phone numbers against the Do-Not-Call lists first. A web-form consent covers contact about this offering, but your attorney should confirm what it covers for texts and calls.
- **Daily limits.** Free Google accounts cap email sends and script run time per day. That's plenty for a small campaign.
- **Tested only with a simulation.** The script logic was checked with a local test, not against a real Google account.
