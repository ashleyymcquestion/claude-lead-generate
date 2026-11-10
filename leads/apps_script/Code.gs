/**
 * PFD lead capture: receives landing-page form posts and writes them to this Google Sheet.
 * Setup steps are in leads/SETUP_lead_capture.md.
 */
var NOTIFY_EMAIL = '';      // optional: your email for "new lead" alerts (no personal data is put in the alert)
var SHEET_ID = '';          // leave blank if this script is attached to the Sheet (Extensions > Apps Script)

var LEAD_HEADERS = ['id', 'source', 'type', 'name', 'firm', 'email', 'phone', 'stage', 'accredited_verified',
  'verification_method', 'date_first_contact', 'last_contact', 'next_action', 'next_action_date',
  'consent_to_contact', 'dnc_checked', 'notes',
  'assets_range', 'self_certified_accredited', 'submitted_at', 'utm_source', 'utm_medium', 'utm_campaign',
  'utm_term', 'utm_content', 'page_url', 'referrer', 'consent_text_version'];
var RAW_HEADERS = ['submitted_at', 'status', 'email', 'payload_json'];

function ss_() { return SHEET_ID ? SpreadsheetApp.openById(SHEET_ID) : SpreadsheetApp.getActiveSpreadsheet(); }

function sheet_(name, headers) {
  var ss = ss_(), sh = ss.getSheetByName(name);
  if (!sh) { sh = ss.insertSheet(name); }
  if (sh.getLastRow() === 0) {
    sh.appendRow(headers); sh.setFrozenRows(1);
    sh.getRange(1, 1, 1, headers.length).setFontWeight('bold');
  }
  return sh;
}

/** Run once from the editor to create the two tabs. */
function setup() { sheet_('Leads', LEAD_HEADERS); sheet_('Raw Submissions', RAW_HEADERS); }

function doGet() {
  return ContentService.createTextOutput('PFD lead capture is running.');
}

function doPost(e) {
  var p = (e && e.parameter) || {};
  var now = new Date();
  var stamp = Utilities.formatDate(now, 'America/Los_Angeles', "yyyy-MM-dd'T'HH:mm:ss");
  var raw = sheet_('Raw Submissions', RAW_HEADERS);
  var email = String(p.email || '').trim().toLowerCase();
  var phone = String(p.phone || '').trim();
  var name = String(p.name || '').trim();

  // reject bots (hidden field), bad emails, and missing consent/certification
  var status = 'ok';
  if (p.website) status = 'rejected: honeypot';
  else if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) status = 'rejected: bad email';
  else if (!name || phone.replace(/\D/g, '').length < 10) status = 'rejected: missing name/phone';
  else if (p.consent !== 'on' || p.accredited !== 'on') status = 'rejected: missing consent or certification';

  var lock = LockService.getScriptLock();
  lock.waitLock(20000);
  try {
    if (status === 'ok') {
      var leads = sheet_('Leads', LEAD_HEADERS);
      var emails = leads.getLastRow() > 1 ? leads.getRange(2, 6, leads.getLastRow() - 1, 1).getValues() : [];
      var dupRow = -1;
      for (var i = 0; i < emails.length; i++) {
        if (String(emails[i][0]).toLowerCase() === email) { dupRow = i + 2; break; }
      }
      if (dupRow > 0) {
        var notesCell = leads.getRange(dupRow, 17);
        notesCell.setValue((notesCell.getValue() + ' | Resubmitted form ' + stamp).replace(/^ \| /, ''));
        leads.getRange(dupRow, 12).setValue(stamp.substring(0, 10));
        status = 'duplicate (existing row ' + dupRow + ')';
      } else {
        var id = 'WEB-' + Utilities.formatDate(now, 'America/Los_Angeles', 'yyMMdd-HHmmss');
        leads.appendRow([id, 'Landing page' + (p.utm_source ? ' / ' + p.utm_source : ''), 'investor', name, '', email, phone,
          'New Lead', 'No (self-certified only; verify before sending materials)', '', stamp.substring(0, 10), stamp.substring(0, 10),
          'Review; call or email within 1 business day; no return figures; verify accredited status first', '',
          'Yes (web form checkbox; ' + stamp + ')', 'No (scrub phone against DNC before calling)', '',
          p.assets || '', 'Yes', stamp, p.utm_source || '', p.utm_medium || '', p.utm_campaign || '', p.utm_term || '',
          p.utm_content || '', p.page_url || '', p.referrer || '', p.consent_text_version || '']);
        if (NOTIFY_EMAIL) {
          MailApp.sendEmail(NOTIFY_EMAIL, 'New PFD web lead ' + id, 'A new lead was added to the Leads sheet: ' + ss_().getUrl());
        }
      }
    }
    raw.appendRow([stamp, status, email, JSON.stringify(p)]);
  } finally { lock.releaseLock(); }
  return ContentService.createTextOutput(JSON.stringify({ ok: status.indexOf('rejected') !== 0 }))
    .setMimeType(ContentService.MimeType.JSON);
}
