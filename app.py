from flask import Flask

from routes.user_route import blueprint_user
from routes.product_route import blueprint_product
from flask_login import LoginManager
from service.database_service import db
from models.user import User

def create_app():
    app= Flask(__name__)
    app.config.from_object('config')
    db.init_app(app)
    return app

app=create_app()
app.register_blueprint(blueprint_user)
app.register_blueprint(blueprint_product)


login_manager=LoginManager()
login_manager.init_app(app)
login_manager.login_view='login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)