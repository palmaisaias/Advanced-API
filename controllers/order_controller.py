from flask import request, jsonify
from services import order_service
from models.schemas.order_schema import order_schema, orders_schema
from models.schemas.product_schema import products_schema
from models.order import Order
from database import db
from sqlalchemy import select
from marshmallow import ValidationError
from utils.util import user_token_required, admin_required

def save_order():
    try:
        order_data = order_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    new_order = order_service.save_order(order_data)
    return jsonify({"id": new_order.id, "Message": "It's on the way!"}), 201

@user_token_required
def get_order_items(id, token_id):
    if id  == token_id:
        query = select(Order).filter(Order.id == id)
        order = db.session.execute(query).scalar()

        if order is None:
            return jsonify({"error": "You aint got no orders and therefore...no items"}), 404
    else:
        return jsonify({"messages": "Not your order, not YOUR items"}), 401
    return products_schema.jsonify(order.products)

@admin_required
def find_all_orders():
    orders = order_service.find_all_orders()
    return orders_schema.jsonify(orders), 200

def find_all_paginate():
    page = int(request.args.get("page"))
    per_page = int(request.args.get("per_page"))
    orders = order_service.find_all_paginate(page, per_page)
    return orders_schema.jsonify(orders), 200
