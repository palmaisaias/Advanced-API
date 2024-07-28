from flask import Blueprint
from controllers.cart_controller import add_to_cart, remove_from_cart, get_cart,clear_cart

cart_bp = Blueprint('cart', __name__)

cart_bp.route('/<int:user_id>/add', methods=['POST'])(add_to_cart)
cart_bp.route('/<int:user_id>/remove', methods=['POST'])(remove_from_cart)
cart_bp.route('/<int:user_id>', methods=['GET'])(get_cart)
cart_bp.route('/<int:user_id>/clear', methods=['POST'])(clear_cart)
