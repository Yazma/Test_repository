# This script works with python3.6, it is not necessary to install any external libraries
# MIME is used to better organize the entire email
# To connect to email account is necessary to specify user credential: sender and sender_psw
# It is possible to send emails to different receivers, use a list, receiver, to pass all the email's address
# To create the email's body you can use text or html body, it is necessary to specify the type of body you are using
# to the body_type parameter, consider this rule: for text --> plain instead for HTML --> html
# If you want to connect to a gmail account pass to server parameter the string 'smtp.gmail.com', to connect to
# an outlook account pass 'smtp-mail.outlook.com'
# Notice that google is not allowing to log in via smtplib because it has flagged this sort of login as "less secure"
# so it's necessary to perform this steps:
# go to Manage pur google account --> Security --> Access app less secure --> set flag to on
# both for sender and receiver (if both are google account), in this way it is possible to send email from gmail account
# to every other email account
# It is possible to send attachment to the mail of the following type: word, excel, pdf, pptx, txt, csv
# No other types of attachment has been tested so it is possible that this process work also for other file's type
# The huger file tested is about 12MB, using a lot of file the process slow down in terms of execution's time
# To send attachment it is mandatory to follow those rules:
# 1) in the variable list_of_file_path_attachment add the file path to add as attachment
# 2) in the variable name_of_file_path_attachment it is necessary to add the name of the file with his extension in the
#    same order in witch they appear in the list_of_file_path_attachment
# See an example at the bottom of the script

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
COMMASPACE = ', '

class emailProcess:

    def send_mail(self,
                  sender: str,
                  sender_psw: str,
                  receiver: list,
                  subject: str,
                  body: str,
                  body_type: str,                            # specify the type of the body: text --> plain, HTML --> html
                  server: str,                               # use 'smtp.gmail.com' or 'smtp-mail.outlook.com'
                  list_of_file_path_attachment: list = None,
                  list_of_file_name_attachment: list = None
                  ):

        message = self.useMIMEMultipartToOrganizeEmail(sender, receiver, subject, body, body_type)

        if list_of_file_path_attachment is not None \
                and list_of_file_name_attachment is not None:
            len_of_list = len(list_of_file_path_attachment)
            for i in range(0, len_of_list):
                message = self.addAttachment(message,
                                             '{}'.format(list_of_file_path_attachment[i]),
                                             '{}'.format(list_of_file_name_attachment[i])
                                             )


        self.createConnection(sender, sender_psw, receiver, message, server)


    def useMIMEMultipartToOrganizeEmail(self, sender, receiver, subject,
                                        body, body_type):
        # Setup MIME, it's used to better organize the entire email
        message = MIMEMultipart()
        # Details the email
        message['From'] = sender
        message['To'] = COMMASPACE.join(receiver)
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


if __name__ == '__main__':
    emailProcess = emailProcess()
    emailProcess.send_mail(sender='your_email@eng.it',
                           sender_psw='your_password',
                           receiver=['receiver_mail1@hotmail.it', 'receiver_mail2@gmail.com'],
                           subject='Titolo della Mail',
                           body='Corpo della mail',
                           body_type='plain',  # Due we use a text body is necessary to use plain as body type
                           server='smtp-mail.outlook.com',  # string for outlook account
                           list_of_file_path_attachment=['your_path/word_file_name.odt',
                                                         'your_path/excel_file_name.xlsx',
                                                         'your_path/pdf_file_name.pdf',
                                                         'your_path/power_point_file_name.pptx',
                                                         'your_path/csv_file_name.csv',
                                                         'your_path/text_file_name.txt'],
                           list_of_file_name_attachment=['word_file_name.odt',
                                                         'excel_file_name.xlsx',
                                                         'pdf_file_name.pdf',
                                                         'power_point_file_name.pptx',
                                                         'csv_file_name.csv',
                                                         'text_file_name.txt']
                           )
