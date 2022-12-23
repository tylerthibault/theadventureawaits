from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models import address_model
from flask_app.config.helpers import page_back


# ********* CREATE *********
# @app.route('/address/new')
# def address_new():
#     return render_template('/address_new.html')

@app.route('/address/create', methods=['POST'])
def address_create():
    data = {
        **request.form,
    }
    last_page = page_back()
    if not address_model.Address.validator(**data):
        order_id = session['order_id']
        return redirect(last_page)
    
    address_model.Address.create_one(**data)
    return redirect(last_page)

# ********* READ *********
# @app.route('/address')
# def address_show():
#     context = {
#     'all_addresss' :  address_model.Address.get_all()
#     }
#     return render_template('/pages/address/address_edit.html', **context)
    
# @app.route('/address/<int:id>/edit')
# def address_edit(id):
#     context = {
#         'address' :  address_model.Address.get_one(id=id)
#     }
#     return render_template('/pages/address/address_edit.html', **context)


# ********* UPDATE *********
@app.route('/address/<int:id>/update', methods=['POST'])
def address_update(id):
    data = {
        **request.form,
    }

    if not address_model.Address.validator(**data):
        return redirect(f'/address/{id}/edit')

    address_model.Address.update_one({'id':id}, **data)
    last_page = page_back()
    return redirect(last_page)

# ********* DELETE *********
@app.route('/address/<int:id>/delete')
def address_delete(id):
    address_model.Address.delete_one(id=id)
    last_page = page_back()
    return redirect(last_page)