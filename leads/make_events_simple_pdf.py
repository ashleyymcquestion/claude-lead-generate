"""One-page printable list: this week's OC events with date, time, price."""
from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer

ss = getSampleStyleSheet()
sm = ParagraphStyle('sm', parent=ss['BodyText'], fontSize=8.5, leading=10.5)
NAVY = colors.HexColor('#1F3864')
P = lambda t: Paragraph(t, sm)
NL = 'Not listed (check organizer)'
ROWS = [  # date, time, event, where, price, link, note
 ('Tue Oct 6', '10:00 AM (6 Tuesdays to Nov 10)', 'Free Business Accelerator Program', 'Orange County (location not listed)', 'FREE', 'https://www.eventbrite.com/d/ca--irvine/networking-events/', 'Find it on the Irvine Eventbrite list'),
 ('Tue Oct 6', '7:00 AM', 'BNI Go Givers (hybrid referral chapter)', 'Hybrid (online + in person)', NL, 'https://www.eventbrite.com/d/ca--irvine/networking-events/', 'Find it on the Irvine Eventbrite list'),
 ('Wed Oct 7', 'Evening (a past Sept 2 event ran 7-9 PM)', 'Orange County Tech & Finance Networking Event', 'Mesa, Costa Mesa (past event venue; Oct 7 venue not confirmed)', NL, 'https://happeningnext.com/event/orange-county-tech-andamp-finance-networking-event-eid1ef0l3gq03fr', 'Link is the Sept 2 event; check for the Oct 7 listing'),
 ('Wed Oct 7', '6:30 PM', 'Cybersecurity for Everyone', 'Orange County (location not listed)', NL, 'https://allevents.in/irvine/business', 'Search the Irvine business events list'),
 ('Wed Oct 7', '6:00 PM (usual start)', 'Tech Link Up After Hours', 'Hangar 24, 17877 Von Karman Ave, Irvine', NL, 'https://www.meetup.com/oc-tech-link-up/', 'Meetup group page'),
 ('Thu Oct 8', '7:00 AM (older listing; one said 6:45)', 'OC PRO Networkers: Business Referral Networking Breakfast', 'Laguna Hills (per older listing)', '$15 (older listing)', 'https://www.ocpronet.com', 'Phone (949) 278-3048; confirm location and time'),
 ('Thu Oct 8', '5:00 PM', 'HUSTLE Orange County Entrepreneur Networking', 'Wild Goose Tavern (Newport Beach per listing; the tavern is also listed in Costa Mesa)', NL, 'https://allevents.in/newport-beach/business', 'Not found beyond the listing; UNVERIFIED'),
 ('Thu Oct 8', '5:30 PM check-in; 6:30-9:30 PM', 'OCREIA monthly real estate investor meeting (2nd Thursday)', 'Avenue of the Arts Hotel, 3350 Ave of the Arts, Costa Mesa, or Zoom', NL, 'https://meetup.com/orange-county-real-estate-investors-association-ocreia', 'Also ocreia.com or 866-200-1435'),
 ('Thu Oct 8', '7:00-10:00 PM (monthly meetup; Oct date unconfirmed)', 'Property Deal Network: free real estate investor meetup', 'Wild Goose Tavern, Costa Mesa', 'FREE', 'https://www.skiddle.com/whats-on/united-states/Wild-Goose-Tavern/Real-Estate-Networking-Orange-County--Property-Deal-Network/42780969/', 'No presentations; ages 25+'),
 ('Thu Oct 8', 'Time not listed', 'AI Leadership: 5 Fundamentals', 'Orange County (location not listed)', NL, 'https://allevents.in/irvine/business', 'Search the Irvine business events list'),
 ('Thu Oct 8', '5:30-8:30 PM', 'Tech Coast Angels OC Entrepreneur Mixer (UNVERIFIED YEAR)', 'ROC building, 4590 MacArthur Blvd, 3rd floor, Newport Beach', NL, 'https://tcaventuregroup.com/tech-coast-angels-is-hosting-the-oc-entrepreneur-mixer/', 'Page may be from a past year'),
 ('Fri Oct 9', '10:00 AM', 'BT Legacy Acct: Private Tax Strategy Intensive', 'VEA Newport Beach, a Marriott Resort & Spa', NL, 'https://allevents.in/newport-beach/business', 'No event page found; UNVERIFIED'),
]
TYPES = [('OCREIA', 'Event/group page'), ('Tech Link Up', 'Event/group page'), ('Tech Coast Angels', 'Event page (year unverified)'),
         ('OC PRO', 'Group site'), ('Property Deal', 'Event page'), ('Tech & Finance', 'Past event only (Sept 2)'),
         ('HUSTLE', 'No event page found'), ('BT Legacy', 'No event page found')]
def ltype(name):
    return next((t for k, t in TYPES if k in name), 'Listing page only')

doc = SimpleDocTemplate('PFD_Events_This_Week_List.pdf', pagesize=landscape(letter), leftMargin=28, rightMargin=28, topMargin=36, bottomMargin=36,
                        title='Orange County Events - Week of Oct 5, 2026')
els = [Paragraph('Orange County Events: Week of Oct 5-11, 2026', ParagraphStyle('t', parent=ss['Title'], fontSize=18, textColor=NAVY)),
       Paragraph('<b>Confirm before you go.</b> Event sites were blocked, so these come from search-result listings. Prices not shown in the listing are marked '
                 '"Not listed". Links go to the best page I found for each event, which is sometimes a listing page rather than the event itself. The Tech Coast Angels date may be from a past year.', sm), Spacer(1, 8)]
link = lambda u: '<a href="%s" color="blue">%s</a>' % (u, u.replace('https://', '').replace('www.', '')[:48])
data = [['Date', 'Time', 'Event', 'Where', 'Price', 'Link', 'Link type', 'Notes']] + [[P(a), P(b), P('<b>%s</b>' % c), P(d), P(e), P(link(f)), P(ltype(c)), P(g)] for a, b, c, d, e, f, g in ROWS]
t = Table(data, repeatRows=1, colWidths=[44, 78, 120, 130, 50, 130, 62, 122])
t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), NAVY), ('TEXTCOLOR', (0, 0), (-1, 0), colors.white), ('FONTSIZE', (0, 0), (-1, -1), 8.5),
                       ('GRID', (0, 0), (-1, -1), .4, colors.grey), ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                       ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F2F2F2')])]))
els.append(t)
els += [Spacer(1, 10), Paragraph('<b>What I found and what is still unconfirmed</b>', ParagraphStyle('h', parent=sm, fontSize=10, textColor=NAVY)), Spacer(1, 3)]
NOTES = [
 '<b>Specific pages found:</b> OCREIA (Meetup page; Avenue of the Arts Hotel, Costa Mesa; ocreia.com or 866-200-1435). Tech Link Up (Meetup group; Hangar 24, 17877 Von Karman Ave, Irvine; usually 6:00 PM). '
 'Tech Coast Angels mixer (4590 MacArthur Blvd, 3rd floor, Newport Beach; the page may be from a past year). OC PRO Networkers (ocpronet.com, (949) 278-3048; older listing: Laguna Hills, Thursdays 7 AM, $15). '
 'Free real estate investor meetup = Property Deal Network, Wild Goose Tavern, Costa Mesa, 7-10 PM, free, no presentations, ages 25+; the Oct 8 date is not confirmed.',
 '<b>Listing pages only:</b> Business Accelerator, BNI Go Givers, Cybersecurity for Everyone and AI Leadership link to general Irvine Eventbrite or Irvine business-events lists. Search those lists for the event.',
 '<b>Problems:</b> No event page was found for HUSTLE Orange County (search results were UK cities) or the BT Legacy Private Tax Strategy Intensive; both are UNVERIFIED. '
 'For Tech &amp; Finance Networking, the only page found was a Sept 2 event at Mesa in Costa Mesa, 7-9 PM; an Oct 7 event was not confirmed.',
 '<b>Before you go:</b> verify each date, time and price on the organizer\'s page.']
for n in NOTES: els += [Paragraph(n, sm), Spacer(1, 4)]
doc.build(els)
