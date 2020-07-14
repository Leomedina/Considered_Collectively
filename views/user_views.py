import os
from flask import Flask, render_template, request, flash, redirect, session, g, jsonify, Blueprint
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.exc import IntegrityError

from utilities.forms import AddUserForm, LoginForm, EditProfileForm, BillSearchForm
from utilities.views_utils import *
from utilities.api_utils import *
from models import *

user_BP = Blueprint ('user_blueprint', __name__, template_folder="templates", static_folder="static");


@user_BP.route("/user", methods=["GET", "POST"])
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
