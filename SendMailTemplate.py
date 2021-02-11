'''All the necessary libraryes'''
import smtplib
import pandas as pd
import os

'''This library permits to better organize body, cc and others of the email'''
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email import encoders

class sendMail():

    def send_mail(self,
                  sender: str,
                  sender_psw: str,
                  receiver: list,
                  subject: str,
                  body: str,
                  ):

        return sender

    def useMIMEMultipartToOrganizeEmail(self, sender_address, receiver_address, cc_address, subject,
                                        body, body_type):
        # Setup MIME, it's used to better organize the entire email
        message = MIMEMultipart()

        # Details the email
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Cc'] = cc_address
        message['Subject'] = subject

        # Add body of the email, use body_type to specify the type of the body:
        #       text --> plain
        #       HTML --> html
        email_body = MIMEText(body, body_type)
        message.attach(email_body)

        return message




