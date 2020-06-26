from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"
app.config["DEBUG_TB_INTERCEPT_REDIRECT"] = False

#TODO: Databases#

@app.route("/")
def show_home():
    return render_template("home.html")