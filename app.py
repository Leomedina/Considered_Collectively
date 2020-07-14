import os
from flask import Flask, render_template, request, flash, redirect, session, g, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.exc import IntegrityError

from utilities.forms import AddUserForm, LoginForm, EditProfileForm, BillSearchForm
from utilities.views_utils import *
from utilities.api_utils import *
from views.auth_views import auth_BP
from views.user_views import user_BP
from views.bills_views import bills_BP
from models import *


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'TisASecret')

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','postgresql:///follow-rep')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

app.register_blueprint(auth_BP)
app.register_blueprint(user_BP)
app.register_blueprint(bills_BP)

connect_db(app);

####################################################################################

@app.before_request
def add_user_to_g():
    """If we're logged in, add curr user to Flask global."""

    if CURR_USER_KEY in session:
        g.user = User.query.get(session[CURR_USER_KEY])
    else:
        g.user = None


####################################################################################

@app.route("/", methods=["GET", "POST"])
def show_home():
    """Return home if user is logged in.
        If user is not logged in, redirect to anonymous home"""

    if g.user:
        form = BillSearchForm()
        your_bills = g.user.bills_following
        bills = 'None'
        if form.validate_on_submit():    
            query = form.search.data
            bills = APIUtils.search_bills(query).values()
        return render_template('home.html', form = form, bills = bills, your_bills = your_bills)


    bill_data = [(APIUtils.get_recent_bills().get(0)),
                    (APIUtils.get_recent_bills().get(1)),
                    (APIUtils.get_recent_bills().get(2)),
                    (APIUtils.get_recent_bills().get(3)),
                    (APIUtils.get_recent_bills().get(4)),
    ]   
    return render_template("home-anon.html", bills = bill_data)