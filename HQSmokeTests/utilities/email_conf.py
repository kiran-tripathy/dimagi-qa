# imap host and email details
imaphost = "imap.gmail.com"
username = ${{secrets.DIMAGI_MAIL_USERNAME}}

# using app password due to 2FA
app_password = ${{secrets.DIMAGI_MAIL_PASSWORD}}

# details for sending the email
smtp_ssl_host = 'smtp.gmail.com'
smtp_ssl_port = 465
sender = ${{secrets.DIMAGI_MAIL_USERNAME}}
targets = ['kbordoloi@dimagi.com','qa@dimagi.com']
