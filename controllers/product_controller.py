from flask import render_template, request
from flask_login import current_user
from service.database_service import db
from models.product import Product

def menu():
    return render_template('menu.html')

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

def products_view():
    user_products=Product.query.filter_by(user_id=current_user.id)
    return render_template('products_view.html', user_products=user_products)

