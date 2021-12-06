"""
Qxf2 Services: Utility script to send pytest test report email
* Supports both text and html formatted messages
* Supports text, html, image, audio files as an attachment

To Do:
* Provide support to add multiple attachment

Note:
* We added subject, email body message as per our need. You can update that as per your requirement.
* To generate html formatted test report, you need to use pytest-html plugin. To install it use command: pip install pytest-html
* To generate pytest_report.html file use following command from the root of repo e.g. py.test --html = log/pytest_report.html
* To generate pytest_report.log file use following command from the root of repo e.g. py.test -k example_form -r F -v > log/pytest_report.log
"""
import datetime
import mimetypes
import os
import smtplib
import sys
from email import encoders
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from HQSmokeTests.utilities.email_conf import conf_file

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))



class Email_Pytest_Report:
    "Class to email pytest report"

    def __init__(self):
        self.smtp_ssl_host = conf_file.smtp_ssl_host
        self.smtp_ssl_port = conf_file.smtp_ssl_port
        # self.username = conf_file.username
        # self.password = conf_file.app_password
        self.targets = conf_file.targets
        # self.sender = conf_file.sender
        # conf_file = email_conf(self)
        # self.smtp_ssl_host = conf_file[self.smtp_ssl_host]
        # self.smtp_ssl_port = conf_file[self.smtp_ssl_port]
        # self.username = conf_file[self.username]
        # self.password = conf_file[self.app_password]
        # self.sender = conf_file[self.sender]
        # self.targets = conf_file[self.targets]

    def get_test_report_data(self,html_body_flag= True,report_file_path= 'default'):
        "get test report data from pytest_report.html or pytest_report.txt or from user provided file"
        if html_body_flag == True and report_file_path == 'default':
            #To generate pytest_report.html file use following command e.g. py.test --html = log/pytest_report.html
            test_report_file = os.path.abspath(os.path.join(os.path.dirname(__file__),'..','','report.html'))#Change report file name & address here
            print(test_report_file)
        elif html_body_flag == False and report_file_path == 'default':
            #To generate pytest_report.log file add ">pytest_report.log" at end of py.test command e.g. py.test -k example_form -r F -v > log/pytest_report.log
            test_report_file = os.path.abspath(os.path.join(os.path.dirname(__file__),'..','','pytest_report.log'))#Change report file name & address here
            print(test_report_file)
        else:
            test_report_file = report_file_path
            print(test_report_file)
        #check file exist or not
        if not os.path.exists(test_report_file):
            raise Exception("File '%s' does not exist. Please provide valid file"%test_report_file)

        with open(test_report_file, "r") as in_file:
            testdata = ""
            for line in in_file:
                testdata = testdata + '\n' + line

        return testdata


    def get_attachment(self,attachment_file_path = 'default'):
        "Get attachment and attach it to mail"
        if attachment_file_path == 'default':
            #To generate report.html file use following command e.g. py.test --html = report.html
            attachment_report_file = os.path.abspath(os.path.join(os.path.dirname(__file__),'..','','report.html'))#Change report file name & address here
            print(attachment_report_file)
        else:
            attachment_report_file = attachment_file_path
            print(attachment_report_file)
        #check file exist or not
        if not os.path.exists(attachment_report_file):
            raise Exception("File '%s' does not exist. Please provide valid file"%attachment_report_file)

        # Guess encoding type
        ctype, encoding = mimetypes.guess_type(attachment_report_file)
        if ctype is None or encoding is not None:
            ctype = 'application/octet-stream'  # Use a binary type as guess couldn't made

        maintype, subtype = ctype.split('/', 1)
        if maintype == 'text':
            fp = open(attachment_report_file)
            attachment = MIMEText(fp.read(), subtype)
            fp.close()
        elif maintype == 'image':
            fp = open(attachment_report_file, 'rb')
            attachment = MIMEImage(fp.read(), subtype)
            fp.close()
        elif maintype == 'audio':
            fp = open(attachment_report_file, 'rb')
            attachment = MIMEAudio(fp.read(), subtype)
            fp.close()
        else:
            fp = open(attachment_report_file, 'rb')
            attachment = MIMEBase(maintype, subtype)
            attachment.set_payload(fp.read())
            fp.close()
            # Encode the payload using Base64
            encoders.encode_base64(attachment)
        # Set the filename parameter
        attachment.add_header('Content-Disposition',
                   'attachment',
                   filename=os.path.basename(attachment_report_file))

        return attachment


    def send_test_report_email(self,username, password html_body_flag = True,attachment_flag = False,report_file_path = 'default'):
        "send test report email"
        #1. Get html formatted email body data from report_file_path file (log/pytest_report.html) and do not add it as an attachment
        if html_body_flag == True and attachment_flag == False:
            testdata = self.get_test_report_data(html_body_flag,report_file_path) #get html formatted test report data from log/pytest_report.html
            message = MIMEText(testdata,"html") # Add html formatted test data to email

        #2. Get text formatted email body data from report_file_path file (log/pytest_report.log) and do not add it as an attachment
        elif html_body_flag == False and attachment_flag == False:
            testdata = self.get_test_report_data(html_body_flag,report_file_path) #get html test report data from log/pytest_report.log
            message  = MIMEText(testdata) # Add text formatted test data to email

        #3. Add html formatted email body message along with an attachment file
        elif html_body_flag == True and attachment_flag == True:
            message = MIMEMultipart()
            #add html formatted body message to email
            html_body = MIMEText('''<p>Hello,</p>
                                     <p>&nbsp; &nbsp; &nbsp; &nbsp; Please check the attachment to see test built report.</p>
                                     <p><strong>Note: For best UI experience, download the attachment and open using Chrome browser.</strong></p>
                                     <p>Regards</p>
                                     <p>Dimagi QA Team</p>   
                                 ''',"html") # Add/Update email body message here as per your requirement
            message.attach(html_body)
            #add attachment to email
            attachment = self.get_attachment(report_file_path)
            message.attach(attachment)

        #4. Add text formatted email body message along with an attachment file
        else:
            message = MIMEMultipart()
            #add test formatted body message to email
            plain_text_body = MIMEText('''Hello,\n\tPlease check attachment to see test built report.
                                       \n\nNote: For best UI experience, download the attachment and open  using Chrome browser.
                                       \n\nRegards
                                       \nDimagi QA Team''')# Add/Update email body message here as per your requirement
            message.attach(plain_text_body)
            #add attachment to email
            attachment = self.get_attachment(report_file_path)
            message.attach(attachment)
        
        time_date=datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        # message['From'] = self.sender
        message['From'] = username
        message['To'] = ', '.join(self.targets)
        message['Subject'] = 'Script generated test report '+ time_date # Update email subject here

        #Send Email
        server = smtplib.SMTP_SSL(self.smtp_ssl_host, self.smtp_ssl_port)
        server.login(username, password)
        # server.login(self.username, self.password)
        # server.sendmail(self.username, self.targets, message.as_string())
        server.sendmail(username, self.targets, message.as_string())
        server.quit()
        print("email sent")

