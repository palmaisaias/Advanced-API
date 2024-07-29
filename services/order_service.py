from datetime import date
from models.order import Order
from models.orderItem import OrderItem
from models.cart import Cart
from database import db
from sqlalchemy import select

def save_order_from_cart(customer_id):
    cart = db.session.query(Cart).filter_by(user_id=customer_id).first()
    if not cart:
        raise ValueError("Cart not found")

    new_order = Order(order_date=date.today(), customer_id=customer_id)
    for cart_item in cart.items:
        order_item = OrderItem(
            product_id=cart_item.product_id,
            quantity=cart_item.quantity,
            price=cart_item.price
        )
        new_order.items.append(order_item)

    db.session.add(new_order)
    db.session.commit()

    # Clear the cart after placing the order
    for cart_item in cart.items:
        db.session.delete(cart_item)
    db.session.commit()

    return new_order

def find_order_by_id(order_id):
    order = db.session.query(Order).filter_by(id=order_id).first()
    return order

def find_all_orders():
    query = select(Order)
    all_orders = db.session.execute(query).scalars().all()
    return all_orders

def find_all_paginate(page, per_page):
    orders = db.paginate(select(Order), page=page, per_page=per_page)
    return orders
