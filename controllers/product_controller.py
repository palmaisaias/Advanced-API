from flask import request, jsonify
from services import product_service
from models.schemas.product_schema import product_schema, products_schema
from marshmallow import ValidationError

def save_product():
    try:
        product_data = product_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    new_product = product_service.save_product(product_data)
    return product_schema.jsonify(new_product), 201

def update_product(product_id):
    data = request.get_json()
    if not data:
        return {"message": "Invalid data"}, 400

    product = product_service.update_product_details(product_id, data)
    if product is None:
        return {"message": "Product not found"}, 404
    return product_schema.jsonify(product), 200

def delete_product(product_id):
    success = product_service.delete_product_by_id(product_id)
    if not success:
        return {"message": "Product not found"}, 404
    return {"message": "Product deleted successfully"}, 200

def get_products():
    products = product_service.find_all_products()
    return products_schema.jsonify(products), 200

def find_all_paginate():
    page = int(request.args.get("page"))
    per_page = int(request.args.get("per_page"))
    products = product_service.find_all_paginate(page, per_page)
    return products_schema.jsonify(products), 200