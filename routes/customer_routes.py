from flask import Blueprint
from controllers.customer_controller import save, get_customers, find_all_paginate, login, get_customer_by_id, update_customer, delete_customer

customer_bp = Blueprint('customers', __name__)

customer_bp.route('/', methods=['POST'])(save)
customer_bp.route('/<int:id>', methods=['GET'])(get_customer_by_id)
customer_bp.route('/<int:id>', methods=['PUT'])(update_customer)
customer_bp.route('/', methods=['GET'])(get_customers)
customer_bp.route('/paginate', methods= ['GET'])(find_all_paginate)
customer_bp.route('/login', methods= ['POST'])(login)
customer_bp.route('/<int:id>', methods=['DELETE'])(delete_customer)
