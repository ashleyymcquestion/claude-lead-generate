"""Printable attorney consultation form for the PFD outreach review."""
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, KeepTogether, PageBreak

ss = getSampleStyleSheet()
H = ParagraphStyle('h', parent=ss['Heading2'], textColor=colors.HexColor('#1F3864'), spaceBefore=10, spaceAfter=4)
B = ParagraphStyle('b', parent=ss['BodyText'], fontSize=9.5, leading=12)
S = ParagraphStyle('s', parent=B, fontSize=8, leading=10, textColor=colors.HexColor('#444444'))
Q = ParagraphStyle('q', parent=B, fontSize=9.5, leading=12)
NAVY = colors.HexColor('#1F3864')

BACKGROUND = ("PFD Capital Partners (Irvine, CA) is raising capital under Rule 506(c): $100,000 minimum, verified accredited investors only. "
 "The investment funds medical receivables for personal-injury doctors with a 3:1 collateral setup; the return is described as a <b>target</b>, never guaranteed. "
 "We built a call sheet of 239 professional firms in 40+ states (CPAs, estate and trust attorneys, independent RIAs, physician advisors, a few family offices and angel groups). "
 "We want to call their published main business lines and email general business addresses to ask whether they would introduce accredited clients. "
 "We are not asking them to buy. Numbers came from public search listings and are not yet verified on each firm's site. "
 "Attached: PFD_Call_Sheet.pdf and PFD_Call_Sheet_Details.xlsx.")

SECTIONS = [
 ('A. Phone calls', [
  'Do federal Do-Not-Call rules (TCPA and the FTC Telemarketing Sales Rule) and California rules apply to calls to a firm\'s main business line? Is there a business-to-business exemption, and does it hold for a securities offering?',
  'Do we still need to scrub against the National and California Do-Not-Call lists and keep an internal do-not-call list? Do any states on our list have their own rules?',
  'What are the permitted calling hours, and who may place the calls?',
  'Do we need to disclose or get consent for call recording? Which states require two-party consent?',
  'What must a caller say at the start (company name, purpose), and what must they not say about returns, collateral and safety?',
  'If a number turns out to be an individual\'s direct line or mobile, what is the rule?']),
 ('B. Emails', [
  'Does CAN-SPAM apply to email to a firm\'s general business address? What must every email include (physical address, opt-out, accurate sender)?',
  'Do California or other states limit emailing a named partner, as opposed to a general inbox?',
  'Which address sources are safe (published on the firm\'s own site) and which are not (harvested or purchased)?',
  'How long may we keep a contact on the list, and how fast must we honor an opt-out?']),
 ('C. Securities rules (506(c))', [
  'Does 506(c) general solicitation cover outreach to firms? Must written materials be approved before use?',
  'If a firm introduces a client, what must be done before taking money (verification method, subscription documents, bad-actor checks)?',
  'Can we offer a referral firm anything of value? Could a fee make the firm an unregistered broker-dealer or put our exemption at risk? What is the compliant route?',
  'What may the referring firm say to its clients? Do CPA, attorney and RIA professional rules limit recommending investments or accepting referral compensation?',
  'Does contacting firms in other states trigger notice filings or registration? Which states, and when?',
  'Which Form D and California notice filings are required, and by when?']),
 ('D. Content and claims', [
  'Please review our scripts, emails, landing page and FAQ (04_outreach_playbook.md, landing_page.html).',
  'What must we have on hand to substantiate our claims about the 3:1 collateral and the target return?',
  'What risk disclosures must accompany any mention of the return?',
  'Can we describe the offering to a referral firm before they have seen the PPM, or only after?']),
 ('E. Health-care angle', [
  'Because investor money funds personal-injury doctors, are there anti-kickback, fee-splitting or lien-related issues if physician advisors, practice brokers or medical groups refer investors?',
  'Should the investor message be kept separate from what we say to providers?']),
 ('F. Records and process', [
  'What records should we keep for each contact (date, who, what was said, consent, DNC check)?',
  'Should we limit the call sheet (drop wirehouse-affiliated firms, certain states) until you sign off?',
  'Do we need an internal compliance policy for calls and emails, and who should review it?']),
]

def box(): return '[   ]'
def answer_table(n, text):
    head = Paragraph(f'<b>{n}.</b> {text}', Q)
    opts = Paragraph(f'{box()} Yes &nbsp;&nbsp; {box()} No &nbsp;&nbsp; {box()} Depends / need more info &nbsp;&nbsp;&nbsp; {box()} Action item', S)
    lines = Table([[''], ['']], colWidths=[500], rowHeights=[14, 14])
    lines.setStyle(TableStyle([('LINEBELOW', (0, 0), (-1, -1), .4, colors.grey)]))
    t = Table([[head], [opts], [Paragraph('Attorney notes:', S)], [lines]], colWidths=[520])
    t.setStyle(TableStyle([('BOX', (0, 0), (-1, -1), .6, NAVY), ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#EEF2F8')),
                           ('TOPPADDING', (0, 0), (-1, -1), 3), ('BOTTOMPADDING', (0, 0), (-1, -1), 2)]))
    return KeepTogether([t, Spacer(1, 6)])

def footer(c, d):
    c.saveState(); c.setFont('Helvetica', 7.5); c.setFillColor(colors.grey)
    c.drawString(46, 24, 'PFD Capital Partners | Attorney consultation form | Confidential: prepared for discussion with counsel; not legal advice')
    c.drawRightString(566, 24, f'Page {d.page}'); c.restoreState()

doc = SimpleDocTemplate('PFD_Attorney_Consultation_Form.pdf', pagesize=letter, leftMargin=46, rightMargin=46, topMargin=40, bottomMargin=40,
                        title='PFD Attorney Consultation Form')
els = [Paragraph('Attorney Consultation Form', ParagraphStyle('t', parent=ss['Title'], textColor=NAVY, fontSize=22)),
       Paragraph('Outreach to the PFD Call Sheet: Phone, Email and 506(c) Compliance', ParagraphStyle('st', parent=B, fontSize=11, alignment=1))]
meta = Table([['Attorney:', '', 'Date:', ''], ['Firm:', '', 'Meeting type:', '[  ] Phone   [  ] Video   [  ] In person'], ['Prepared by:', '', 'Attendees:', '']],
             colWidths=[65, 180, 80, 195])
meta.setStyle(TableStyle([('FONTSIZE', (0, 0), (-1, -1), 9), ('LINEBELOW', (1, 0), (1, -1), .4, colors.grey), ('LINEBELOW', (3, 0), (3, -1), .4, colors.grey),
                          ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'), ('FONTNAME', (2, 0), (2, -1), 'Helvetica-Bold'), ('TOPPADDING', (0, 0), (-1, -1), 6)]))
els += [Spacer(1, 8), meta, Paragraph('Background for counsel', H), Paragraph(BACKGROUND, B)]
n = 0
for title, qs in SECTIONS:
    els.append(Paragraph(title, H))
    for q in qs:
        n += 1; els.append(answer_table(n, q))
els.append(PageBreak())
els.append(Paragraph('Written go / no-go by channel', H))
go = [['Channel', 'Approved', 'With conditions', 'Not approved', 'Conditions / notes']]
for ch in ['Phone calls to firms\' main business lines', 'Email to firms\' general business addresses', 'Email / calls to named partners', 'Contact with individual investors', 'Paying or offering referral compensation', 'Outreach in states outside California']:
    go.append([Paragraph(ch, B), '[  ]', '[  ]', '[  ]', ''])
gt = Table(go, colWidths=[160, 55, 80, 70, 155], rowHeights=[28] + [34] * 6)
gt.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), NAVY), ('TEXTCOLOR', (0, 0), (-1, 0), colors.white), ('FONTSIZE', (0, 0), (-1, -1), 8.5),
                        ('GRID', (0, 0), (-1, -1), .5, colors.grey), ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'), ('ALIGN', (1, 0), (3, -1), 'CENTER')]))
els += [gt, Paragraph('Steps to complete before the first call (attorney checklist)', H)]
for i in range(1, 9):
    els.append(Table([[f'[  ]  {i}.', '']], colWidths=[50, 470], rowHeights=[20], style=[('LINEBELOW', (1, 0), (1, 0), .4, colors.grey), ('FONTSIZE', (0, 0), (-1, -1), 9)]))
els += [Paragraph('Our to-do list before the meeting', H)]
for t in ['Scrub call sheet numbers against National and California Do-Not-Call lists (needs our registered account).',
          'Spot-check about 20 numbers on firms\' own websites.',
          'Bring current scripts, emails and landing page.',
          'List the states we most want to reach: ______________________________________']:
    els.append(Paragraph(f'[  ] {t}', B))
els += [Spacer(1, 18), Table([['Attorney signature:', '', 'Date:', '']], colWidths=[100, 220, 40, 120],
        style=[('LINEBELOW', (1, 0), (1, 0), .5, colors.black), ('LINEBELOW', (3, 0), (3, 0), .5, colors.black), ('FONTSIZE', (0, 0), (-1, -1), 9)])]
doc.build(els, onFirstPage=footer, onLaterPages=footer)
print(n, 'questions')
