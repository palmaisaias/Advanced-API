from database import db
from models.order import Order
from models.product import Product
from sqlalchemy import select
from datetime import date

def save_order(order_data):
    new_order = Order(order_date=date.today(), customer_id=order_data['customer_id'])

    for item_id in order_data['items']:
        query = select(Product).filter(Product.id == item_id)
        item = db.session.execute(query).scalar()
        new_order.products.append(item)

    db.session.add(new_order)
    db.session.commit()
    db.session.refresh(new_order)
    return new_order

def find_all_orders():
    query = select(Order)
    all_orders = db.session.execute(query).scalars().all()
    return all_orders

def find_all_paginate(page, per_page):
    orders = db.paginate(select(Order), page=page, per_page=per_page)
    return orders
