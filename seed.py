from app import app
from models import db, User, Representative, Bill, User_Rep, User_Bill

db.drop_all()
db.create_all()