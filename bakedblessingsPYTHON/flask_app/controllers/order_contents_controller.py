from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models import order_contents_model
from flask_app.config.helpers import page_back


# ********* CREATE *********
# @app.route('/order_content/new')
# def order_content_new():
#     return render_template('/order_content_new.html')

@app.route('/order_content/<int:product_id>/create', methods=['GET'])
def order_content_create(product_id):
    data = {
        **request.form,
        'order_id': session['order_id'],
        'product_id': product_id
    }

    if not order_contents_model.OrderContent.validator(**data):
        return redirect('/#menu')
    
    order_contents_model.OrderContent.create_one(**data)
    return redirect('/#menu')

@app.route('/api/order_content/<int:product_id>/create', methods=['GET'])
def api_order_content_create(product_id):
    data = {
        'order_id': session['order_id'],
        'product_id': product_id
    }
    
    order_contents_model.OrderContent.create_one(**data)
    res = {
        'msg': 'All good'
    }
    return res, 200

# ********* READ *********
# @app.route('/order_content')
# def order_content_show():
#     context = {
#     'all_order_contents' :  order_contents_model.OrderContent.get_all()
#     }
#     return render_template('/pages/order_content/order_content_edit.html', **context)
    
# @app.route('/order_content/<int:id>/edit')
# def order_content_edit(id):
#     context = {
#         'order_content' :  order_contents_model.OrderContent.get_one(id=id)
#     }
#     return render_template('/pages/order_content/order_content_edit.html', **context)


# ********* UPDATE *********
@app.route('/order_content/<int:id>/update', methods=['POST'])
def order_content_update(id):
    data = {
        **request.form,
    }
    last_page = page_back()
    if not order_contents_model.OrderContent.validator(**data):
        return redirect(last_page)

    order_contents_model.OrderContent.update_one({'id':id}, **data)
    return redirect(last_page)

# ********* DELETE *********
@app.route('/order_content/<int:product_id>/<int:order_id>/delete')
def order_content_delete(product_id, order_id):

    order_contents_model.OrderContent.delete_one(product_id=product_id, order_id=order_id)
    last_page = page_back()
    return redirect(last_page)