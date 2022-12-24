from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models import product_model, category_model
from flask_app.config.helpers import admin_required, login_required, log_page, upload_photo


# ********* CREATE *********
@app.route('/admin/products')
@login_required
@admin_required
@log_page
def admin_products():
    context = {
        'all_products': product_model.Product.get_all_with_category(),
        'all_categories': category_model.Category.get_all_with_products()
    }
    return render_template("admin/products.html", **context)

@app.route('/admin/product/create', methods=['POST'])
@login_required
@admin_required
def product_create():
    data = {
        **request.form,
        'is_available': 1 if 'is_available' in request.form else 0
    }

    if not data['size']:
         del data['size']

    if 'img_url' in request.files:
        data['img_url'] = upload_photo(request.files['img_url'])

    if not product_model.Product.validator(**data):
        print("Not Valid")
        print(request.form)
        return redirect('/admin/products')
    
    print(data)
    product_model.Product.create_one(**data)
    return redirect('/admin/products')

# ********* READ *********
@app.route('/admin/product')
@login_required
@admin_required
def product_show():
    context = {
    'all_products' :  product_model.Product.get_all()
    }
    return render_template('/pages/product/product_edit.html', **context)

@app.route('/admin/product/<int:id>/edit')
@login_required
@admin_required
def product_edit(id):
    context = {
        'product' :  product_model.Product.get(id=id),
        'all_categories': category_model.Category.get_all()
    }
    return render_template('/admin/product_edit.html', **context)


# ********* UPDATE *********
@app.route('/admin/product/<int:id>/update', methods=['POST'])
@login_required
@admin_required
def product_update(id):
    data = {
        **request.form,
        'is_available': 1 if 'is_available' in request.form else 0
    }

    if not data['size']:
         del data['size']

    if 'img_url' in request.files:
        if request.files['img_url']:
            data['img_url'] = upload_photo(request.files['img_url'])

    if not product_model.Product.validator(**data):
        return redirect(f'/admin/product/{id}/edit')

    product_model.Product.update_one({'id':id}, **data)
    return redirect(f'/admin/products')

# ********* DELETE *********
@app.route('/admin/product/<int:id>/delete')
@login_required
@admin_required
def product_delete(id):
    product_model.Product.delete_one(id=id)
    return redirect('/admin/products')