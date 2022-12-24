from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models import config_model
from flask_app.config.helpers import admin_required, login_required, log_page, page_back

# ********* CREATE *********
@app.route('/config/new')
def config_new():
    return render_template('/config_new.html')

@app.route('/config/create', methods=['POST'])
def config_create():
    data = {
        **request.form,
    }
    if not config_model.Config.validator(**data):
        return redirect('/config')
    
    config_model.Config.create_one(**data)
    return redirect('/config')

# ********* READ *********
@app.route("/admin/settings")
@log_page
@login_required
@admin_required
def admin_settings():
    context = {
        'config': config_model.Config.get(id = 1)
    }
    return render_template("admin/settings.html", **context)

@app.route('/config')
def config_show():
    context = {
    'all_configs' :  config_model.Config.get_all()
    }
    return render_template('/pages/config/config_edit.html', **context)
    
@app.route('/config/<int:id>/edit')
def config_edit(id):
    context = {
        'config' :  config_model.Config.get(id=id)
    }
    return render_template('/pages/config/config_edit.html', **context)


# ********* UPDATE *********
@app.route('/config/update', methods=['POST'])  
def config_update():
    data = {
        **request.form,
    }
    last_page = page_back()

    if not config_model.Config.validator(**data):
        return redirect(last_page)

    config_model.Config.update_one({'id':1}, **data)
    return redirect(last_page)

# ********* DELETE *********
@app.route('/config/<int:id>/delete')
def config_delete(id):
    config_model.Config.delete_one(id=id)
    return redirect('/config')