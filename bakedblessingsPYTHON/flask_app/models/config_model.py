from flask_app.models import base_model
from flask import flash, session

class Config(base_model.Base):
    table_name = "config"
    attributes = ['max_daily_orders', 'announcement', 'deliver_monday', 'deliver_tuesday', 'deliver_wednesday', 'deliver_thursday', 'deliver_friday', 'deliver_saturday', 'deliver_sunday']
    required_attributes = []
    def __init__(self, data):
        super().__init__(data)

        # TODO: create attributes
        self.max_daily_orders = data['max_daily_orders']
        self.announcement = data['announcement']
        self.deliver_monday = data['deliver_monday']
        self.deliver_tuesday = data['deliver_tuesday']
        self.deliver_wednesday = data['deliver_wednesday']
        self.deliver_thursday = data['deliver_thursday']
        self.deliver_friday = data['deliver_friday']
        self.deliver_saturday = data['deliver_saturday']
        self.deliver_sunday = data['deliver_sunday']


