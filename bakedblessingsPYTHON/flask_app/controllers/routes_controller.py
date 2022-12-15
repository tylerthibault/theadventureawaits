from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models import user_model
from flask_app.config.helpers import login_required, admin_required

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")

@app.route("/admin/dashboard")
@login_required
@admin_required
def admin_dashboard():
    return render_template("admin/dashboard.html")