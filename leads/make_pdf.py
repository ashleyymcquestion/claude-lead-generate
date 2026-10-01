"""Build a printable call sheet of firms with a published main business phone."""
import csv, glob, re
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak

EXCLUDE = ('ocreia', 'real estate investors association', 'windfall advisors')  # association / conflicting data
rows = []
for r in csv.DictReader(open('firms_with_phone.csv')):
    if any(x in r['Firm'].lower() for x in EXCLUDE): continue
    city = r['City'].split('(')[0].strip()
    rows.append(dict(firm=r['Firm'], cat=r['Category'], loc=city + ', CA', phone=r['Main phone (verify before calling)'],
                     contact=r['Contact name'], conf=r['Contact confidence'], src=r['Contact source URL']))
for f in sorted(glob.glob('national_*.csv')):
    for r in csv.DictReader(open(f)):
        ph = (r.get('main_phone') or '').strip()
        if not ph or not re.search(r'\d{3}\D*\d{4}', ph): continue
        rows.append(dict(firm=r['firm'], cat=r['category'], loc=f"{r['city']}, {r['state']}", phone=ph,
                         contact=r.get('contact_name', ''), conf=r.get('confidence', ''), src=r.get('source_url', '')))
seen, uniq = set(), []
for r in rows:
    k = re.sub(r'\D', '', r['phone'])[-10:]
    if k in seen: continue
    seen.add(k); uniq.append(r)
uniq.sort(key=lambda r: (r['loc'].split(', ')[-1] != 'CA', r['loc'].split(', ')[-1], r['firm'].lower()))

ss = getSampleStyleSheet()
sm = ParagraphStyle('sm', parent=ss['BodyText'], fontSize=7.5, leading=9)
doc = SimpleDocTemplate('PFD_Call_Sheet.pdf', pagesize=landscape(letter), leftMargin=28, rightMargin=28, topMargin=30, bottomMargin=30,
                        title='PFD Capital Partners - Referral Partner Call Sheet')
els = [Paragraph('PFD Capital Partners: Referral Partner Call Sheet', ss['Title']),
       Paragraph(f'{len(uniq)} firms with a published main business phone number. Business main lines only; no personal or mobile numbers.', ss['BodyText']),
       Paragraph('<b>Before dialing:</b> verify each number on the firm\'s own site, scrub against your Do-Not-Call lists (national, California, internal), '
                 'call 9am-9pm recipient time, and use only attorney-approved scripts. Numbers were taken from search listings and are unverified. '
                 'Do not promise or guarantee returns.', sm), Spacer(1, 8)]
data = [['#', 'Firm', 'Type', 'Location', 'Main phone', 'Contact', 'Conf.', 'DNC\nscrubbed', 'Date\ncalled', 'Outcome / notes']]
for i, r in enumerate(uniq, 1):
    data.append([i, Paragraph(r['firm'], sm), Paragraph(r['cat'], sm), Paragraph(r['loc'], sm), r['phone'],
                 Paragraph(r['contact'], sm), r['conf'][:1].upper(), '[  ]', '', ''])
t = Table(data, repeatRows=1, colWidths=[20, 150, 90, 80, 78, 85, 28, 45, 45, 120])
t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1F3864')), ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('FONTSIZE', (0, 0), (-1, -1), 7.5), ('GRID', (0, 0), (-1, -1), .4, colors.grey), ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F2F2F2')])]))
els += [t, Spacer(1, 6), Paragraph('Conf.: H = high, M = medium, L = low confidence in contact details.', sm)]
doc.build(els)
print(len(uniq), 'firms')
