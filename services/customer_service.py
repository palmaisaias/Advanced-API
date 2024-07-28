from database import db
from models.customer import Customer
from sqlalchemy import select
from utils.util import encode_token

def login(username, password):
    query = select(Customer).where(Customer.username == username)
    customer = db.session.execute(query).scalar_one_or_none()

    if customer and customer.password == password:
        auth_token = encode_token(customer.id, customer.role.role_name)

        response = {
            "status": "Success!",
            "message": "You have ACTUALLY logged in",
            "auth_token": auth_token
        }
        return response

def save(customer_data):
    new_customer = Customer(
        customer_name=customer_data['customer_name'], 
        email=customer_data['email'], 
        phone=customer_data['phone'],
        username=customer_data['username'],
        password=customer_data['password'],
        role_id=customer_data['role_id']
    )
    db.session.add(new_customer)
    db.session.commit()
    db.session.refresh(new_customer)
    return new_customer

def find_customer_by_id(customer_id):
    query = select(Customer).where(Customer.id == customer_id)
    customer = db.session.execute(query).scalars().one_or_none()
    return customer

def find_all_customers():
    query = select(Customer)
    all_customers = db.session.execute(query).scalars().all()
    return all_customers

def update_customer_details(id, data):
    customer = find_customer_by_id(id)
    if customer:
        if 'customer_name' in data:
            customer.customer_name = data['customer_name']
        if 'email' in data:
            customer.email = data['email']
        if 'phone' in data:
            customer.phone = data['phone']
        db.session.commit()
    return customer

def delete_customer_by_id(id):
    customer = find_customer_by_id(id)
    if customer:
        db.session.delete(customer)
        db.session.commit()
        return True
    return False

def find_all_paginate(page, per_page):
    customers = db.paginate(select(Customer), page=page, per_page=per_page)
    return customers

