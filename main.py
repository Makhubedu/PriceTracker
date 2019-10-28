import os
from flask import Flask,render_template,request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker

#setting up the flask app
app = Flask(__name__)

#setting up the database
#database_url = os.getenv("DATABSE_URL")
#engine = create_engine(database_url)
#db = scoped_session(sessionmaker(bind=engine))

#flask rountes
@app.route("/")

def home_page():
    return render_template("home_page.html")

@app.route("/Track" , methods=["post"])
def track():
    return ("hey Your here Now !!")

