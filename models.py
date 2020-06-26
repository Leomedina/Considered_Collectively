"""SQLAlchemy models for Follow Your Rep"""

from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

bcrypt = Bcrypt()
db = SQLAlchemy()

def connect_db(app):
    """Connect this database to app.py"""
    db.app = app
    db.init_app(app)


class User(db.Model):
    """TBD"""

    __tablename__ = "users"

    id = db.Column(
        db.Integer,
        primary_key = True,
        autoincrement = True,
    )
    
    email = db.Column(
        db.String(50),
        nullable = False,
    )

    password = db.Column(
        db.Text,
        nullable = False
    )

    first_name = db.Column(
        db.String(50),
        nullable = False,
    )

    last_name = db.Column(
        db.String(50),
        nullable = False
    )

    def __repr__(self):
        first_half = f"<id: {self.id}; Name: {self.first_name}"
        second_half = f"{self.last_name}; Email: {self.email}>"
        return f"{first_half} {second_half}"
    
    @classmethod
    def register(cls, email, pwd, first_name, last_name):
        """WRITE THIS"""

        hashed = bcrypt.generate_password_hash(pwd)
        hashed_utf8 = hashed.decode("utf8")

        return cls(
            email = email,
            password = hashed_utf8,
            first_name = first_name,
            last_name = last_name,
        )

    def authenticate(cls, email, pwd):
        """WRITE THIS"""

        user = User.query.filter_by(email = email).first()
        if user and bcrypt.check_password_hash(u.password, pwd):
            return user
        else:
            return False
