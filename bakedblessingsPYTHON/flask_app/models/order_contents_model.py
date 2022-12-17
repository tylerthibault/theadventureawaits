from flask_app.models import base_model
from flask import flash, session

class OrderContent(base_model.Base):
    table_name = "order_contents"
    attributes = ['order_id', 'product_id', 'status']
    required_attributes = ['order_id', 'product_id']
    def __init__(self, data):
        super().__init__(data)

        self.order_id = data['order_id']
        self.product_id = data['product_id']
