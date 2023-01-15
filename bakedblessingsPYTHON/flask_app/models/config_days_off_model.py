from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import base_model
from flask import flash, session
from flask_app import DATABASE

class DaysOff(base_model.Base):
    table_name = "days_off"
    attributes = ['day']
    required_attributes = ['day']
    
    def __init__(self, data):
        super().__init__(data)

        self.day = data['day']

    @classmethod
    def get_10(cls):
        query = "SELECT * FROM days_off WHERE day >= CURDATE() ORDER BY day LIMIT 10;"
        results = connectToMySQL(DATABASE).query_db(query)
        if not results:
            return []

        all_dates = []
        for date in results:
            all_dates.append( cls(date) )
        return all_dates

    @staticmethod
    def validator(**data):
        is_valid = True

        if len(data['day']) < 1:
            is_valid = False
            flash("*Date is required", "err_days_off_day")

        potential_date = DaysOff.get(day=data['day'])
        if potential_date:
            is_valid = False
            flash("You have already taken that day off", "err_days_off_day")
        
        return is_valid
