from database import db
from models.product import Product
from sqlalchemy import select

def save_product(product_data):
    new_product = Product(
        product_name=product_data['product_name'], 
        price=product_data['price']
    )
    db.session.add(new_product)
    db.session.commit()
    db.session.refresh(new_product)
    return new_product

def update_product_details(product_id, data):
    product = db.session.get(Product, product_id)
    if product:
        if 'product_name' in data:
            product.product_name = data['product_name']
        if 'price' in data:
            product.price = data['price']
        db.session.commit()
        return product
    return None

def delete_product_by_id(product_id):
    product = db.session.get(Product, product_id)
    if product:
        db.session.delete(product)
        db.session.commit()
        return True
    return False

def find_all_products():
    query = select(Product)
    all_products = db.session.execute(query).scalars().all()
    return all_products

def find_all_paginate(page, per_page):
    products = db.paginate(select(Product), page=page, per_page=per_page)
    return products