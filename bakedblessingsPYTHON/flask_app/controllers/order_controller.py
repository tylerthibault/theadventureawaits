from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models import order_model, user_model, address_model, config_model
from flask_app.config.helpers import generateCode, admin_required, login_required, log_page, page_back
import datetime

order_status_list = ['finalizing order', 'order submitted', 'order in process', 'order ready', 'out for delivery', 'order completed']
order_status_colors = ['bg-red-500 text-white', 'bg-orange-400' , 'bg-yellow-300', 'bg-green-300', 'bg-yellow-300', 'bg-green-700 text-white']

# ********* CREATE *********
# @app.route('/order/new')
# def order_new():
#     return render_template('/order_new.html')

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
@log_page
def admin_orders():
    all_orders = order_model.Order.get_all()

    seven_days = datetime.date.today() + datetime.timedelta(days=7)
    
    sorted_orders = {}
    if len(all_orders) > 0:
        current_date = str(all_orders[0].delivery_date)
        for order in all_orders:
            if order.status != 'order completed':
                if order.delivery_date:
                    if order.delivery_date < seven_days:
                        if order.delivery_date != current_date:
                            current_date = order.delivery_date
                        
                        if current_date not in sorted_orders:
                            sorted_orders[current_date] = []
                        sorted_orders[current_date].append(order)

    print(sorted_orders)

    context = {
        'all_orders': all_orders,
        'sorted_orders': sorted_orders,
        'order_status_list': order_status_list,
        'order_status_colors': order_status_colors
    }
    return render_template('/admin/orders.html', **context)

@app.route('/admin/orders/all')
@login_required
@admin_required
@log_page
def admin_orders_all():
    all_orders = order_model.Order.get_all()

    context = {
        'all_orders': all_orders,
        'order_status_list': order_status_list,
        'order_status_colors': order_status_colors
    }
    return render_template('/admin/orders_all.html', **context)

@app.route('/dashboard/orders')
@log_page
@login_required
def order_one():
    context = {
        'user': user_model.User.get(id=session['uuid']),
        'all_orders': order_model.Order.get_all({'user_id': session['uuid']})
    }
    return render_template("pages/order_one.html", **context)

@app.route('/dashboard/order/<int:id>')
@log_page
def order_show(id):
    context = {
    'order' :  order_model.Order.get_one({'id': id}),
    'order_status_list': order_status_list,
    }
    if 'uuid' in session:
        context['user'] = user_model.User.get(id=session['uuid'])
    return render_template('/pages/order_show.html', **context)

@app.route('/admin/order/<int:id>')
@login_required
@admin_required
@log_page
def admin_order_show(id):
    context = {
    'order' :  order_model.Order.get_one({'id': id}),
    'order_status_list': order_status_list
    }
    if 'uuid' in session:
        context['user'] = user_model.User.get(id=session['uuid'])
    return render_template('/admin/order_show.html', **context)
    
# ********* UPDATE *********
@app.route('/order/<int:id>/update', methods=['POST'])
@login_required
def order_update(id):
    last_page = page_back()
    data = {
        **request.form,
    }

    if not order_model.Order.validate(data):
        return redirect(last_page)

    if not order_model.Order.validator(**data):
        return redirect(last_page)

    # order_model.Order.update_one({'id':id}, **data)
    # if 'order_id' in session:
    #     del session['order_id']
    
    return redirect(last_page)

@app.route('/api/order/<int:id>/update', methods=['POST'])
@login_required
def api_order_update(id):
    res = {
        'msg': "GTG"
    }

    data = {
        **request.form,
    }

    if 'is_pickup' in request.form:
        if request.form['is_pickup'] == 0:
            address_data = {
                'street': request.form['street'],
                'city': request.form['city'],
                'state': request.form['state'],
                'zip': request.form['zip'],
            }
            if 'is_primary' in request.form:
                address_data['is_primary'] = 1

            address_id = address_model.Address.create_one(**address_data)
            data['address_id'] = address_id
    
    if 'has_paid' in data:
        data['has_paid'] = 1

    if not order_model.Order.validator(**data):
        return res, 402

    order_model.Order.update_one({'id':id}, **data)
    if 'order_id' in session:
        del session['order_id']
    
    
    return res, 200

@app.route("/api/order/<int:id>/date_checker", methods=['POST'])
def date_checker(id):
    print(request.form)
    order_model.Order.update_one({'id': id}, **request.form)
    res = {
        'msg': "date added"
    }
    return res, 200

# ********* DELETE *********
@app.route('/order/<int:id>/delete')
def order_delete(id):
    order_model.Order.delete_one(id=id)
    del session['order_id']
    
    # TODO Navigate back to where you came from 
    return redirect('/#menu')