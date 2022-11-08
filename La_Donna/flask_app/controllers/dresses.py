from flask_app import app
from flask_app.models import bride, dress, employee, measurement, order
from flask import render_template, redirect, request, session

@app.route('/dresses')
def dresses_list():
    active_dr = {
        "status":"active"
    }
    active_dresses = dress.Dress.dress_by_status(active_dr)
    archive_dr = {
        "status":"archived"
    }
    archived_dresses = dress.Dress.dress_by_status(archive_dr)
    return render_template("dresses_list.html", active_dresses = active_dresses, archived_dresses = archived_dresses)

@app.route('/new_dress')
def add_a_dress():
    return render_template('dress_add.html')

@app.route('/dress_add', methods=["POST"])
def add_dress_to_db():
    data={
        "employee_id":1,
        "name":request.form['dress_name'],
        "style":request.form['style'],
        "color":request.form['color'],
        "fabric":request.form['fabric'],
        "other":request.form['other'],
        "status":"active"
    }
    dress.Dress.add_dress(data)
    return redirect('/dresses')

@app.route('/dress_edit/<int:id>')
def edit_dress_info(id):
    dress_data = dress.Dress.get_dress_by_id(id)
    return render_template('dress_edit.html', dress_data = dress_data)

@app.route('/dress_update/<int:id>', methods=["POST"])
def update_dress_info(id):
    updated_dress_data={
        "id":id,
        "name":request.form['dress_name'],
        "style":request.form['style'],
        "color":request.form['color'],
        "fabric":request.form['fabric'],
        "other":request.form['other'],
        "status":"active"
    }
    dress.Dress.update_dress_info(updated_dress_data)
    return redirect('/dresses')

@app.route('/dress_archive/<int:id>')
def archive_dress(id):
    dress.Dress.update_dress_status_to_archive(id)
    return redirect('/dresses')
