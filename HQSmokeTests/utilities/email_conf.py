def email_conf(settings):
    email_dict = {
        "imaphost" : "imap.gmail.com",
        "username": settings["login_username"],
        "app_password": settings["login_password"],
        "smtp_ssl_host" : "smtp.gmail.com",
        "smtp_ssl_port" : "465",
        "sender" : settings["login_username"],
        "targets" : ['kbordoloi@dimagi.com']
    }
    return (email_dict)

# # imap host and email details
# imaphost = "imap.gmail.com"
# username = "kbordoloi@dimagi.com"
#
# # using app password due to 2FA
# app_password = "ydfxtggbtggodgrn"
#
# # details for sending the email
# smtp_ssl_host = 'smtp.gmail.com'
# smtp_ssl_port = 465
# sender = "kbordoloi@dimagi.com"
# targets = ['kbordoloi@dimagi.com','qa@dimagi.com']
