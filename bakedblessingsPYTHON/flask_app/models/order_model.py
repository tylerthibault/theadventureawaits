from flask_app.models import base_model, product_model, user_model, address_model
from flask import flash, session
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class Order(base_model.Base):
    table_name = "orders"
    attributes = ['user_id', 'delivery_date', 'address_id', 'status', 'public_notes', 'has_paid', 'public_note_read', 'private_notes', 'is_pickup', 'payment_type']
    required_attributes = ['user_id']

    def __init__(self, data):
        super().__init__(data)
        self.user_id = data['user_id']
        self.status = data['status']
        self.delivery_date = data['delivery_date']
        self.address_id = data['address_id']
        self.public_notes = data['public_notes']
        self.public_note_read = data['public_note_read']
        self.private_notes = data['private_notes']
        self.is_pickup = data['is_pickup']
        self.payment_type = data['payment_type']
        self.has_paid = data['has_paid']

    @property
    def get_address(self):
        return address_model.Address.get(id = self.address_id)
    
    @property 
    def get_user(self):
        return user_model.User.get(id = self.user_id)

    @classmethod
    def get_all(cls, data=None):
        if data:
            query = "SELECT * FROM orders LEFT JOIN order_contents ON order_contents.order_id = orders.id LEFT JOIN products ON order_contents.product_id = products.id LEFT JOIN users ON orders.user_id = users.id where user_id = %(user_id)s;"
            results = connectToMySQL(DATABASE).query_db(query, data)
        else:
            query = "SELECT * FROM orders LEFT JOIN order_contents ON order_contents.order_id = orders.id LEFT JOIN products ON order_contents.product_id = products.id LEFT JOIN users ON orders.user_id = users.id;"
            results = connectToMySQL(DATABASE).query_db(query)
        if not results:
            return []
        all_orders = []
        orders_processed = []
        product_list = []
        for dict in results:
            if dict['id'] in orders_processed:
                order_idx = orders_processed.index(dict['id'])
                order = all_orders[order_idx]
            else:
                order = cls(dict)
                product_list = []

                user_data = {
                    **dict,
                    'id': dict['users.id'],
                    'created_at': dict['users.created_at'],
                    'updated_at': dict['users.updated_at'],
                }
                user = user_model.User(user_data)
                order.user = user
            
            product_data = {
                **dict,
                'id': dict['products.id'],
                'created_at': dict['products.created_at'],
                'updated_at': dict['products.updated_at'],
            }
            product = product_model.Product(product_data)
            
            if dict['id'] in orders_processed:
                order.product_list.append(product)
            else:
                product_list.append(product)
                order.product_list = product_list
                orders_processed.append(dict['id'])
                all_orders.append(order)
        return all_orders

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM orders JOIN order_contents ON order_contents.order_id = orders.id JOIN products ON order_contents.product_id = products.id WHERE orders.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if not results:
            return False

        order = cls(results[0])
        product_list = []
        sum = 0
        for dict in results:
            product_data = {
                **dict,
                'id': dict['products.id'],
                'created_at': dict['products.created_at'],
                'updated_at': dict['products.updated_at'],
            }
            product = product_model.Product(product_data)
            product_list.append(product)
            sum += int(dict['price'])
        order.product_list = product_list
        order.total = sum
        return order
