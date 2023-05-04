from flask_app import app
from flask_app.models import bride, dress, employee, measurement, order
from flask import render_template, redirect, request, session

@app.route('/clients')
def index():
    all_brides = bride.Bride.all_brides()
    return render_template("client_list.html", all_brides = all_brides)

@app.route('/all_clients')
def active_clients():
    active_clients = bride.Bride.all_brides()
    return render_template("dashboard2.html", active_clients=active_clients)

@app.route('/new_client')
def new_bride():
    return render_template("client_add.html")

@app.route('/bride_add_name_only', methods = ['POST'])
def add_bride_to_db_name_only():
    data={
        "bride_first_name": request.form['bride_first_name'],
        "bride_last_name":request.form['bride_last_name']
    }
    session['bride_first_name'] = request.form['bride_first_name']
    session['bride_last_name'] = request.form['bride_last_name']
    bride.Bride.add_a_bride_basic(data)
    return redirect ('/choose_next')

@app.route('/choose_next')
def choose_next_step ():
    return render_template("choose.html")

@app.route('/bride_add', methods=['POST'])
def add_bride_to_db():
    data={
        "first_name":request.form['fname'],
        "last_name":request.form['lname'],
        "email":request.form['email'],
        "phone":request.form['phone'],
        "wedding_date":request.form['wedding_date'],
        "other":request.form['other']
    }
    bride.Bride.add_a_bride(data)
    return redirect('/brides')

@app.route('/bride_edit/<int:id>')
def edit_bride_page(id):
    bride_info = bride.Bride.get_bride_by_id(id)
    return render_template('brides_edit.html', bride = bride_info)

@app.route('/bride_update/<int:id>', methods=['POST'])
def update_bride_info(id):
    data={
        "id":id,
        "first_name":request.form['fname'],
        "last_name":request.form['lname'],
        "email":request.form['email'],
        "phone":request.form['phone'],
        "wedding_date":request.form['wedding_date'],
        "notes":request.form['other']
    }
    bride.Bride.update_bride_by_id(data)
    return redirect('/brides')

@app.route('/bride_notes')
def bride_notes():
    bride_list = bride.Bride.all_brides()
    print("****BRIDE LIST*****", bride_list[1])
    return render_template ('notes.html', bride_list = bride_list)

