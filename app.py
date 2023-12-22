from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'
app.config['SECRET_KEY']='stopuncle'
db=SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(60))
    email=db.Column(db.String(100))
    password=db.Column(db.String(100))

with app.app_context():
    db.create_all()


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        name= request.form['name']
        email=request.form['email']
        password=request.form['password']
        new_user=User(name=name, email=email,password=password)
        db.session.add(new_user)
        db.session.commit()


    return render_template('register.html')
