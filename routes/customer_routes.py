from flask import Blueprint
from controllers.customer_controller import save, get_customers, find_all_paginate, login

customer_bp = Blueprint('customers', __name__)

customer_bp.route('/', methods=['POST'])(save)
customer_bp.route('/', methods=['GET'])(get_customers)
customer_bp.route('/paginate', methods= ['GET'])(find_all_paginate)
customer_bp.route('/login', methods= ['POST'])(login)
