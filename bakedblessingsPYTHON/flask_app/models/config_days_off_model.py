from flask_app.models import base_model
from flask import flash, session

class DaysOff(base_model.Base):
    table_name = "days_off"
    attributes = ['day']
    required_attributes = ['day']
    def __init__(self, data):
        super().__init__(data)

        self.day = data['day']