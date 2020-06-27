from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import *


app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECT'] = False

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///follow-rep'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

debug = DebugToolbarExtension(app)

connect_db(app);

@app.route("/")
def show_home():
    return render_template("home.html")