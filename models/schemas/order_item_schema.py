from models.schemas.schema import ma
from marshmallow import fields
from models.schemas.product_schema import ProductSchema

class OrderItemSchema(ma.Schema):
    id = fields.Integer(required=False)
    order_id = fields.Integer(required=True)
    product_id = fields.Integer(required=True)
    quantity = fields.Integer(required=True)
    price = fields.Float(required=True)
    product = fields.Nested(ProductSchema, only=["product_name", "price"])

    class Meta:
        fields = ('id', 'order_id', 'product_id', 'quantity', 'price', 'product')

order_item_schema = OrderItemSchema()
order_items_schema = OrderItemSchema(many=True)
