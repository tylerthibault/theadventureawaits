from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models import config_model, config_days_off_model
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
        'config': config_model.Config.get(id = 1),
        'all_days_off': config_days_off_model.DaysOff.get_10()
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
@app.route('/admin/config/update', methods=['POST'])  
@login_required
@admin_required
def config_update():
    data = {
        **request.form,
    }

    attributes = ['deliver_monday', 'deliver_tuesday', 'deliver_wednesday', 'deliver_thursday', 'deliver_friday', 'deliver_saturday', 'deliver_sunday']
    for attribute in attributes:
        if attribute in data:
            data[attribute] = 1
        else:
            data[attribute] = 0
    
    last_page = page_back()

    if not config_model.Config.validator(**data):
        return redirect(last_page)

    config_model.Config.update_one({'id':1}, **data)
    return redirect(last_page)

@app.route('/admin/config/days_off/update', methods=['post'])
@login_required
@admin_required
def days_off_update():
    last_page = page_back()
    if not config_days_off_model.DaysOff.validator(**request.form):
        return redirect(last_page)
    config_days_off_model.DaysOff.create_one(**request.form)
    return redirect(last_page)


# ********* DELETE *********
@app.route('/admin/config/days_off/<int:id>/delete')
def config_delete(id):
    last_page = page_back()
    config_days_off_model.DaysOff.delete_one(id=id)
    return redirect(last_page)