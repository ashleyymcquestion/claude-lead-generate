# PFD Capital Partners: Inbound Funnel Plan (Rule 506(c))

Status: DRAFT for securities-counsel review. Nothing here is legal advice. Every item marked [ATTORNEY TO APPROVE] must be cleared before launch, including all ads, emails, scripts, and the landing page (`leads/landing_page.html`).

Offering facts used: Irvine, CA issuer; Rule 506(c); accredited investors only; $100k minimum; funds medical receivables for personal-injury (PI) doctors; repaid when insurers or settlements pay; 3:1 collateral target; ~15% annual return target.

## 0. Ground rules for all marketing

1. Never say "guaranteed", "safe", "risk-free", "secured returns", "fixed return", or "no risk". Always write: "targeted ~15% annual return (target, not guaranteed). Loss of principal is possible."
2. 506(c) permits general solicitation, but every sale must be to a verified accredited investor. Public content may describe the opportunity but should avoid specific deal terms beyond what counsel approves. Anti-fraud rules (Rule 10b-5, Cal. Corp. Code 25401) apply to everything.
3. No testimonials or past-performance claims without counsel sign-off and substantiation.
4. Do not pay commissions or per-lead/success fees tied to investments to anyone not a registered broker-dealer (unregistered-broker risk). Paying an ad platform or agency flat media fees is generally fine; confirm with counsel. Lead-gen vendors paid per investor are a red flag.
5. Rule 506(d) bad-actor questionnaires for the issuer, managers, officers, and 20% holders before launch.
6. Keep a dated archive of every ad, post, page version, and email (supports defense and the SEC/state exams).
7. Do not call this a "fund" or "loan" in marketing unless counsel confirms how it should be characterized. Check whether the structure triggers investment company, investment adviser, or California finance lender considerations. [ATTORNEY TO APPROVE]

## 1. Landing page

File: `leads/landing_page.html` (self-contained, light/dark, mobile-friendly). Contains:
- Headline, "how it works" in 4 steps, key terms (target return labeled "target, not guaranteed").
- Risk disclosure: delayed settlements, case losses, collateral valuation, illiquidity, loss of principal, plus concentration/regulatory and "past results" notes.
- Accredited-investor self-certification checkbox (required) and TCPA/CAN-SPAM consent checkbox (required, unchecked by default, separate from the certification, not a condition of purchase).
- Form fields: name, email, phone, investable-assets range.
- Placeholders: [ATTORNEY TO APPROVE] markers, legal entity name, privacy/terms links, physical address (CAN-SPAM), CRM endpoint. The form is intentionally not wired up.

Implementation notes:
- Store consent evidence: timestamp, IP, page version, exact consent text.
- TCPA: marketing calls/texts via autodialer or prerecorded voice need prior express written consent; scrub against the National and California DNC lists; honor STOP immediately; respect calling hours (8am-9pm recipient's local time).
- CAN-SPAM: accurate sender info, physical address, working unsubscribe honored within 10 business days, no deceptive subject lines. California also has additional email rules (B&P 17529.5).
- The self-certification checkbox is NOT verification. State it clearly; no documents or PPM go out until verification is complete (section 4).
- Consider a thank-you page that states next steps and that the investment decision requires verification and PPM review.
- Privacy: CCPA/CPRA notice at collection; don't send investor data to ad pixels beyond what the privacy policy and platform rules allow. Avoid passing investable-assets answers or any financial data to Meta/Google pixels (see platform rules).
- Add a disclosure footer to every page and consider a cookie/consent banner.

## 2. Lead magnet ideas

All gated behind the same form (name, email, phone, assets range, certifications and consents). Content must be educational, balanced, and reviewed by counsel. [ATTORNEY TO APPROVE all]

| # | Asset | Format | Angle |
|---|-------|--------|-------|
| 1 | "Investor's Guide to Medical Receivables" | 10-12 page PDF | How PI medical funding works, who pays, typical timelines, what can go wrong. Balanced risk section up front. |
| 2 | "Due Diligence Checklist: 15 Questions to Ask Any Receivables Fund" | 2-page PDF | Collateral, custody, concentration, case-outcome data, fees, audits. Positions PFD as transparent. |
| 3 | "Alternative Income vs. Public Markets" explainer | Short PDF/email series | Role of private credit in a portfolio; avoids return promises; includes illiquidity warning. |
| 4 | Live webinar: "How Funding PI Medical Receivables Works" | 45 min + Q&A | Co-hosted by management and a PI attorney or healthcare finance expert. Scripted; slides reviewed; recording gated. |
| 5 | On-demand webinar series | 3 x 15 min | (a) Mechanics (b) Risks and how they're mitigated (c) Becoming a verified investor. |
| 6 | "How accredited investor verification works" | One-page FAQ | Reduces drop-off at the verification step; sets expectations. |
| 7 | Quarterly "PI Market Update" newsletter | Email | Settlement-timing trends, regulation news. No performance claims without approval. |
| 8 | Calendar link: 20-minute intro call | Call | Offered after form submit. Script reviewed; no promises. |

Webinar compliance: disclosures on first and last slide and spoken; live Q&A moderated against off-script promises; keep recordings and chat logs.

Nurture sequence (email, opt-in only): Day 0 confirm + guide; Day 2 how it works; Day 5 risks (explicit); Day 8 webinar invite; Day 12 verification explainer; Day 15 call invitation. Each with unsubscribe and address.

## 3. Channel plan

### Targeting
Accredited individuals: physicians and dentists, business owners, executives, real-estate investors, retirees with liquid assets, existing alternative-investment investors, 40-70 age range. Do not target using protected or sensitive financial-status data in a way that platforms prohibit; use interest/job-title proxies.

### 3.1 LinkedIn
- Sponsored content and Lead Gen Forms (gated guide), Conversation Ads; job titles: Physician, Surgeon, Owner, Founder, CEO, Managing Partner, Principal; seniority Director+/Owner; company size and industry filters.
- Organic: founder thought-leadership 2-3x/week (educational, no returns promises), company page, employee advocacy (all posts reviewed).
- Outreach: connection requests to relevant professionals are fine, but cold DMs pitching the offering need counsel review (general solicitation is allowed, but messages must be truthful and non-promissory).
- LinkedIn restricts some financial-product claims; follow its Advertising Policies on financial services (no misleading returns claims).
- Budget guide: $3-5k/mo test; expect high CPL, high quality.

### 3.2 Google Ads (Search + YouTube)
- Restriction: Google's Financial Services verification is required to advertise financial products/services in many regions, and ads must comply with its Financial products and services policy (clear disclosure, no misleading claims, and no unrealistic returns). Complete advertiser verification and any financial services certificate before launching. Also confirm whether "unregulated/speculative" products fall under restricted categories (e.g., Google restricts some speculative financial products). Budget time for rejection and appeals. [VERIFY CURRENT POLICY]
- Keyword themes (exact/phrase; negative-match heavy):
  - Core: "accredited investor opportunities", "506(c) offering", "private credit for accredited investors", "alternative investments accredited investors", "medical receivables investment", "medical receivables fund", "healthcare receivables investing", "medical funding investment", "personal injury medical funding investors", "medical lien investing", "invest in medical liens", "healthcare private credit", "short-term private credit", "asset-backed private lending", "receivables-backed investment", "high-yield alternative investments", "passive income alternative investments", "private placement investments".
  - Long tail: "how to invest in medical receivables", "medical receivables fund accredited", "private credit fund minimum $100k", "alternatives to bonds for accredited investors", "Irvine private investment", "California private credit fund".
  - Negatives: free, jobs, career, course, loan (borrower intent), "get loan", lawsuit loans, pre-settlement funding for plaintiffs, medical billing jobs, crypto, forex, scam, reviews (consider), penny, "how to get funding" (borrower-side), medical debt relief.
- Ad copy rules: headline example "Private Credit for Accredited Investors"; description "Target ~15% annual return (target, not guaranteed). Illiquid; loss of principal possible. Verification required." Keep disclosures on landing page prominent and consistent.
- Landing page needs clear risk disclosure, privacy, entity identity; no misleading claims; fast and mobile-ready.
- YouTube: pre-roll or in-feed ads for the explainer video (60-90 sec) and webinar replay; subject to same Google financial-services policy. Organic channel: explainers, "ask the founder", compliance-reviewed, comments moderated (no promises in replies).

### 3.3 Meta (Facebook/Instagram)
- Restriction: ads for financial products and services must be declared under the Special Ad Category "Financial products and services" when required. In that category, targeting by age, gender, ZIP code, and Lookalike audiences are restricted, so use broad targeting, interests/behaviors still available, and creative that self-selects. Meta also bans misleading or "get rich quick" claims and requires a verified identity/"Paid for by" disclaimers in some regions; some regions require authorization. [VERIFY CURRENT POLICY]
- Use Lead Ads sparingly (limited consent text). Prefer link ads to the landing page with the TCPA consent.
- Do not send sensitive financial data via Pixel/CAPI; follow Meta's rules on prohibited data.
- Retargeting: site visitors and video viewers (subject to special-category limits), with the consent banner.
- Budget guide: $2-4k/mo test.

### 3.4 Podcasts
- Sponsorships/guest spots on finance, alternative investing, physician-investor, and real-estate podcasts.
- Host-read ads must use approved script with disclosures ("target, not guaranteed; risk of loss; accredited investors only; verification required"). Hosts who are not registered should not be paid per investor; use flat-fee sponsorship only, and have the host-read script and show notes reviewed. [ATTORNEY TO APPROVE]
- Own podcast option: "Private Credit Explained" interviews with healthcare finance and legal guests.
- Use unique vanity URLs (pfdcapital.com/podcastname) for attribution.

### 3.5 SEO / content
- Pillar pages: "What are medical receivables?", "How PI medical funding works", "What is a 506(c) offering?", "How accredited investor verification works", "Risks of investing in medical receivables", "Private credit vs. bonds".
- Target keywords (informational): medical receivables investing, what is medical factoring, PI medical lien investing, medical lien funds, healthcare receivables private credit, accredited investor definition, 506(b) vs 506(c), how to verify accredited investor status, private credit minimum investment, short-duration alternative investments, personal injury medical funding explained, letters of protection medical billing, medical lien risks, alternative investments for physicians.
- Technical: schema markup (Organization, FAQ), fast pages, local SEO (Irvine, Orange County), Google Business Profile.
- Each article has a risk-and-disclosure block and a CTA to the guide. Avoid return claims in titles/meta descriptions.
- Link building: legal and healthcare-finance publications, guest posts, directory listings (e.g., reputable alternative-investment platforms; confirm no unregistered-broker issues).

### 3.6 Measurement
KPIs: CPL, form-to-call rate, call-to-verification rate, verification-to-funded rate, CAC per funded investor, average ticket. Segment by channel/UTM. Weekly review. Keep compliance review SLA (48 hours) for new creative.

## 4. 506(c) verification workflow

Requirement: issuer must take "reasonable steps to verify" accredited status; self-certification alone is insufficient. Verify before accepting funds/countersigning subscription.

Workflow:
1. Lead submits form (self-certification + consents) -> CRM tag "Lead - Unverified".
2. Qualification call: confirm interest, explain verification, no promises, no PPM yet (or PPM only after verification, per counsel). Offer facts: min $100k, risks, liquidity.
3. Send verification request. Choose method:
   a. Third-party verification service: e.g., VerifyInvestor.com, Parallel Markets, or similar. Investor uploads documents or connects accounts; service issues a verification letter/certificate (typically valid ~90 days; confirm). Cost often paid by issuer or investor; confirm disclosure.
   b. Letter from a registered broker-dealer, SEC-registered investment adviser, licensed attorney, or CPA (or other qualifying professional) stating they took reasonable steps within the prior three months and determined the person is accredited.
   c. Document review by issuer (Rule 506(c)(2)(ii) non-exclusive methods):
      - Income test: IRS forms (W-2, 1099, K-1, Form 1040) for the two most recent years plus a written representation of expectation to reach the threshold in the current year.
      - Net-worth test: bank, brokerage, and other statements, and a consumer-report (credit report) from a nationwide agency dated within the prior three months, plus written representation that liabilities are disclosed.
   d. Prior verification: for an investor previously verified by the issuer, a written representation of continued accredited status can be relied on for up to five years (confirm current SEC guidance). Use for repeat investors/roll-overs. [ATTORNEY TO CONFIRM]
   e. Minimum-investment approach: per SEC staff no-action relief (March 2025), an issuer may treat "reasonable steps" as satisfied for a high minimum investment - $200,000 for natural persons ($1,000,000 for entities) - if there's no actual knowledge to the contrary and the investor gives written representations that (i) they are accredited and (ii) the minimum investment is not financed in whole or part by a third party for the purpose of making the investment. NOTE: PFD's $100k minimum is below the $200k natural-person level, so this option is unavailable unless counsel approves a different structure or raised minimum. If you raise the minimum to $200k+, it could simplify onboarding, but it is a tradeoff against lead volume. Also confirm any "5-year" rule you intend (user brief mentioned a 5-year minimum-investment option; confirm with counsel whether this refers to the prior-verification five-year reliance in 4d or to the March 2025 relief). [ATTORNEY TO APPROVE]
4. Review result: compliance officer checks letter date, name match, method, and any red flags (e.g., financing by third party, inconsistent info). If red flags, do not rely on it.
5. Mark "Verified" with date, method, reviewer. Keep records (documents or letter, representations, notes) for at least the offering period plus 5 years.
6. Send PPM, subscription agreement, investor questionnaire; collect bad-actor/representation confirmations; KYC/AML screening (OFAC) per your AML policy. [ATTORNEY TO APPROVE]
7. Accept subscription only after verification is current (third-party letters within 3 months of sale). Re-verify if sale is delayed.
8. Funding -> countersign -> record "first sale" date for filings (section 5) -> welcome pack.
9. Privacy and data security: encrypt documents, restrict access, retention schedule.

Rule: never accept money from an unverified person; reject subscription if verification is not complete.

## 5. Filing reminders (calendar these)

| Item | Deadline | Notes |
|------|----------|-------|
| Form D (SEC, EDGAR) | Within 15 calendar days after the first sale (date the first investor is irrevocably contractually committed). If the due date falls on a weekend/holiday, next business day. | Need EDGAR access codes (Form ID, with notarized authentication) well before the first sale - allow weeks. Check the 506(c) box. Amend annually if offering continues, and for material changes. File a closing amendment when the offering ends. |
| California notice filing (DFPI) | Within 15 days of first sale in California (Cal. Corp. Code 25102.1(d)); file Form D via NASAA EFD with fee. | Fee is tiered by offering amount (confirm current schedule on the DFPI site). Also file for each other state where investors reside, within that state's deadline (typically 15 days after first sale in the state). Confirm current EFD process. |
| Other states' notice filings | Generally 15 days after first sale in that state | Track investor state of residence; fees vary. |
| Form D annual amendment | Each year by the anniversary of the initial filing if offering continues | Also if material mistakes or changes. |
| Rule 506(d) bad-actor diligence | Before offering begins and updated at each sale | Written questionnaires; disclosure of pre-2013 events. |
| Form D general solicitation | Not required to be filed before use (the former Form D advance filing requirement was dropped) | Confirm with counsel. |
| Marketing records | Retain through offering + 5 years | Ads, webpages, emails, scripts, verification files. |
| Anti-fraud / PPM updates | Ongoing | Update PPM and marketing when facts change (e.g., collateral ratio, performance). |
| Annual state renewals/amendments | Per state | Calendar. |

Pre-launch checklist:
- [ ] Counsel approves landing page, ads, emails, scripts, webinar deck
- [ ] PPM, subscription agreement, operating agreement finalized
- [ ] EDGAR access obtained
- [ ] Verification vendor selected and tested
- [ ] Bad-actor questionnaires completed
- [ ] Google financial-services verification and Meta special-ad-category setup done
- [ ] TCPA consent logging, DNC scrubbing, CAN-SPAM address and unsubscribe live
- [ ] Privacy policy and terms published
- [ ] Broker-dealer / finder compensation policy confirmed (no unregistered transaction-based pay)
- [ ] Investment-company, adviser, and California lending-law analysis done

Items flagged [VERIFY CURRENT POLICY] or [ATTORNEY TO CONFIRM] reflect rules and platform policies that change; confirm before relying on them.
