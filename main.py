import os
from flask import Flask,render_template,request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker
from services.emailsend import sendEmail


#setting up the flask app
app = Flask(__name__)

#setting up the database
database_url = os.getenv("DATABASE_URL")
engine = create_engine(database_url)
db = scoped_session(sessionmaker(bind=engine))
print(database_url)

#flask rountes
@app.route("/")
def home_page():
    return render_template("home_page.html")

@app.route("/Track" , methods=["post"])
def track():
    username = request.form.get("name")
    user_email = request.form.get("email")
    item_link = request.form.get("item")
    
    user_data = db.execute("INSERT INTO user_prices(username,email,link) VALUES (:username, :email, :link)",
    {"username":username,"email":user_email,"link":item_link})
    db.commit()
    derrick = sendEmail(username,user_email,item_link)
    derrick.email()
    print(username)
    print(user_email)
    print(item_link)
    return render_template("success.html")

