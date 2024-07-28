from models.schemas.schema import ma
from marshmallow import fields
from models.schemas.cart_item_schema import CartItemSchema

class CartSchema(ma.Schema):
    id = fields.Integer(required=False)
    user_id = fields.Integer(required=True)
    items = fields.List(fields.Nested(CartItemSchema), required=False)

    class Meta:
        fields = ('id', 'user_id', 'items')

cart_schema = CartSchema()
carts_schema = CartSchema(many=True)
