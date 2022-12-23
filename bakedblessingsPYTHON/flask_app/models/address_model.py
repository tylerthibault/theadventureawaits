from flask_app.models import base_model
from flask import flash, session

class Address(base_model.Base):
    table_name = "addresses"
    attributes = ['street', 'state', 'city', 'zip', 'user_id', 'is_primary']
    required_attributes = ['street', 'state', 'city', 'zip', 'user_id']
    def __init__(self, data):
        super().__init__(data)

        self.street = data['street']
        self.city = data['city']
        self.state = data['state']
        self.zip = data['zip']
        self.user_id = data['user_id']
        self.is_primary = data['is_primary']
        self.full = f"{self.street} {self.city} {self.state} {self.zip}"