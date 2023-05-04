from flask_app import app
from flask_app.models import bride, dress, employee, measurement, order
from flask import render_template, redirect, request, session
from flask_mail import Mail, Message
import random
import string
import smtplib

mail = Mail(app)

# @app.route('/')
# def main_page():
#     return render_template('login.html')

@app.route('/')
def main_page():
    return render_template('/test_pages/login_pin.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

# @app.route('/check_login', methods=["POST"])
# def validate_login_info():
#     login_data = {
#         "email":request.form['email'],
#         "password":request.form['password']
#     }
#     an_employee = employee.Employee.get_employee_by_email(login_data)
#     print(" ---- AN EMPLOYEE----", an_employee)
#     if not employee.Employee.validate_login(login_data, an_employee):
#         return redirect('/')
#     session['id'] = an_employee['id']
#     session['first_name']=an_employee['first_name']
#     session['last_name']=an_employee['last_name']
#     session['permission']=an_employee['permission']
#     return redirect('/dashboard')

@app.route('/check_login', methods=["POST"])
def validate_login_info():
    login_data = {
        "user_email":request.form['user_login'],
        "pin":request.form['password']
    }
    print ("****LOGIN DATA***** : ", login_data)
    an_employee = employee.Employee.get_employee_by_email(login_data)
    print(" ---- AN EMPLOYEE----", an_employee)
    if not employee.Employee.validate_pin(login_data, an_employee):
        return redirect('/')
    session['id'] = an_employee['id']
    session['first_name']=an_employee['first_name']
    session['last_name']=an_employee['last_name']
    session['permission']=an_employee['permission']
    return redirect('/dashboard')



@app.route('/check_registration', methods=["POST"])
def validate_registration():
    reg_data = {
        "registration_code":request.form['registration_code'],
        "email":request.form['email'],
        "password":request.form['password'],
        "password_confirm":request.form['password_confirm']
    }
    an_employee = employee.Employee.get_employee_by_email(reg_data)
    if not employee.Employee.validate_registration(reg_data, an_employee):
        return redirect('/')
    employee.Employee.update_employee_password(reg_data)
    
    return redirect('/login_after_register')


@app.route('/login_after_register')
def login_page_after_register():
    return render_template('login_after_reg.html')


@app.route('/dashboard')
def user_dashborad():
    if session:
        active_clients = bride.Bride.all_brides()
        return render_template('dashboard2.html', active_clients=active_clients) #Change to dashboard_new_test.html to change back
    else:
        return redirect('/')

@app.route('/employees')
def employees():
    all_employees = employee.Employee.get_all_employees()
    return render_template('employees_list.html', all_employees = all_employees)

@app.route('/forgot_login', methods=["POST"])
def update_pw():
    data = {
        "email": request.form['email']
    }
    employee.Employee.reset_pw_request_message(data)
    return redirect('/forgot_pw')

@app.route('/forgot_pw')
def req_pw_reset_page():
    return render_template('forgot_login.html')


    
@app.route('/new_employee')
def add_new_empl_page():
    random_code =''.join(random.choices(string.ascii_uppercase + string.digits, k=9))
    return render_template('employee_add.html', random_code = random_code)

@app.route('/employee_add', methods=["POST"])
def add_empl_to_db():
    ee_data={
        "first_name":request.form['fname'],
        "last_name":request.form['lname'],
        "title":request.form['title'],
        "email":request.form['email'],
        "phone":request.form['phone'],
        "addr_street":request.form['addr_street'],
        "addr_city":request.form['addr_city'],
        "addr_state":request.form['addr_state'],
        "addr_zip":request.form['addr_zip'],
        "permission":request.form['permission'],
        "hire_date":request.form['hire_date'],
        "reg_code":request.form['reg_code']
    }
    employee.Employee.add_employee_to_db(ee_data)

    msg = Message("Welcome to La Donna Bridal %s" % request.form['fname'], sender="noreply@laDonna.com", recipients = ["NoorMusheer@aol.com"])
    msg.html = """
    <b>Welcome!</b>
    We are excited to have you start. <br>
    Please follow the link below to register and set up your account password.<br>
    Your registration code is:  %r <br>
    <a href="http://localhost:5000/">Click Here to Register</a>
    """ % request.form['reg_code']
    mail.send(msg)

    return redirect('/employees')

@app.route('/my_account')
def employee_account_info():
    id = session['id']
    my_acct_info =  employee.Employee.get_employee_by_id(id)
    return render_template('employee_info.html', my_info = my_acct_info)

@app.route('/employee_update/<int:id>', methods=['POST'])
def update_employee_info(id):
    data={
        "id":id, 
        "email":request.form['email'],
        "phone":request.form['phone'],
        "addr_street":request.form['addr_street'],
        "addr_city":request.form['addr_city'],
        "addr_state":request.form['addr_state'],
        "addr_zip":request.form['addr_zip'],
    }
    employee.Employee.update_employee(data)
    return redirect('/my_account')

@app.route('/ee_info_mngr/<int:id>')
def view_ee_info(id):
    ee_data = employee.Employee.get_employee_by_id(id)
    return render_template('employee_info_mngr.html', ee_data = ee_data)
