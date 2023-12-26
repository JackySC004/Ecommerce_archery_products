from flask import redirect, render_template, request
from flask_login import login_user, logout_user
from service.database_service import db

from models.user import User


def home():
    return render_template('home.html')

def login():
    if request.method == 'POST':
        email=request.form['email']
        password=request.form['password']
        user=User.query.filter_by(email=email).first()
        if user and password == user.password:
            login_user(user)
            return redirect('/menu')
    return render_template('login.html')

def register():
    if request.method == 'POST':
        name= request.form['name']
        email=request.form['email']
        password=request.form['password']
        new_user=User(name=name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
    return render_template('register.html')

def logout():
    logout_user()
    return redirect('/login')