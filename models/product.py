from service.database_service import db


class Product(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(60))
    img_url=db.Column(db.String(100))
    price=db.Column(db.Integer)
    description=db.Column(db.String(100))
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'))