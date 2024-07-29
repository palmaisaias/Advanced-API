from flask import request, jsonify
from services import order_service
from models.schemas.order_schema import order_schema, orders_schema
from models.schemas.product_schema import products_schema
from models.order import Order
from database import db
from sqlalchemy import select
from marshmallow import ValidationError
from utils.util import user_token_required, admin_required

@user_token_required
def place_order(customer_id, token_id):
    if customer_id != token_id:
        return jsonify({"message": "Token does not match customer ID"}), 401

    try:
        new_order = order_service.save_order_from_cart(customer_id)
    except ValueError as e:
        return jsonify({"message": str(e)}), 404

    return jsonify({"id": new_order.id, "message": "Order placed successfully!"}), 201

@user_token_required
def get_order(id, token_id):
    order = order_service.find_order_by_id(id)
    if order is None:
        return jsonify({"error": "Order not found"}), 404

    if order.customer_id != token_id:
        return jsonify({"message": "Not your order"}), 401

    return order_schema.jsonify(order)

@admin_required
def find_all_orders():
    orders = order_service.find_all_orders()
    return orders_schema.jsonify(orders), 200

def find_all_paginate():
    page = int(request.args.get("page"))
    per_page = int(request.args.get("per_page"))
    orders = order_service.find_all_paginate(page, per_page)
    return orders_schema.jsonify(orders), 200
