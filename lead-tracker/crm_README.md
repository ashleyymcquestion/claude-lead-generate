# CRM Tracker Guide (`crm_tracker.csv`)

Companion to `05_compliance_checklist.md`. Discussion tool for use with securities counsel; not legal advice.

The three rows in the CSV are marked EXAMPLE (ids `EX-xxx`, names/sources prefixed EXAMPLE, fake `example.com` emails and 555 numbers). Delete them before entering real data.

## Columns

| Column | Use |
|---|---|
| id | Unique id (e.g., L-0001) |
| source | Where the lead came from (be specific and documentable: referral, inbound form, event, purchased list name) |
| type | investor, referral partner, provider, vendor, other. Note: referral partners must not be paid per investor without counsel approval |
| name, firm, email, phone | Contact details; minimize data collected |
| stage | One of the stages below |
| accredited_verified | Yes / No / Pending. Yes ONLY after verification evidence is in the secure file |
| verification_method | Income docs, net worth docs, third-party letter (CPA/attorney/RIA/BD), entity analysis, etc. Never store the documents in the CRM |
| date_first_contact, last_contact | YYYY-MM-DD |
| next_action, next_action_date | One concrete next step and date |
| consent_to_contact | Yes/No plus channel, form (written/verbal), date and source of consent |
| dnc_checked | Yes/No plus scrub date (National and internal DNC) |
| notes | Factual notes only. No promises, return talk, or speculation. Assume notes may be reviewed by regulators or in litigation |

## Stages

1. **New Lead**: identified, no substantive contact. Confirm source, consent, and DNC status before contact.
2. **Contacted**: initial outreach made using approved language only.
3. **Engaged**: replied or took a meeting; interested in learning more.
4. **Qualified**: indicates likely accredited, has capacity for $100k+ minimum, and fits (self-reported only; not verification).
5. **Materials Sent**: received PPM/deck through approved process (PPM only to prospects who appear accredited).
6. **Verification in Progress**: evidence requested or under review (see checklist section 2).
7. **Verified**: reasonable steps completed; documentation filed; approver recorded.
8. **Subscribed**: subscription agreement signed (calendar Form D 15-day and state notice deadlines; first sale triggers them, counsel to confirm).
9. **Funded / Closed**: funds received after verification and acceptance.
10. **Nurture**: not now; follow up on a set schedule if consent permits.
11. **Closed-Lost / Do Not Contact**: declined, not accredited, or opted out. Add to the suppression/DNC list immediately and stop all outreach.

Rules: no one moves to Subscribed or Funded unless `accredited_verified = Yes`. Any opt-out request moves the record to Do Not Contact the same day.

## Lead Scoring (0-100, suggested starting point)

Score is for prioritizing effort, not for deciding who is accredited. Adjust after reviewing results.

| Factor | Points |
|---|---|
| Capacity (likely able to invest $100k+ based on self-report): clear 20 / probable 10 / unknown 0 | 0-20 |
| Accredited likelihood (self-reported or credible indicators; not verified) | 0-20 |
| Interest in private credit/alternative income/healthcare assets: high 15 / some 8 / none 0 | 0-15 |
| Warmth of relationship/source: referral or prior relationship 15 / inbound 12 / cold 3 | 0-15 |
| Engagement (replies, meetings, requests for materials) | 0-15 |
| Timing (ready to decide within 90 days) | 0-10 |
| Compliance readiness (consent documented and DNC clear) | 0-5 |

Tiers: **A** 70+ (priority, personal follow-up); **B** 45-69 (regular cadence); **C** below 45 (nurture/low touch).

Disqualifiers (score 0 / hold): cannot or will not be verified, wants to skip paperwork, uses third-party funds, bad actor concern, opt-out or DNC.

Record the score in `notes` or add a `score` column if you want it sortable (the current required header is unchanged).

## Handling Rules

- Do not contact anyone with `consent_to_contact` blank/unknown or `dnc_checked` No for calls/texts until resolved.
- Keep the CSV free of SSNs, account numbers, tax documents, or financial statements.
- Restrict access, back up, and keep an audit trail; retain records per counsel's schedule.
- Review weekly: overdue next actions, upcoming verification expirations (suggest 90 days), and pending deadlines.
