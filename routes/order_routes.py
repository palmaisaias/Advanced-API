from flask import Blueprint
from controllers.order_controller import find_all_orders, find_all_paginate, place_order, get_order

order_bp = Blueprint('orders', __name__)

order_bp.route('/<int:customer_id>/place', methods=['POST'])(place_order)
order_bp.route('/<int:id>', methods=['GET'])(get_order)
order_bp.route('/', methods=['GET'])(find_all_orders)
order_bp.route('/paginate', methods= ['GET'])(find_all_paginate)