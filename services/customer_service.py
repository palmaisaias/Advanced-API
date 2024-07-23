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

def find_all_customers():
    query = select(Customer)
    all_customers = db.session.execute(query).scalars().all()
    return all_customers

def find_all_paginate(page, per_page):
    customers = db.paginate(select(Customer), page=page, per_page=per_page)
    return customers

