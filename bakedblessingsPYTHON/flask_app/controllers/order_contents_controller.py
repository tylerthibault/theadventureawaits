from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models import order_contents_model


# ********* CREATE *********
@app.route('/cart/new')
def cart_new():
    return render_template('/cart_new.html')

@app.route('/cart/<int:product_id>/create', methods=['GET'])
def cart_create(product_id):
    data = {
        **request.form,
        'order_id': session['order_id'],
        'product_id': product_id
    }

    if not order_contents_model.OrderContent.validator(**data):
        return redirect('/#menu')
    
    order_contents_model.OrderContent.create_one(**data)
    return redirect('/#menu')

# ********* READ *********
@app.route('/cart')
def cart_show():
    context = {
    'all_carts' :  order_contents_model.OrderContent.get_all()
    }
    return render_template('/pages/cart/cart_edit.html', **context)
    
@app.route('/cart/<int:id>/edit')
def cart_edit(id):
    context = {
        'cart' :  order_contents_model.OrderContent.get_one(id=id)
    }
    return render_template('/pages/cart/cart_edit.html', **context)


# ********* UPDATE *********
@app.route('/cart/<int:id>/update', methods=['POST'])
def cart_update(id):
    data = {
        **request.form,
    }

    if not order_contents_model.OrderContent.validator(**data):
        return redirect(f'/cart/{id}/edit')

    order_contents_model.OrderContent.update_one({'id':id}, **data)
    return redirect(f'/cart/{id}/edit')

# ********* DELETE *********
@app.route('/cart/<int:id>/delete')
def cart_delete(id):
    order_contents_model.OrderContent.delete_one(id=id)
    return redirect('/cart')