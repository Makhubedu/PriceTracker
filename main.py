import os
from flask import Flask,render_template,request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker
from services.get_price import GamePrice

# The flask framework was used to the application
# POSTGRES SQL was used as the DBMS of choice
#SQLALCHEMY is used to make working with database with python easy
#And the sessions are used here. Session are important because every user can have a deffirent experice on the same app


#setting up the flask app
app = Flask(__name__)


#setting up the database
database_url = os.getenv("DATABASE_URL")
engine = create_engine(database_url)
db = scoped_session(sessionmaker(bind=engine))

#flask rountes
@app.route("/")
def home_page():
    return render_template("home_page.html")
#This is a post request, Instead of getting web page you are getting some data.
@app.route("/Track" , methods=["post"])
def track():
    # Here i am just accessing the data form the form
    username = request.form.get("name")
    user_email = request.form.get("email")
    item_link = request.form.get("item")
# I am calling the get get price class here in order to use get_price method
    find_price = GamePrice(item_link)
    price = find_price.get_the_price()
# The following code will be and extensive error handling.
    if price == None: 
        # since i am able to get the price, if the price is nothing it means the user put in a wrong email
        # The following they go to the ginger AKA html, and this is similar to all .
        title = "Wrong Link"
        sorry = "Sorry"
        heading = "Wrong Link"
        link = "https://photos.google.com/search/_tra_/photo/AF1QipOXEmdL1K991WPagHJ64ewdJmuIZ64KIr_LUlDE"
        message = "You forgot to Enter the link, Please go back and Enter The Correct one."
        return render_template("wrong_link.html",message=message,heading=heading,sorry=sorry,title=title,link=link)
    elif item_link[:54] != "https://www.game.co.za/game-za/en/All-Game-Categories/":
        title = "Wrong Link"
        sorry = "Sorry"
        heading = "Wrong Link"
        link = "https://photos.google.com/search/_tra_/photo/AF1QipOXEmdL1K991WPagHJ64ewdJmuIZ64KIr_LUlDE"
        message = "You Enter a wrong link, Please go back and Enter The Correct one."
        return render_template("wrong_link.html",message=message,heading=heading,sorry=sorry,title=title,link=link)
    elif username == "":
        title = "No User Name"
        heading = "Oops!!"
        message = "You Forgot to Enter Your Name, Please go back and Enter It."
        sorry = "Sorry"
        link = "https://www.pngtube.com/myfile/full/59-592368_confused-emoji-disappointed-emoji.png"
        return render_template("error_layout.html",message=message,heading=heading,sorry=sorry,title=title,link=link)
    elif user_email == "":
        title = "No Email"
        heading = "Oops!"
        message = "You Forgot to Enter Your Email, Please go back and Enter It."
        sorry = "Sorry"
        link = "https://www.pngtube.com/myfile/full/59-592368_confused-emoji-disappointed-emoji.png"
        return render_template("error_layout.html",message=message,heading=heading,sorry=sorry,title=title,link=link)
    elif item_link == "":
        message= "You Enter a wrong link, Please go back and Enter The Correct one."
        sorry = "Sorry"
        title = "No Link"
        heading = "Oops!!"
        link = "https://www.pngtube.com/myfile/full/59-592368_confused-emoji-disappointed-emoji.png"
        
        return render_template("error_layout.html",message=message,heading=heading,sorry=sorry,title=title,link=link)

# Now that i am done handling the small exceptions. I am going for the database
    try :

        database_email = db.execute("SELECT email FROM user_prices").fetchall() #Here i am selecting everything in the database
        for current_email in database_email:
            for actual_email in current_email:
                if actual_email == user_email:
                    return render_template("temp.html") #Here is when the email already exists. Instead of throwing 
                    #database error i wil l return error page
                    # Since this has time complexity of O(N^2) i have to make it better when io have time.
    #Here i am inserting the data into the database, But i will use python context management once i am good with them
        user_data = db.execute("INSERT INTO user_prices(username,email,link) VALUES (:username, :email, :link)",
        {"username":username,"email":user_email,"link":item_link})
        db.commit()
        
    except :
        
        return render_template("something_is_wrong.html")
    #Hamdling errors before sending email, to avoid the websitre crashing
    try :
        derrick = sendEmail(username,user_email,item_link)
        derrick.email()
    except :
        return render_template("something_is_wrong.html")
    
# You willl only get here if all thing are well. :)
    return render_template("success.html",name=username,email=user_email)

if __name__=="__main__":
    app.run()
#copyright Derrick MAkhubedu