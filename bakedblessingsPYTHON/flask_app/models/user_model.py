from flask_app.models import base_model, address_model
from flask import flash, session
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app import bcrypt

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User(base_model.Base):
    table_name = "users"
    attributes = ['first_name', 'last_name', 'email', 'phone_num', 'pw', 'level']
    required_attributes = ['first_name', 'last_name', 'email', 'pw', 'phone_num']
    def __init__(self, data):
        super().__init__(data)
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.phone_num = data['phone_num']
        # self.pw = data['pw']
        self.level = data['level']
        self.is_verified = data['is_verified']
        self.fullname = f"{self.first_name.capitalize()} {self.last_name.capitalize()}"

    @property 
    def get_pw(self):
        query = f"SELECT pw FROM users WHERE id = {self.id}"
        result = connectToMySQL(DATABASE).query_db(query)
        return result[0]['pw']


    @property
    def get_address(self):
        return address_model.Address.get(user_id=self.id)

    @classmethod
    def login_validator(cls, **data):
        if not super().validator(**data):
            return False
        
        is_valid = True

        if not EMAIL_REGEX.match(data['email_login']): 
            flash("Invalid email address!", "err_users_email_login")
            is_valid = False

        if is_valid:
            potential_user = cls.get(email=data['email_login'])
            print(potential_user)
            if not potential_user:
                is_valid = False
                flash("Invalid Credentials", "err_users_pw_login")
            else:
                if not bcrypt.check_password_hash(potential_user.get_pw, data['pw_login']):
                    is_valid = False
                    flash("Invalid Credentials", "err_users_pw_login")
                else:
                    session['uuid'] = potential_user.id
                    session['level'] = potential_user.level
        
        return is_valid

    @staticmethod
    def update_pw(data):
        is_valid = True

        current_user = User.get(id=session['uuid'])
        if not bcrypt.check_password_hash(current_user.get_pw, data['old_pw']):
            flash("Old Password do not match", "err_user_pw")
            is_valid = False

        if data['pw'] != data['confirm_pw']:
            flash("New Passwords do not match", "err_user_pw_confirm")
            is_valid = False

        return is_valid



