import smtplib
import os
from email.mime.text import MIMEText
class sendEmail():
    def __init__(self,username,user_email,link):
        self.username = username
        self.user_email = user_email
        self.link = link

    def email(self):


        #Accessing the email and the password in environment variables
        MY_EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
        MY_PASSWORD = os.getenv("MY_PASSWORD")

        body = f"\n\nDear {self.username} \n\n\nThe Item that you tracked has changed price ,\n check it out here {self.link}\n\nThank You\n\nPrice Checker"

        # Setting up the email text
        msg = MIMEText(body)
        msg['From'] = MY_EMAIL_ADDRESS
        msg ['To'] = self.user_email
        msg['Subject'] = "Price Track"
    
        #Specifying Which email i am sending to and fro
        send_from = MY_EMAIL_ADDRESS
        to = self.user_email

        #Checking if there is no error before sending the email
        try:

            server  = smtplib.SMTP_SSL('smtp.gmail.com',465) #specifying the server
            server.ehlo()
            server.login(MY_EMAIL_ADDRESS,MY_PASSWORD)
            server.sendmail(send_from,to,msg.as_string())
            server.close()
            print("Email Has Been Send!!")
        except:
            print("Something Went Wrong")

