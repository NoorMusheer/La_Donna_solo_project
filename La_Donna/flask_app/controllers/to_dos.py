from flask_app import app
from flask_app.models import bride, dress, employee, measurement, order, to_do
from flask import render_template, redirect, request, session

@app.route('/task_list')
def to_do_page():
    active_ee_tasks = {
        "id":session['id'],
        "status":"active"
    }
    active_tasks= to_do.To_Do.task_by_employee_id(active_ee_tasks)

    completed_ee_tasks = {
        "id":session['id'],
        "status":"completed"
    }
    completed_tasks = to_do.To_Do.task_by_employee_id(completed_ee_tasks)
    return render_template('to_do_list.html', active_tasks = active_tasks, completed_tasks = completed_tasks)

@app.route('/task_new')
def add_new_task_page():
    return render_template('to_do_add.html')

@app.route('/task_add', methods=["POST"])
def add_task_to_db():
    data={
        "employee_id":session['id'],
        "notes":request.form['notes'],
        "status":"active",
        "date_due":request.form['date_due']
    }
    to_do.To_Do.new_task(data)
    return redirect('/task_list')

@app.route('/task_edit/<int:id>')
def edit_task(id):
    task_info = to_do.To_Do.task_by_id(id)
    return render_template('to_do_view.html', task_info = task_info)

@app.route('/task_update/<int:id>', methods=["POST"])
def update_task(id):
    data = {
        "id":id, 
        "notes":request.form['notes'],
        "status":"active",
        "date_due":request.form['date_due']
    }
    to_do.To_Do.update_task(data)
    return redirect('/task_list')

@app.route('/task_complete/<int:id>')
def update_task_status(id):
    data={
        "id":id, 
        "status":"completed"
    }
    to_do.To_Do.update_task_status(data)
    return redirect('/task_list')




