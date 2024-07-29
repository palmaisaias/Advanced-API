from models.schemas.schema import ma
from marshmallow import fields
from models.schemas.order_item_schema import OrderItemSchema

class OrderSchema(ma.Schema):
    id = fields.Integer(required=False)
    order_date = fields.Date(required=False)
    customer_id = fields.Integer(required=True)
    items = fields.List(fields.Nested(OrderItemSchema))
    customer = fields.Nested("CustomerOrderSchema")

    class Meta:
        fields = ('id', 'order_date', 'customer_id', 'items', 'customer')

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)

