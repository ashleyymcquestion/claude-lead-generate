"""One-page printable list: this week's OC events with date, time, price."""
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer

ss = getSampleStyleSheet()
sm = ParagraphStyle('sm', parent=ss['BodyText'], fontSize=8.5, leading=10.5)
NAVY = colors.HexColor('#1F3864')
P = lambda t: Paragraph(t, sm)
NL = 'Not listed (check organizer)'
ROWS = [  # date, time, event, venue, price
 ('Tue Oct 6', '10:00 AM (6 Tuesdays to Nov 10)', 'Free Business Accelerator Program', 'Orange County (see listing)', 'FREE'),
 ('Tue Oct 6', '7:00 AM', 'BNI Go Givers (hybrid referral chapter)', 'Hybrid', NL),
 ('Wed Oct 7', 'Evening (time not listed)', 'Orange County Tech & Finance Networking Event', 'Orange County (see listing)', NL),
 ('Wed Oct 7', '6:30 PM', 'Cybersecurity for Everyone', 'Orange County (see listing)', NL),
 ('Wed Oct 7', 'Evening (time not listed)', 'Tech Link Up After Hours', 'Hangar 24, Irvine', NL),
 ('Thu Oct 8', '6:45 AM', 'OC PRO Networkers: Business Referral Networking Breakfast', 'Orange County (see listing)', NL),
 ('Thu Oct 8', '5:00 PM', 'HUSTLE Orange County Entrepreneur Networking', 'Wild Goose Tavern, Newport Beach', NL),
 ('Thu Oct 8', '5:30 PM check-in; 6:30-9:30 PM', 'OCREIA monthly real estate investor meeting (2nd Thursday)', 'Avenue of the Arts Hotel, 3350 Ave of the Arts, Costa Mesa, or Zoom', NL),
 ('Thu Oct 8', 'Evening (time not listed)', 'Free monthly OC real estate investor networking meetup', 'Orange County (see listing)', 'FREE'),
 ('Thu Oct 8', 'Time not listed', 'AI Leadership: 5 Fundamentals', 'Orange County (see listing)', NL),
 ('Thu Oct 8', '5:30-8:30 PM', 'Tech Coast Angels OC Entrepreneur Mixer (UNVERIFIED YEAR)', 'ROC building, 4590 MacArthur Blvd, 3rd floor, Newport Beach', NL),
 ('Fri Oct 9', '10:00 AM', 'BT Legacy Acct: Private Tax Strategy Intensive', 'VEA Newport Beach, a Marriott Resort & Spa', NL),
]
doc = SimpleDocTemplate('PFD_Events_This_Week_List.pdf', pagesize=letter, leftMargin=36, rightMargin=36, topMargin=36, bottomMargin=36,
                        title='Orange County Events - Week of Oct 5, 2026')
els = [Paragraph('Orange County Events: Week of Oct 5-11, 2026', ParagraphStyle('t', parent=ss['Title'], fontSize=18, textColor=NAVY)),
       Paragraph('<b>Confirm before you go.</b> Event sites were blocked, so these come from search-result listings. Prices not shown in the listing are marked '
                 '"Not listed". The Tech Coast Angels date may be from a past year.', sm), Spacer(1, 8)]
data = [['Date', 'Time', 'Event', 'Where', 'Price']] + [[P(a), P(b), P('<b>%s</b>' % c), P(d), P(e)] for a, b, c, d, e in ROWS]
t = Table(data, repeatRows=1, colWidths=[52, 85, 175, 140, 80])
t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), NAVY), ('TEXTCOLOR', (0, 0), (-1, 0), colors.white), ('FONTSIZE', (0, 0), (-1, -1), 8.5),
                       ('GRID', (0, 0), (-1, -1), .4, colors.grey), ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                       ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F2F2F2')])]))
els.append(t)
doc.build(els)
