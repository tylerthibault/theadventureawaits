from flask_app.models import base_model, category_model
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
from flask_app import DATABASE

class Product(base_model.Base):
    table_name = "products"
    attributes = ['name', 'size', 'description', 'price', 'is_available', 'qty', 'category_id', 'img_url']
    required_attributes = ['name', 'price']
    
    def __init__(self, data):
        super().__init__(data)
        self.name = data['name']
        self.size = data['size']
        self.description = data['description']
        self.price = data['price']
        self.is_available = data['is_available']
        self.qty = data['qty']
        self.category_id = data['category_id']
        self.img_url = data['img_url']

    @property
    def get_category(self):
        return category_model.Category.get_one(id=self.category_id)

    @classmethod
    def get_all_with_category(cls):
        query = "SELECT * FROM products JOIN categories ON products.category_id = categories.id;"
        results = connectToMySQL(DATABASE).query_db(query)
        if not results:
            return []
        
        all_products = []
        for dict in results:
            product = cls(dict)
            category_data = {
                **dict,
                'id': dict['categories.id'],
                'updated_at': dict['categories.updated_at'],
                'created_at': dict['categories.created_at'],
            }
            product.category = category_model.Category(category_data)
            all_products.append(product)
        return all_products
