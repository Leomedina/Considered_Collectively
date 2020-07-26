"""SQLAlchemy models for Follow Your Rep"""

from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from utilities.api_utils import *
from sqlalchemy import update

bcrypt = Bcrypt()
db = SQLAlchemy()

def connect_db(app):
    """Connect this database to app.py"""
    db.app = app
    db.init_app(app)


class User(db.Model):
    """USER MODEL"""

    __tablename__ = "users"

    __table_args__ = (
        db.UniqueConstraint('id', 'email', name='id_email_unique_components'),
    )

    id = db.Column(
        db.Integer,
        primary_key = True,
        autoincrement = True,
    )

    name = db.Column(
        db.String(100),
        nullable = False,
    )
    
    email = db.Column(
        db.String(50),
        unique = True,
        nullable = False,
    )

    password = db.Column(
        db.Text,
        nullable = False
    )

    profile_url = db.Column(
        db.Text,
        nullable = False,
        default="/static/images/profile_default.jpg",
    )

    reps_following = db.relationship(
        'Representative', secondary='users_reps', backref="users"
    )

    bills_following = db.relationship(
        'Bill', secondary='users_bills', backref="users"
    )

    def __repr__(self):
        first_half = f"<id: {self.id}; Name: {self.first_name};"
        second_half = f"profile_url: {self.profile_url} ; Email: {self.email}>"
        return f"{first_half} {second_half}"
    
    @classmethod
    def register(cls, email, password, name):
        """Register user and hash's the password"""

        hashed = bcrypt.generate_password_hash(password)
        hashed_utf8 = hashed.decode("utf8")

        return cls(
            email = email,
            password = hashed_utf8,
            name = name,
        )

    @classmethod
    def authenticate(cls, email, password):
        """Authenticates user"""

        user = User.query.filter_by(email = email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            return user
        else:
            return False

class Representative(db.Model):

    __tablename__ = "representatives"
    
    id = db.Column(
        db.Text,
        primary_key = True,
    )

    first_name = db.Column(
        db.Text,
    )

    last_name = db.Column(
        db.Text,
    )

    chamber = db.Column(
        db.Text,
    )

    state = db.Column(
        db.Text,
    )

    party = db.Column (
        db.Text,
    )

    twitter = db.Column(
        db.Text,
    )

    facebook = db.Column(
        db.Text,
    )

    next_election = db.Column(
        db.Text,
    )

    def __repr__(self):
        first = f"<Name: {self.first_name} {self.last_name}; Chamber: {self.chamber};"
        second =f"State: {self.state}; Party: {self.party}; Twitter: {self.twitter_link};"
        third = f"Facebook: {self.facebook}; Next Election {self.next_election}>"
        return f"{first} {second} {third}"

class Bill(db.Model):

    __tablename__ = "bills"

    id = db.Column(
        db.Text,
        primary_key = True
    )

    sponsor_id = db.Column(
        db.Text,
    )

    introduced_date = db.Column(
        db.Text,
    )

    title = db.Column(
        db.Text,
    )

    short_title = db.Column(
        db.Text,
    )

    govtrack_url = db.Column(
        db.Text,
    )

    committees = db.Column(
        db.Text,
    )

    primary_subject = db.Column(
        db.Text,
    )

    latest_major_action = db.Column(
        db.Text,
    )

    latest_major_action_date = db.Column(
        db.Text,
    )

    sponsor_name = db.Column(
        db.Text,
    )

    sponsor_state = db.Column(
        db.Text,
    )

    sponsor_party = db.Column(
        db.Text
    )

    @classmethod
    def update_all_bills(self):
        bills = Bill.query.all()
        for bill in bills:
            response = APIUtils.get_bill_by_id(bill.id)
            Bill.query.filter_by(id = bill.id).update({
                Bill.latest_major_action: response.get('latest_major_action'),
                Bill.latest_major_action_date: response.get('latest_major_action_date')
            }, synchronize_session = False)

            db.session.commit()

        return {'status':'success'}

    def __repr__(self):
        first = f"<Bill_id: {self.id}; Sponsor_id: {self.sponsor_id}>"
        return f"{first}"

class User_Rep(db.Model):
    """Mapping of a user and Representative"""

    __tablename__ = "users_reps"

    id = db.Column(
        db.Integer,
        primary_key = True,
        autoincrement = True,
    )
    
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
    )

    rep_id = db.Column(
        db.Text,
        db.ForeignKey('representatives.id')
    )

    def __repr__(self):
        return f"<User_id {self.rep_id} is following Rep_id {self.rep_id}>"

class User_Bill(db.Model):
    """Mapping of a User and a Bill"""

    __tablename__ = "users_bills"
    
    id = db.Column(
        db.Integer,
        primary_key = True,
        autoincrement = True,
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
    )

    bill_id = db.Column(
        db.Text,
        db.ForeignKey('bills.id'),
    )

    def __repr__(self):
        return f"<User_id {self.user_id} is following Bill_id: {self.bill_id}>"