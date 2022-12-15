from functools import wraps
from flask import request, redirect, session

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'uuid' not in session:
            return redirect('/')
        return f(*args, **kwargs)
    return decorated_function

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session['level'] <= 1:
            return redirect('/')
        return f(*args, **kwargs)
    return decorated_function