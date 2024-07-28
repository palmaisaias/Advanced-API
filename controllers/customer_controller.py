from flask import request, jsonify
from services import customer_service
from models.schemas.customer_schema import customer_schema, customers_schema
from marshmallow import ValidationError
from caching import cache
from utils.util import token_required, admin_required

def login():
    try:
        credentials = request.json
        token = customer_service.login(credentials['username'], credentials['password'])
    except KeyError:
        return jsonify({'messages': 'Invalid payloaddddd, expecting the username and password'}), 401
    if token:
        return jsonify(token), 200
    else:
        return jsonify({'messages': "invalid username OR password...we just wont tell you which"}), 401

def save():
    try:
        customer_data = customer_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    new_customer = customer_service.save(customer_data)
    return customer_schema.jsonify(new_customer), 201

def get_customer_by_id(id):
    customer = customer_service.find_customer_by_id(id)
    if customer is None:
        return {"message": "Customer not found"}, 404
    return customer_schema.jsonify(customer), 200

def update_customer(id):
    data = request.get_json()
    customer = customer_service.update_customer_details(id, data)
    if customer is None:
        return {"message": "Customer not found"}, 404
    return customer_schema.jsonify(customer), 200

def delete_customer(id):
    success = customer_service.delete_customer_by_id(id)
    if not success:
        return {"message": "Customer not found"}, 404
    return {"message": "Customer deleted successfully"}, 200

# @cache.cached(timeout=60)
@admin_required
def get_customers():
    customers = customer_service.find_all_customers()
    return customers_schema.jsonify(customers), 200

@admin_required
def find_all_paginate():
    page = int(request.args.get("page"))
    per_page = int(request.args.get("per_page"))
    customers = customer_service.find_all_paginate(page, per_page)
    return customers_schema.jsonify(customers), 200