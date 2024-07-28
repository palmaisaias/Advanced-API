from flask import request, jsonify
from models.schemas.cart_item_schema import cart_item_schema
from models.schemas.cart_schema import cart_schema
from services import cart_service

def add_to_cart(user_id):
    data = request.get_json()
    product_id = data.get('product_id')
    quantity = data.get('quantity', 1)

    if not product_id or not quantity:
        return jsonify({"message": "Invalid data"}), 400

    cart_item, error = cart_service.add_item_to_cart(user_id, product_id, quantity)
    if error:
        return jsonify({"message": error}), 404

    return cart_item_schema.jsonify(cart_item), 200

def remove_from_cart(user_id):
    data = request.get_json()
    product_id = data.get('product_id')

    if not product_id:
        return jsonify({"message": "Invalid data"}), 400

    cart_item, error = cart_service.remove_item_from_cart(user_id, product_id)
    if error:
        return jsonify({"message": error}), 404

    return cart_item_schema.jsonify(cart_item), 200

def get_cart(user_id):
    cart = cart_service.get_cart(user_id)
    if not cart:
        return jsonify({"message": "Cart not found"}), 404

    return cart_schema.jsonify(cart), 200

def clear_cart(user_id):
    cart, error = cart_service.clear_cart(user_id)
    if error:
        return jsonify({"message": error}), 404

    return jsonify({"message": "Cart cleared successfully"}), 200

