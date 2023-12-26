from service.database_service import db
from flask_login import UserMixin

class User(UserMixin,db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(60))
    email=db.Column(db.String(100))
    password=db.Column(db.String(100))
    product=db.relationship('Product', lazy='select')

