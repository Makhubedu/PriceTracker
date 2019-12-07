from bs4 import BeautifulSoup
import requests
import re
#This is the python web scraping code that is used to get the data from game.co.za
#The code was is object oriented 
#The code gets the price and the item name
class GamePrice:

    def __init__(self,the_item_link):

        self.the_item_link = the_item_link
# Here is the method that was used to get the price
    def get_the_price(self):
        try:
            data  = self.the_item_link

            req = requests.get(data) #This line requests the web page 

            soup= BeautifulSoup(req.text ,'html.parser') # and BeautifulSoup was used to make the requested tha
                                                         # to look better

            price = soup.find(class_="pdp_price").get_text()# Here i am specifying which html element i am lookin for.
            #Here i am using regular expressions to converted the price to floating values
            price_one = re.sub(r"R","",price)
            price_two = re.sub(r",","",price_one)
            digit_price = float(price_two)

            return digit_price
        except :
            print("Something Went wrong!")

    def get_name(self):
        # Here i am just using the same steps to get the name of the item.
        data  = self.the_item_link

        req = requests.get(data)

        soup= BeautifulSoup(req.text ,'html.parser')

        title = soup.find("div",class_="name").get_text()
        print(title.strip())
        return title



