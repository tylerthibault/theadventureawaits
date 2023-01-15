from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models import user_model, category_model, order_model, config_model
from flask_app.config.helpers import login_required, admin_required, log_page

@app.route("/")
@log_page
def index():
    context = {
        'all_categories': category_model.Category.get_all_with_products(),
        'config': config_model.Config.get(id=1)
    }
    if 'order_id' in session:
        context['order'] = order_model.Order.get_one({'id': session['order_id']})

    return render_template("pages/index.html", **context)

@app.route("/dashboard")
@log_page
@login_required
def dashboard():
    return redirect("/dashboard/orders")
    # context = {
    #     'user': user_model.User.get(id=session['uuid'])
    # }
    # return render_template("pages/dashboard.html", **context)

@app.route("/admin/dashboard")
@log_page
@login_required
@admin_required
def admin_dashboard():
    return redirect("/admin/orders")
    return render_template("admin/dashboard.html")

