from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_user, login_required, logout_user


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'
app.config['SECRET_KEY']='stopuncle'
db=SQLAlchemy(app)

login_manager=LoginManager()
login_manager.init_app(app)
login_manager.login_view='login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(60))
    email=db.Column(db.String(100))
    password=db.Column(db.String(100))

with app.app_context():
    db.create_all()

@app.route('/menu', methods=['POST', 'GET'])
def menu():
    return render_template('menu.html')

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


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email=request.form['email']
        password=request.form['password']
        user=User.query.filter_by(email=email).first()
        if user and password == user.password:
            login_user(user)
            return redirect('/products_view')
    return render_template('login.html')


@app.route('/products_view', methods=['POST', 'GET'])
@login_required
def products_view():
    return render_template('products_view.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')