from flask_app import app, bcrypt
from flask import render_template, redirect, session, request, flash
from flask_app.models import user_model, order_model
from flask_app.config.helpers import login_required, admin_required, page_back, log_page


@app.route('/user/login', methods=['POST'])
def user_login():
    data = {
        **request.form,
    }
    if not user_model.User.login_validator(**data):
        return redirect('/user/new')
    
    return redirect('/')

@app.route('/user/logout')
def user_logout():
    del session['uuid']
    if 'order_id' in session:
        order_model.Order.delete_one(id=session['order_id'])
        del session['order_id']
    return redirect('/')

# ********* CREATE *********
@app.route('/user/new')
@log_page
def user_new():
    return render_template('pages/user_new.html')


@app.route('/user/create', methods=['POST'])
def user_create():
    data = {
        **request.form,
    }
    if not user_model.User.validator(**data):
        return redirect('/user/new')
    
    hash_pw = bcrypt.generate_password_hash(data['pw'])
    data['pw'] = hash_pw

    userId = user_model.User.create_one(**data)
    session['uuid'] = userId
    session['level'] = user_model.User.get(id=userId).level

    return redirect('/')

# ********* READ *********
@app.route('/dashboard/user/<int:id>/edit')
@log_page
def user_edit(id):
    context = {
        'user' :  user_model.User.get(id=id)
    }
    return render_template('/pages/user_edit.html', **context)

@app.route("/admin/users")
@login_required
@admin_required
@log_page
def all_users():
    context = {
        "all_users": user_model.User.get_all()
    }
    return render_template("admin/users.html", **context)

# ********* UPDATE *********
@app.route('/user/<int:id>/update', methods=['POST'])
def user_update(id):
    last_page = page_back()
    if id != session['uuid']:
        return redirect(last_page)

    data = {
        **request.form,
    }

    if 'old_pw' in data:
        if not user_model.User.update_pw(data):
            return redirect(last_page)

    if not user_model.User.validator(**data):
        return redirect(last_page)

    user_model.User.update_one({'id':id}, **data)
    return redirect(last_page)

# ********* DELETE *********
@app.route('/user/<int:id>/delete')
def user_delete(id):
    user_model.User.delete_one(id=id)
    return redirect('/user')