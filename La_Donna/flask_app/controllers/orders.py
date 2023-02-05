from flask_app import app
from flask_app.models import bride, dress, employee, measurement, order
from flask import render_template, redirect, request, session


@app.route('/orders')
def orders_page():
    active = {
        "status":"active"
    }
    active_orders = order.Order.orders_by_status(active)
    archived = {
        "status":"archived"
    }
    archived_orders = order.Order.orders_by_status(archived)
    return render_template('orders_list.html', active_orders = active_orders, archived_orders = archived_orders)

@app.route('/measurements_page')
def start_order_test_page():
    return render_template('test_pages/order_add_test.html')

@app.route('/archive_order/<int:id>')
def update_to_archived(id):
    order.Order.update_status_to_archive(id)
    return redirect('/orders')

@app.route('/new_order')
def new_order():
    return render_template('test_pages/order_add_test2.html')

@app.route('/order_add', methods=["POST"])
def add_order_to_db():
    data={
        "employee_id":session['id'],
        "dress_id":request.form['dress_id'],
        "bride_id":request.form['bride_id'],
        "notes":request.form['notes'],
        "status":"active"
    }
    m_data = {
        "bride_id":request.form['bride_id'],
        "height":request.form['m_height'],
        "waist":request.form['m_waist'],
    }
    measurement.Measurement.add_measurement(m_data)
    order.Order.add_order_to_db(data)
    return redirect('/orders')

@app.route('/orders_edit/<int:id>')
def edit_orders(id):
    selected_order  = order.Order.orders_by_id(id)
    the_brides_id = selected_order['bride_id']
    bride_measurements = measurement.Measurement.measurement_by_bride_id(the_brides_id)
    return render_template ('orders_edit.html', order = selected_order, bride_m = bride_measurements)

@app.route('/order_update/<int:id>', methods=['POST'])
def update_order_form(id):
    o_data = {
        "id":id,
        "bride_id":request.form['bride_id'],
        "dress_id":request.form['dress_id'],
        "order_notes":request.form['notes'],
        "status":"active"
    }
    m_data={
        "m_id":request.form['m_id'],
        "bride_id":request.form['bride_id'],
        "m_height":request.form['m_height'],
        "m_waist":request.form['m_waist']
    }
    order.Order.update_order(o_data)
    measurement.Measurement.update_measurements(m_data)
    return redirect ('/orders')