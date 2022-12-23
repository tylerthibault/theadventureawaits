from functools import wraps
from flask import request, redirect, session
import requests
import base64
import os
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

def log_page(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'history' not in session:
            session['history'] = []
        
        history = session['history']
        current_page = request.path

        if len(history) > 0:
            if current_page != history[-1]:
                history.append(current_page)
                session['history'] = history
        else:
            history.append(current_page)
            session['history'] = history
        return f(*args, **kwargs)
    return decorated_function

def page_back():
    if 'history' in session:
        history = session['history']
        return history.pop()
    else:
        return '/'

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

def upload_photo(file):
    base64_file = base64.b64encode(file.read())
    url = "https://api.imgbb.com/1/upload"
    payload = {
        'key': os.environ.get("IMGBB_KEY"),
        'image': base64_file
    }
    resp = requests.post(url, payload)
    resp = resp.json()
    print("**************************************")
    print(resp)
    return resp['data']['url']

