from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models import order_model, user_model
from flask_app.config.helpers import generateCode, admin_required, login_required


# ********* CREATE *********
@app.route('/order/new')
def order_new():
    return render_template('/order_new.html')

@app.route('/order/create', methods=['GET'])
def order_create():
    data = {
        **request.form,
        'user_id': session['uuid'] if 'uuid' in session else None,
        'confirmation_num': generateCode() 
    }

    if not order_model.Order.validator(**data):
        return redirect('/#menu')
    
    order_id = order_model.Order.create_one(**data)
    session['order_id'] = order_id

    return redirect('/#menu')

# ********* READ *********
@app.route('/admin/orders')
@login_required
@admin_required
def admin_orders():
    context = {
        'all_orders': order_model.Order.get_all()
    }
    return render_template('/admin/orders.html', **context)

@app.route('/order/<int:id>')
def order_show(id):
    context = {
    'order' :  order_model.Order.get_one({'id': id}),
    }
    if 'uuid' in session:
        context['user'] = user_model.User.get_one(id=session['uuid'])
    return render_template('/order_show.html', **context)
    
@app.route('/order/<int:id>/edit')
def order_edit(id):
    context = {
        'order' :  order_model.Order.get_one(id=id)
    }
    return render_template('/pages/order/order_edit.html', **context)


# ********* UPDATE *********
@app.route('/order/<int:id>/update', methods=['POST'])
def order_update(id):
    data = {
        **request.form,
    }

    if not order_model.Order.validator(**data):
        return redirect(f'/order/{id}/edit')

    order_model.Order.update_one({'id':id}, **data)
    return redirect(f'/order/{id}/edit')

# ********* DELETE *********
@app.route('/order/<int:id>/delete')
def order_delete(id):
    order_model.Order.delete_one(id=id)
    del session['order_id']
    
    # TODO Navigate back to where you came from 
    return redirect('/#menu')