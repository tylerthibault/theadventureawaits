from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models import user_model, category_model, order_model
from flask_app.config.helpers import login_required, admin_required

@app.route("/")
def index():
    context = {
        'all_categories': category_model.Category.get_all_with_products(),
    }
    if 'order_id' in session:
        context['order'] = order_model.Order.get_one({'id': session['order_id']})

    return render_template("index.html", **context)

@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")

@app.route("/admin/dashboard")
@login_required
@admin_required
def admin_dashboard():
    return render_template("admin/dashboard.html")