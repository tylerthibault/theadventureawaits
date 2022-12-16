from flask_app.models import base_model, product_model
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
from flask_app import DATABASE

class Category(base_model.Base):
    table_name = "categories"
    attributes = ['name']
    required_attributes = ['name']
    def __init__(self, data):
        super().__init__(data)
        self.name = data['name']

    def __repr__(self) -> str:
        return self.name

    @classmethod
    def get_all_with_products(cls):
        query = "SELECT * FROM categories JOIN products ON products.category_id = categories.id;"
        results = connectToMySQL(DATABASE).query_db(query)
        if not results:
            return []
        
        all_categories = []
        for dict in results:
            print(dict)
            product_data = {
                **dict,
                'id': dict['products.id'],
                'name': dict['products.name'],
                'created_at': dict['products.created_at'],
                'updated_at': dict['products.updated_at'],
            }
            product = product_model.Product(product_data)

            found_item = False
            for item in all_categories:
                if item.name == dict['name']:
                    found_item = item
                
            if found_item:
                found_item.all_products.append(product)
            else:
                category = cls(dict)
                category.all_products = []
                category.all_products.append(product)
                all_categories.append(category)
        return all_categories