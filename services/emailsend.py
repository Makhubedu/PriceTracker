import smtplib #Python email library thatwas used.
import os # used for keeping the email,database and password save.
from .get_price import GamePrice #accessing the web scrapping class that have created
from email.mime.text import MIMEText

class sendEmail():
    #Initializing the method
    def __init__(self,username,user_email,link):
        self.username = username
        self.user_email = user_email
        self.link = link

    def email(self):


        #Accessing the email and the password in environment variables
        MY_EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
        MY_PASSWORD = os.getenv("MY_PASSWORD")
        scrapper = GamePrice(self.link)

        body = f"\n\nDear {self.username}\n\n\nThe price for the item you tracked has changed,\n check it out here {self.link}\nPrice Is {scrapper.get_the_price()}\nThe item name is{scrapper.get_name()}\nThank You\n\nPrice Checker"

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

            #copyright Derrick MAkhubedu
