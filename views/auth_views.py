import os
from flask import Flask, render_template, request, flash, redirect, session, g, jsonify, Blueprint
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.exc import IntegrityError

from utilities.forms import AddUserForm, LoginForm, EditProfileForm, BillSearchForm
from utilities.views_utils import *
from utilities.api_utils import *
from models import *

auth_BP = Blueprint ('auth_blueprint', __name__, template_folder="templates", static_folder="static");

@auth_BP.route("/register", methods=["GET", "POST"])
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

@auth_BP.route("/login", methods = ["GET","POST"])
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

@auth_BP.route("/logout")
def logout():
    """Handle Logout functionality"""
    do_logout()
    return redirect("/")