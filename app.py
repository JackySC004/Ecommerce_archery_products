from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_user, login_required, logout_user, current_user


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
    product=db.relationship('Product', lazy='select')

class Product(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(60))
    img_url=db.Column(db.String(100))
    price=db.Column(db.Integer)
    description=db.Column(db.String(100))
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'))


with app.app_context():
    db.create_all()

@app.route('/home', methods=['POST', 'GET'])
def home():
    return render_template('home.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        name= request.form['name']
        email=request.form['email']
        password=request.form['password']
        new_user=User(name=name, email=email, password=password)
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
            return redirect('/menu')
    return render_template('login.html')

@app.route('/menu', methods=['POST', 'GET'])
@login_required
def menu():
    return render_template('menu.html')

@app.route('/add_product', methods=['POST','GET'])
@login_required
def add_product():
    if request.method == 'POST':
        img_url=request.form['img_url']
        name=request.form['name']
        price=request.form['price']
        description=request.form['description']
        new_product=Product(img_url=img_url, name=name, price=price, description=description, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
    return render_template('add_product.html')


@app.route('/products_view', methods=['POST', 'GET'])
@login_required
def products_view():
    user_products=Product.query.filter_by(user_id=current_user.id)
    return render_template('products_view.html', user_products=user_products)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')