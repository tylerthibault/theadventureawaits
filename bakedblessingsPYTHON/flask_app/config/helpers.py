from functools import wraps
from flask import request, redirect, session
import random

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

def generateCode():
    options = [
        ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],
        [1,2,3,4,5,6,7,8,9,0],
        ['!','@','#','$','&'],
    ]

    code = ""
    for idx in range(10):
        option = options[random.randint(0, len(options) - 1)]
        idx = random.randint(0, len(option) - 1)
        char = str(option[idx])
        code += char
    
    return code
