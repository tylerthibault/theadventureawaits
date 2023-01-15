from flask import Flask
from flask_bcrypt import Bcrypt
import os
app = Flask(__name__)

app.secret_key = "bananas"
bcrypt = Bcrypt(app)

IS_LOCAL = False

DATABASE = "BakedBlessingsDB" if IS_LOCAL else os.environ.get("DATABASE_DB")