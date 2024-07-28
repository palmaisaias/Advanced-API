from models.schemas.schema import ma
from marshmallow import fields, validate

class CartItemSchema(ma.Schema):
    id = fields.Integer(required=False)
    cart_id = fields.Integer(required=True)
    product_id = fields.Integer(required=True)
    quantity = fields.Integer(required=True, validate=validate.Range(min=1))
    price = fields.Float(required=True, validate=validate.Range(min=0))

    class Meta:
        fields = ('id', 'cart_id', 'product_id', 'quantity', 'price')

cart_item_schema = CartItemSchema()
cart_items_schema = CartItemSchema(many=True)
