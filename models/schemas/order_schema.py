from models.schemas.schema import ma
from marshmallow import fields
from models.schemas.product_schema import ProductSchema

class OrderSchema(ma.Schema):
    id = fields.Integer(required=False)
    order_date = fields.Date(required=False)
    customer_id = fields.Integer(required=True)
    products = fields.List(fields.Nested(ProductSchema))
    customer = fields.Nested("CustomerOrderSchema")

    class Meta:
        fields = ('id', 'date', 'customer_id', 'product_ids', 'products', 'customer')

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)
