from controllers.product_controller import menu
from controllers.product_controller import add_product
from controllers.product_controller import products_view
from flask import Blueprint

blueprint_product=Blueprint('blueprint_product', __name__)

blueprint_product.route('/menu', methods=['GET', 'POST'])(menu)
blueprint_product.route('/add_product', methods=['GET', 'POST'])(add_product)
blueprint_product.route('/products_view', methods=['GET', 'POST'])(products_view)
