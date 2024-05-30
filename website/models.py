from . import db
from flask_login import UserMixin

class user(db.Model,UserMixin):
    id = db.column(db.Integer,primary_key=True)
    email = db.column(db.String(150),unique=True)
    password = db.column(db.String(150))
    