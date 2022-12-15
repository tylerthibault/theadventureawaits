from flask_app.models import base_model
from flask import flash, session
from flask_app import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User(base_model.Base):
    table_name = "users"
    attributes = ['first_name', 'last_name', 'email', 'phone_num', 'pw', 'level']
    def __init__(self, data):
        super().__init__(data)
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.phone_num = data['phone_num']
        self.pw = data['pw']
        self.level = data['level']

    @classmethod
    def login_validator(cls, **data):
        if not super().validator(**data):
            return False
        
        is_valid = True

        if not EMAIL_REGEX.match(data['email_login']): 
            flash("Invalid email address!", "err_users_email_login")
            is_valid = False

        if is_valid:
            potential_user = cls.get_one(email=data['email_login'])
            print(potential_user)
            if not potential_user:
                is_valid = False
                flash("Invalid Credentials", "err_users_pw_login")
            else:
                if not bcrypt.check_password_hash(potential_user.pw, data['pw_login']):
                    is_valid = False
                    flash("Invalid Credentials", "err_users_pw_login")
                else:
                    session['uuid'] = potential_user.id
                    session['level'] = potential_user.level
        
        return is_valid


