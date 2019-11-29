from bs4 import BeautifulSoup
import requests
import re
class GamePrice:

    def __init__(self,the_item_link):

        self.the_item_link = the_item_link

    def get_the_price(self):
        try:
            data  = self.the_item_link

            req = requests.get(data)

            soup= BeautifulSoup(req.text ,'html.parser')

            price = soup.find(class_="pdp_price").get_text()

            price_one = re.sub(r"R","",price)
            price_two = re.sub(r",","",price_one)
            digit_price = float(price_two)
            print(digit_price)

            return digit_price


            
           
        except :
            print("Something Went wrong!")

    def get_name(self):
        data  = self.the_item_link

        req = requests.get(data)

        soup= BeautifulSoup(req.text ,'html.parser')

        title = soup.find("div",class_="name").get_text()
        print(title.strip())
        return title


if __name__=="__main__":
    my_price = GamePrice("https://www.game.co.za/game-za/en/All-Game-Categories/Electronics-%26-Entertainment/Television-%26-Satellite/TVs/Hisense-55%22-ULED-TV/p/00800860")
    my_price.get_the_price()
    my_price.get_name()

