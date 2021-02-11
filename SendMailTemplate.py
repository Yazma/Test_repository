'''All the necessary libraryes'''

# Notice that google is not allowing to log in via smtplib because it has flagged this sort of login as
# "less secure" so it's necessary to perform this steps:
# go to Manage pur google account --> Security --> Access app less secure --> set flag to on
# both for sender and receiver (if both are google account)
# with this method it's possible to sent email from gmail account to every other email account

import smtplib
import pandas as pd
import os

'''This library permits to better organize body, cc and others of the email'''
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email import encoders

class emailProcess:

    def send_mail(self,
                  sender: str,
                  sender_psw: str,
                  receiver: list,
                  subject: str,
                  body: str,
                  body_type: str,                # specify the type of the body: text --> plain, HTML --> html
                  word_file_path: str = None,
                  word_file_name: str = None,
                  excel_file_path: str = None,
                  excel_file_name: str = None,
                  pdf_file_path: str = None,
                  pdf_file_name: str = None,
                  connect_to_server: str = None,  # use 'smtp.gmail.com' or 'smtp-mail.outlook.com'
                  ):




        return sender

    def useMIMEMultipartToOrganizeEmail(self, sender, receiver, subject,
                                        body, body_type):
        # Setup MIME, it's used to better organize the entire email
        message = MIMEMultipart()
        # Details the email
        message['From'] = sender
        message['To'] = receiver
        message['Subject'] = subject
        email_body = MIMEText(body, body_type)
        message.attach(email_body)
        return message


    def addAttachment(self, message, path, file_name):
        # Open file in binary mode
        open_file_as_binary = open(path, "rb")
        # Use MIMEBase with ('application','octet-stream') that lets to attach all files in a binary mode
        attach_loader = MIMEBase('application', 'octet-stream')
        # Read the file
        attach_loader.set_payload(open_file_as_binary.read())
        # Encode the file in base 64
        encoders.encode_base64(attach_loader)
        # Attach file
        attach_loader.add_header('Content-Disposition', 'attachment; filename="{}"'.format(file_name))
        # Add the attachment to the email
        message.attach(attach_loader)
        return message


    def createConnection(self, sender, sender_psw, receiver, message, server):
        # Create SMTP session for sending the mail
        try:
            session = smtplib.SMTP('{}'.format(server))
            session.starttls()  # enable security
            session.login(sender, sender_psw)  # login with mail_id and password
            body = message.as_string()
            session.sendmail(sender, receiver, body)
            session.close()
            print('Success sending from', sender, 'to', receiver)
        except Exception as e:
            print('Error during connection to outlook account')
            print(e)