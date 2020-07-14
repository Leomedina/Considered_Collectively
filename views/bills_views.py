import os
from flask import Flask, render_template, request, flash, redirect, session, g, jsonify, Blueprint
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.exc import IntegrityError

from utilities.forms import AddUserForm, LoginForm, EditProfileForm, BillSearchForm
from utilities.views_utils import *
from utilities.api_utils import *
from models import *

bills_BP = Blueprint ('bills_blueprint', __name__, template_folder="templates", static_folder="static");


@bills_BP.route("/bills_search/<bill_id>")
def search_bills(bill_id):
    query = "health care"
    bill_search = APIUtils.get_bill_by_id(bill_id)

    return jsonify(bill_search)

@bills_BP.route("/search", methods=["GET", "POST"])
def search_page():
    form = BillSearchForm()
    bills = 'None'

    if form.validate_on_submit():    
        query = form.search.data
        bills = APIUtils.search_bills(query).values()
        return render_template('user/explore.html', form = form, bills = bills)

    return render_template('user/explore.html', form = form)

@bills_BP.route("/bill/<bill_id>", methods=["POST"])
def add_bill_to_user(bill_id):
    if not g.user:
        flash("Sign up to save bills!", "warning")
        return redirect("/register")

    add_bill(bill_id)
    link_bill_to_user(bill_id)

    return redirect('/')