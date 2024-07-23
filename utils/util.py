from datetime import datetime, timedelta, timezone
import jwt
from flask import jsonify, request
from functools import wraps

SECRET_KEY = "funky_frogs_flip_fruits"

def encode_token(user_id, role):
    payload = {
        'exp': datetime.now(timezone.utc) + timedelta(hours=1),
        'iat': datetime.now(timezone.utc), 
        'sub': user_id,
        'role': role
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

def token_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            try:
                token = request.headers['Authorization'].split()[1]
                payload = jwt.decode(token, SECRET_KEY, algorithms="HS256")
                print("Payload:", payload)
            except jwt.ExpiredSignatureError:
                return jsonify({'message': "Token has expired"}), 401
            except jwt.InvalidTokenError:
                return jsonify({"message": "Invalid token"}), 401
            return func(*args, **kwargs)
        else:
            return ({"messages": "You need token auth baybayyyy"}), 401
    return wrapper

def user_token_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            try:
                token = request.headers['Authorization'].split()[1]
                payload = jwt.decode(token, SECRET_KEY, algorithms="HS256")
                print("Payload:", payload)
            except jwt.ExpiredSignatureError:
                return jsonify({'message': "Token has expired"}), 401
            except jwt.InvalidTokenError:
                return jsonify({"message": "Invalid token"}), 401
            return func(token_id=payload['sub'],*args, **kwargs)
        else:
            return ({"messages": "You need token auth baybayyyy"}), 401
    return wrapper

def admin_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            try:
                token = request.headers['Authorization'].split()[1]
                payload = jwt.decode(token, SECRET_KEY, algorithms="HS256")
                print("Payload:", payload)
            except jwt.ExpiredSignatureError:
                return jsonify({'message': "Token has expired"}), 401
            except jwt.InvalidTokenError:
                return jsonify({"message": "Invalid token"}), 401
            if payload['role'] == 'Admin':
                print(payload['role'])
                return func(*args, **kwargs)
            else:
                return jsonify({"messages": "Admin role required"})
        else:
            return ({"messages": "You need token auth baybayyyy"}), 401
    return wrapper
