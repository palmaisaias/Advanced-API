from database import db
from models.cart import Cart
from models.cartItem import CartItem
from models.product import Product

def add_item_to_cart(user_id, product_id, quantity):
    product = db.session.get(Product, product_id)
    if not product:
        return None, "Product not found"

    cart = db.session.query(Cart).filter_by(user_id=user_id).first()
    if not cart:
        cart = Cart(user_id=user_id)
        db.session.add(cart)
        db.session.commit()

    cart_item = db.session.query(CartItem).filter_by(cart_id=cart.id, product_id=product_id).first()
    if cart_item:
        cart_item.quantity += quantity
        cart_item.price = product.price
    else:
        cart_item = CartItem(cart_id=cart.id, product_id=product_id, quantity=quantity, price=product.price)
        db.session.add(cart_item)

    db.session.commit()
    return cart_item, None

def remove_item_from_cart(user_id, product_id):
    cart = db.session.query(Cart).filter_by(user_id=user_id).first()
    if not cart:
        return None, "Cart not found"

    cart_item = db.session.query(CartItem).filter_by(cart_id=cart.id, product_id=product_id).first()
    if not cart_item:
        return None, "Cart item not found"

    db.session.delete(cart_item)
    db.session.commit()
    return cart_item, None

def get_cart(user_id):
    cart = db.session.query(Cart).filter_by(user_id=user_id).first()
    return cart
