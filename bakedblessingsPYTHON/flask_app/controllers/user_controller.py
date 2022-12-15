from flask_app import app, bcrypt
from flask import render_template, redirect, session, request
from flask_app.models import user_model


@app.route('/user/login', methods=['POST'])
def user_login():
    data = {
        **request.form,
    }
    if not user_model.User.login_validator(**data):
        return redirect('/user/new')
    
    if session['level'] > 1:
        return redirect('/admin/dashboard')
    return redirect('/dashboard')

@app.route('/user/logout')
def user_logout():
    del session['uuid']
    return redirect('/')

# ********* CREATE *********
@app.route('/user/new')
def user_new():
    return render_template('/user_new.html')


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
    session['level'] = user_model.User.get_one(id=userId).level

    return redirect('/')

# ********* READ *********
@app.route('/user/')
def user_show():
    context = {
        'all_users' :  user_model.User.get_all()
    }
    return render_template('/pages/user/user_show.html', **context)

@app.route('/user/<int:id>/edit')
def user_edit(id):
    context = {
        'user' :  user_model.User.get_one(id=id)
    }
    return render_template('/pages/user/user_edit.html', **context)


# ********* UPDATE *********
@app.route('/user/<int:id>/update', methods=['POST'])
def user_update(id):
    data = {
        **request.form,
    }

    if not user_model.User.validator(**data):
        return redirect(f'/user/{id}/edit')

    user_model.User.update_one({'id':id}, **data)
    return redirect(f'/user/{id}/edit')

# ********* DELETE *********
@app.route('/user/<int:id>/delete')
def user_delete(id):
    user_model.User.delete_one(id=id)
    return redirect('/user')