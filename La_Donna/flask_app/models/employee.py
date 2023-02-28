from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
import re
from flask import flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

PASSWORD_REGEX = re.compile (r'^(?=.*[A-Z])(?=.*[a-z])(?=.*?[0-9]).{8,}$')


class Employee: 
    DB = "la_donna_bridal_atelier"
    def __init__(self, ee_data):
        self.id = ee_data['id']
        self.first_name = ee_data['first_name']
        self.last_name = ee_data['last_name']
        self.title = ee_data['title']
        self.email = ee_data['email']
        self.phone= ee_data['phone']
        self.addr_street = ee_data['addr_street']
        self.addr_city = ee_data['addr_city']
        self.addr_state = ee_data['addr_state']
        self.addr_zip = ee_data['addr_zip']
        self.permission = ee_data['permission']
        self.hire_date = ee_data['hire_date']
        self.password = ee_data['password']
        self.created_at = ee_data['created_at']
        self.updated_at = ee_data['updated_at']
        self.to_do_id = []

    @classmethod
    def get_all_employees(cls):
        query = "SELECT * FROM employees;"
        return connectToMySQL(cls.DB).query_db(query)

    @classmethod
    def add_employee_to_db(cls,ee_data):
        query = "INSERT INTO employees (first_name, last_name, title, email, phone, addr_street, addr_city, addr_state, addr_zip, permission, hire_date, reg_code, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(title)s, %(email)s, %(phone)s, %(addr_street)s, %(addr_city)s, %(addr_state)s, %(addr_zip)s, %(permission)s, %(hire_date)s, %(reg_code)s, NOW(), NOW() );"
        return connectToMySQL(cls.DB).query_db(query, ee_data)

    @classmethod
    def get_employee_by_id(cls, id):
        data ={
            "id":id
        }
        query = "SELECT * FROM employees WHERE id = %(id)s ;"
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result[0]

    @classmethod
    def get_employee_by_email(cls, ee_data):
        query = "SELECT * FROM employees WHERE email = %(user_email)s;"
        result = connectToMySQL(cls.DB).query_db(query,ee_data)
        if result == ():
            return False
        else:
            return result[0]

    @classmethod
    def update_employee_password(cls, reg_data):
        data={
            "email":reg_data['email'],
            "password":bcrypt.generate_password_hash(reg_data['password'])
        }
        query = """
        UPDATE employees
        SET password = %(password)s
        WHERE email = %(email)s ;
        """
        return connectToMySQL(cls.DB).query_db(query, data)
    
    
    @staticmethod
    def validate_login(login_data, an_employee):
        is_valid = True
        if not an_employee:
            flash("*E-mail / password combination does not match our records. Please try again, or  register <a href='/'>HERE</a>.", "login")
            is_valid = False
        elif not an_employee['password']:
            flash("* It looks like you have not registered yet, please register. ", "login")
            is_valid = False
        elif not bcrypt.check_password_hash(an_employee['password'], login_data['password']):
            flash("*E-mail and password combination do not match our records. Please try again, or register <a href='/'>HERE</a>.", "login")
            is_valid = False
        return is_valid

    @staticmethod
    def validate_pin(login_data, an_employee):
        is_valid = True
        if not an_employee:
            flash("E-mail and PIN combination does not match our records. Please try again.", "login")
            is_valid = False
        elif (an_employee['pin'] != login_data['pin']):
            flash("*Sorry cuz, that's not the boss' code! Go get her to help you. ", "login")
            is_valid = False
        return is_valid

    @staticmethod
    def validate_registration(reg_data, an_employee):
        is_valid = True
        if not an_employee:
            flash("*Employee Email not found. Please contact your manager. ", "register")
            is_valid = False
        elif not PASSWORD_REGEX.match(reg_data['password']):
            flash("* At least one number, one Upper Case letter, one Lower case letter is required  ", 'register')
            is_valid = False
        elif len(reg_data['password'])<8:
            flash("* Password must be at least 8 characters. ")
            is_valid = False
        elif not reg_data['registration_code']:
            flash ("* Please enter a registration code", "register")
            is_valid = False
        elif reg_data['password'] != reg_data['password_confirm']:
            flash("* Passwords do not match. Try again. ", "register")
            is_valid = False
        return is_valid

    @staticmethod
    def reset_pw_request_message(data):
        flash("* Thank you. If your email address is found in our system, an email message will be sent to it with a link to where you can reset your password.", "update_pw")
        return True

    @classmethod
    def update_employee(cls, data):
        query = """
            UPDATE employees
            SET email=%(email)s, phone=%(phone)s, addr_street=%(addr_street)s, addr_city=%(addr_city)s, addr_state=%(addr_state)s, addr_zip=%(addr_zip)s, updated_at=NOW() 
            WHERE id = %(id)s; 
        """
        return connectToMySQL(cls.DB).query_db(query, data)