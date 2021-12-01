from HQSmokeTests.testCases.conftest import settings

# imap host and email details
imaphost = "imap.gmail.com"
username = settings['DIMAGI_MAIL_USERNAME']

# using app password due to 2FA
app_password = settings['DIMAGI_MAIL_PASSWORD']

# details for sending the email
smtp_ssl_host = 'smtp.gmail.com'
smtp_ssl_port = 465
sender = settings['DIMAGI_MAIL_USERNAME']
targets = ['kbordoloi@dimagi.com','qa@dimagi.com']
