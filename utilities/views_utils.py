import os
from flask import Flask, render_template, request, flash, redirect, session, g, jsonify
from sqlalchemy.exc import IntegrityError

from utilities.api_utils import *
from models import *

CURR_USER_KEY = "curr_user"

def do_login(user):
    """Log-in User"""
    session[CURR_USER_KEY] = user.id

def do_logout():
    """Logout User"""

    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]

def add_bill(bill_id):
    """Save bill to database"""
    bill = APIUtils.get_bill_by_id(bill_id)
   
    new_bill = Bill(
        id = bill.get("bill_id"),
        sponsor_id = bill.get("sponsor_id"),
        sponsor_name = bill.get("sponsor_name"),
        sponsor_state = bill.get("sponsor_state"),
        sponsor_party = bill.get("sponsor_party"),
        introduced_date = bill.get("introduced_date"),
        title = bill.get("title"),
        short_title = bill.get("short_title"),
        govtrack_url = bill.get("govtrack_url"),
        committees = bill.get("committees"),
        primary_subject = bill.get("primary_subject"),
        latest_major_action = bill.get("latest_major_action"),
        latest_major_action_date = bill.get("latest_major_action_date"),
    )

    db.session.add(new_bill)
    db.session.commit()

def link_bill_to_user(bill_id):
    """Link bill to user"""

    newLink = User_Bill(
        user_id = g.user.id,
        bill_id = bill_id
    )

    db.session.add(newLink)
    db.session.commit()