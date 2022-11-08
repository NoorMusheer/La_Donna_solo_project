from sqlite3 import connect
from flask_app.config.mysqlconnection import connectToMySQL

class Order:
    DB = "la_donna_bridal_atelier"
    def __init__(self, order_data):
        self.id = order_data['id']
        self.bride_id = order_data['bride_id']
        self.dress_id = order_data['dress_id']
        self.created_at = order_data['created_at']
        self.updated_at = order_data['updated_at']

    @classmethod
    def all_orders(cls):
        query = "SELECT * FROM orders;"
        return connectToMySQL(cls.DB).query_db(query)

    @classmethod
    def orders_by_status(cls, data):
        # query = "SELECT * FROM orders WHERE status = %(status)s ;"
        query = """
            SELECT orders.id, brides.first_name AS brfname, brides.last_name AS brlname, name, orders.notes AS order_notes, employees.first_name AS taken_by FROM orders 
            LEFT JOIN brides ON brides.id = orders.bride_id 
            LEFT JOIN dresses ON dresses.id = orders.dress_id
            LEFT JOIN employees ON employees.id = orders.employee_id
            WHERE orders.status = %(status)s;
            """
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def orders_by_id(cls, id):
        data = {
            "id":id,
        }
        query = "SELECT * FROM orders WHERE id = %(id)s ;"
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result[0]

    @classmethod
    def update_status_to_archive(cls, id):
        data={
            "id":id,
            "status":"archived"
        }
        query = "UPDATE orders SET status = %(status)s WHERE id = %(id)s ;"
        connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def add_order_to_db(cls, data):
        query ="INSERT INTO orders (employee_id, dress_id, bride_id, notes, status, created_at, updated_at) VALUES (%(employee_id)s, %(dress_id)s, %(bride_id)s, %(notes)s, %(status)s, NOW(), NOW() );"
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def update_order(cls, o_data):
        query = """
            UPDATE orders
            SET bride_id = %(bride_id)s, dress_id=%(dress_id)s, notes=%(order_notes)s, status=%(status)s, updated_at=NOW()
            WHERE id = %(id)s;
        """
        return connectToMySQL(cls.DB).query_db(query,o_data)