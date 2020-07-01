from flask import Flask, render_template, request, flash, redirect, session, g, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.exc import IntegrityError

from models import *
from forms import *
from utilities import *

CURR_USER_KEY = "curr_user"

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///follow-rep'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app);

####################################################################################
# User Register/Login/Logout

@app.before_request
def add_user_to_g():
    """If we're logged in, add curr user to Flask global."""

    if CURR_USER_KEY in session:
        g.user = User.query.get(session[CURR_USER_KEY])
    else:
        g.user = None

def do_login(user):
    """Log-in User"""
    session[CURR_USER_KEY] = user.id

def do_logout():
    """Logout User"""

    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]

@app.route("/register", methods=["GET", "POST"])
def register():

    if g.user:
        return render_template('home.html')
    
    form = AddUserForm()

    if form.validate_on_submit():
        try:
            user = User.register(
                email = form.email.data,
                password = form.password.data,
                name = form.name.data,
            )

            db.session.add(user)
            db.session.commit()
            do_login(user)
            return redirect("/")
            
        except IntegrityError:
            flash("Email already taken", "danger")
            return redirect("/")
    
    return render_template("user/register.html", form = form)

@app.route("/login", methods = ["GET","POST"])
def login():
    """handle user login"""
    if g.user:
        return redirect('/')

    form = LoginForm()

    if form.validate_on_submit():
        user = User.authenticate(form.email.data,
                                 form.password.data)
        if user:
            do_login(user)
        else:
            flash("Invalid credentials.", 'danger')
        return redirect("/login")

    return render_template("/user/login.html", form = form)

@app.route("/logout")
def logout():
    """Handle Logout functionality"""
    do_logout()
    return redirect("/")

####################################################################################

@app.route("/", methods=["GET", "POST"])
def show_home():
    """Return home if user is logged in.
        If user is not logged in, redirect to anonymous home"""

    if g.user:
        form = BillSearchForm()

        bills = 'None'
        if form.validate_on_submit():    
            query = form.search.data
            bills = APIUtils.search_bills(query).values()
        return render_template('home.html', form = form, bills = bills)


    bill_data = [(APIUtils.get_recent_bills().get(0)),
                    (APIUtils.get_recent_bills().get(1)),
                    (APIUtils.get_recent_bills().get(2)),
                    (APIUtils.get_recent_bills().get(3)),
                    (APIUtils.get_recent_bills().get(4)),
    ]   
    return render_template("home-anon.html", bills = bill_data)


@app.route("/user", methods=["GET", "POST"])
def user():
    if not g.user:
        flash("Must be logged in to view page", "danger")
        return redirect("/")
    
    form = EditProfileForm(obj = g.user)

    if form.validate_on_submit():
        if not User.authenticate(g.user.email, form.password.data):
            flash("Wrong Password", "danger")
            return redirect("/")

        user = User.query.get_or_404(g.user.id)
        user.email = form.email.data
        user.name = form.name.data
        # user.profile_url = form.profile_url.data

        db.session.add(user)
        db.session.commit()
        
        flash("Profile Updated!", "success")
        return redirect('/')
    return render_template("/user/edit_user.html", form = form )

####################################################################################

@app.route("/bills")
def recent_bills():
    bill_data = APIUtils.get_recent_bills();

    return jsonify(bill_data)

@app.route("/bills_search")
def search_bills():
    query = "health care"
    bill_search = APIUtils.search_bills(query)

    return jsonify(bill_search)

@app.route("/search", methods=["GET", "POST"])
def search_page():
    if not g.user:
        flash("Must be logged in to view page", "warning")
        return redirect("/")

    form = BillSearchForm()
    bills = 'None'
    if form.validate_on_submit():    
        query = form.search.data
        bills = APIUtils.search_bills(query).values()
        return render_template('user/explore.html', form = form, bills = bills)

    return render_template('user/explore.html', form = form)