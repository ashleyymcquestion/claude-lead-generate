# PFD Lead Tracker

Everything for capturing and tracking leads lives in this folder.

| File | What it is |
|---|---|
| `landing_page.html` | Investor landing page with the accredited-investor and consent checkboxes. The form posts to the Apps Script URL set in `ENDPOINT`. |
| `apps_script/Code.gs` | Google Apps Script that receives each form post and adds a row to your Google Sheet. |
| `SETUP_lead_capture.md` | Step-by-step setup (Sheet, script, web app URL, hosting, testing). |
| `crm_tracker.csv` | Lead tracker template (same columns the Sheet uses). |
| `crm_README.md` | Pipeline stages and lead-scoring guide. |

Research, call sheets, events and attorney forms are in `../leads/`.

Nothing here is live until you complete the setup guide and your attorney approves the page text and consent wording.
