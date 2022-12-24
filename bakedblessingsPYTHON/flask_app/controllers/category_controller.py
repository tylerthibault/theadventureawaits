from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models import category_model
from flask_app.config.helpers import admin_required, login_required, page_back


# ********* CREATE *********
# @app.route('/admin/category/new')
# @login_required
# @admin_required
# def category_new():
#     return render_template('/category_new.html')

@app.route('/admin/category/create', methods=['POST'])
@login_required
@admin_required
def category_create():
    data = {
        **request.form,
    }
    last_page = page_back()
    if not category_model.Category.validator(**data):
        return redirect(last_page)
    
    category_model.Category.create_one(**data)
    return redirect(last_page)

# ********* READ *********
# @app.route('/admin/category')
# @login_required
# @admin_required
# def category_show():
#     context = {
#     'all_categorys' :  category_model.Category.get_all()
#     }
#     return render_template('/pages/category/category_edit.html', **context)

# @app.route('/admin/category/<int:id>/edit')
# @login_required
# @admin_required
# def category_edit(id):
#     context = {
#         'category' :  category_model.Category.get(id=id)
#     }
#     return render_template('/pages/category/category_edit.html', **context)


# ********* UPDATE *********
@app.route('/admin/category/<int:id>/update', methods=['POST'])
@login_required
@admin_required
def category_update(id):
    data = {
        **request.form,
    }
    last_page = page_back()
    if not category_model.Category.validator(**data):
        return redirect(f'/category/{id}/edit')

    category_model.Category.update_one({'id':id}, **data)
    return redirect(f'/category/{id}/edit')

# ********* DELETE *********
@app.route('/admin/category/<int:id>/delete')
@login_required
@admin_required
def category_delete(id):
    category_model.Category.delete_one(id=id)
    last_page = page_back()
    return redirect(last_page)