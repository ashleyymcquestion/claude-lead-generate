"""Printable one-week OC networking list tailored to PFD (week of Oct 5-11, 2026)."""
from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer

ss = getSampleStyleSheet()
sm = ParagraphStyle('sm', parent=ss['BodyText'], fontSize=8, leading=9.5)
bd = ParagraphStyle('bd', parent=ss['BodyText'], fontSize=9, leading=11)
NAVY = colors.HexColor('#1F3864')
P = lambda t: Paragraph(t, sm)

# (date, time, event, place, why it fits PFD, how to work it, fit, status)
THIS_WEEK = [
 ('Thu Oct 8', '5:30-9:30 PM', 'OCREIA monthly meeting (2nd Thursday)', 'Avenue of the Arts Hotel, 3350 Ave of the Arts, Costa Mesa (or Zoom)',
  'Real estate investors and private lenders; many are accredited and understand secured, short-duration lending.', 'Arrive for 5:30 check-in. Ask who they use as CPA/attorney. Collect cards; no pitching returns.', 'A', 'Recurring schedule; confirm at ocreia.com or 866-200-1435'),
 ('Thu Oct 8', 'Evening (check listing)', 'Free monthly OC real estate investor networking meetup', 'Orange County (see listing)',
  'Investors, lenders, JV partners; billed as "bring a deal, find capital".', 'Introduce PFD as medical receivables funding; ask for CPA/attorney introductions.', 'A', 'From a search listing; confirm time and venue'),
 ('Wed Oct 7', 'Evening', 'Orange County Tech & Finance Networking Event', 'Orange County (see listing)',
  'Finance professionals and business owners; possible advisors and accredited investors.', 'Focus on advisors, CPAs and fund people; ask about their client base.', 'A', 'From a search listing; confirm details'),
 ('Fri Oct 9', '10:00 AM', 'BT Legacy Acct: Private Tax Strategy Intensive', 'VEA Newport Beach, a Marriott Resort & Spa',
  'Tax-strategy audience of high-income and high-net-worth attendees; CPAs and advisors likely present.', 'Confirm it is open to the public and not a private client event before you go.', 'A', 'From a search listing; may be invitation or ticketed'),
 ('Thu Oct 8', '5:00 PM', 'HUSTLE Orange County Entrepreneur Networking', 'Wild Goose Tavern, Newport Beach',
  'Business owners and entrepreneurs; some accredited, plus professionals.', 'Light networking; collect cards, follow up with an opt-in invite.', 'B', 'From a search listing'),
 ('Thu Oct 8', '5:30-8:30 PM', 'Tech Coast Angels: OC Entrepreneur Mixer (listing says Oct 8; year unconfirmed)', 'ROC building, 4590 MacArthur Blvd, 3rd floor, Newport Beach',
  'Angel investors are typically accredited. This is the highest-value room if the date is current.', 'Verify the date on tcaventuregroup.com before going.', 'A?', 'UNVERIFIED YEAR: the page may be from a past year'),
 ('Tue Oct 6, Wed Oct 7', '7:00 AM (BNI); evening (Tech Link Up)', 'BNI Go Givers; Tech Link Up After Hours (Hangar 24, Irvine)', 'Hybrid / Irvine',
  'Referral-based groups. Members include CPAs, attorneys, mortgage and insurance people who may know accredited clients.', 'Visit as a guest; ask for introductions, not investments.', 'B', 'From a search listing'),
 ('Thu Oct 8', '6:45 AM', 'OC PRO Networkers: Business Referral Networking Breakfast', 'Orange County (see listing)',
  'Referral breakfast with professional-services members.', 'Ask about CPAs, estate attorneys and wealth advisors in the group.', 'B', 'From a search listing'),
 ('Wed Oct 7, Thu Oct 8', 'Various', 'Cybersecurity for Everyone; AI Leadership (5 Fundamentals)', 'Orange County',
  'Mostly general business crowd. Lower fit for accredited investors.', 'Skip unless you have extra time.', 'C', 'From a search listing'),
]
COMING = [
 ('Oct 21-23', 'Opal Family Office & Private Wealth Forum West', 'Napa', 'Family offices and wealth managers; $2,895-$3,195'),
 ('Oct 22', 'OCBC Economic Forecast', 'Orange County', 'Business leaders'),
 ('Oct 23 (check year)', 'Newport Beach Chamber Economic Forecast ($75)', 'Newport Beach', 'Business leaders; unconfirmed year'),
 ('Oct 28-29', 'RIA Edge Orange County', 'Dana Point', 'Registered investment advisors'),
 ('Nov 10', 'CFA Society OC PORTFOLIO', 'Orange County', 'Investment professionals'),
 ('Nov 12', 'ACG LA: State of Private Credit ($185-$235)', 'LA area', 'Private credit professionals'),
 ('Nov 18', 'FPA Orange County quarterly meeting ($150 non-member)', 'Orange County', 'Financial planners (referral source)'),
]
fitcol = {'A': '#C6EFCE', 'A?': '#FFEB9C', 'B': '#FFF2CC', 'C': '#EDEDED'}

def build():
    doc = SimpleDocTemplate('PFD_Networking_This_Week.pdf', pagesize=landscape(letter), leftMargin=26, rightMargin=26, topMargin=28, bottomMargin=28,
                            title='PFD Networking Events - Week of Oct 5, 2026')
    els = [Paragraph('PFD Capital Partners: Orange County Networking, Week of Oct 5-11, 2026', ParagraphStyle('t', parent=ss['Title'], fontSize=17, textColor=NAVY)),
           Paragraph('<b>Read first:</b> I could not open event sites (Eventbrite, ACG and others were blocked), so this list comes from search-result listings only. '
                     'Confirm every date, time, venue and price on the organizer\'s page before you go. No event confirmed as exclusively for accredited investors or PI medical funding turned up.', bd),
           Spacer(1, 6)]
    data = [['Fit', 'Date', 'Time', 'Event', 'Where', 'Why it fits PFD', 'How to work it', 'Status / verify', 'Go?']]
    for d, t, e, w, why, how, fit, st in THIS_WEEK:
        data.append([fit, P(d), P(t), P('<b>%s</b>' % e), P(w), P(why), P(how), P(st), '[  ]'])
    tb = Table(data, repeatRows=1, colWidths=[24, 48, 58, 120, 100, 150, 140, 98, 24])
    sty = [('BACKGROUND', (0, 0), (-1, 0), NAVY), ('TEXTCOLOR', (0, 0), (-1, 0), colors.white), ('FONTSIZE', (0, 0), (-1, -1), 8),
           ('GRID', (0, 0), (-1, -1), .4, colors.grey), ('VALIGN', (0, 0), (-1, -1), 'TOP')]
    for i, row in enumerate(THIS_WEEK, 1): sty.append(('BACKGROUND', (0, i), (0, i), colors.HexColor(fitcol[row[6]])))
    tb.setStyle(TableStyle(sty))
    els += [tb, Spacer(1, 6), Paragraph('Fit: A = best (investors, advisors, angels), B = good (referral and business owners), C = low. '
                                        'Verify the date and year of any item marked A? before you go.', sm), Spacer(1, 8)]
    els += [Paragraph('<b>Event rules for PFD</b>', bd),
            Paragraph('Collect cards and ask for introductions. Do not take money or subscription documents at an event. Describe returns only as a target, never guaranteed, '
                      'and do not quote returns until counsel approves your materials. Anyone interested must be verified as accredited under 506(c) before investing. '
                      'Log every contact in the tracker (<i>crm_tracker.csv</i>) and send follow-up only to people who agree to it.', sm), Spacer(1, 8)]
    d2 = [['Date', 'Event', 'Where', 'Audience']] + [[P(a), P('<b>%s</b>' % b), P(c), P(d)] for a, b, c, d in COMING]
    t2 = Table(d2, colWidths=[90, 270, 130, 250], repeatRows=1)
    t2.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), NAVY), ('TEXTCOLOR', (0, 0), (-1, 0), colors.white), ('FONTSIZE', (0, 0), (-1, -1), 8),
                            ('GRID', (0, 0), (-1, -1), .4, colors.grey), ('VALIGN', (0, 0), (-1, -1), 'TOP')]))
    els += [Paragraph('<b>Coming up soon (from earlier research; confirm details)</b>', bd), Spacer(1, 3), t2]
    doc.build(els)
build()
