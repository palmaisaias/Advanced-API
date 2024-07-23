from models.schemas.schema import ma
from marshmallow import fields, validate

class ProductSchema(ma.Schema):
    id = fields.Integer(required=False)
    product_name = fields.String(required=True, validate=validate.Length(min=1))
    price = fields.Float(required=True, validate=validate.Range(min=0))

    class Meta:
        fields = ('id', 'product_name', 'price')

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
