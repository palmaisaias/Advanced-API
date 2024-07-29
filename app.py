from flask import Flask
from database import db
from models.schemas import ma
from limiter import limiter
from caching import cache

from models.customer import Customer
from models.order import Order
from models.product import Product
from models.role import Role
from models.orderItem import OrderItem

from routes.customer_routes import customer_bp
from routes.product_routes import product_bp
from routes.order_routes import order_bp
from routes.cart_routes import cart_bp

def create_app(config_name):

    app = Flask(__name__)

    app.config.from_object(f'config.{config_name}')
    db.init_app(app)
    ma.init_app(app)
    cache.init_app(app)
    # limiter.init_app(app)
    
    return app

def blueprint_config(app):
    app.register_blueprint(customer_bp, url_prefix='/customers')
    app.register_blueprint(product_bp, url_prefix='/products')
    app.register_blueprint(order_bp, url_prefix='/orders')
    app.register_blueprint(cart_bp, url_prefix='/cart')

def rate_limit_config():
    limiter.limit("200 per day")(customer_bp)

if __name__ == '__main__':
    app = create_app('Config')
    blueprint_config(app)
    rate_limit_config()

    with app.app_context():
        db.create_all()

    app.run()
