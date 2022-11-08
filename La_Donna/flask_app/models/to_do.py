from flask_app.config.mysqlconnection import connectToMySQL

class To_Do:
    DB = "la_donna_bridal_atelier"
    def __init__(self, tddata):
        self.id = tddata['id']
        self.notes = tddata['notes']
        self.status=tddata['status']
        self.date_due = tddata['date_due']
        self.created_at = tddata['created_at']
        self.updated_at = tddata['updated_at']

    @classmethod
    def all_to_do_items(cls):
        query = "SELECT * FROM to_do_items;"
        return connectToMySQL(cls.DB).query_db(query)

    @classmethod
    def new_task(cls, data):
        query = "INSERT INTO to_do_items (employee_id, notes, status, date_due, created_at, updated_at) VALUES (%(employee_id)s, %(notes)s, %(status)s, %(date_due)s, NOW(), NOW() );"
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def task_by_employee_id(cls, data):
        
        query = """
                SELECT * FROM to_do_items 
                LEFT JOIN employees
                ON to_do_items.employee_id = employees.id
                WHERE employees.id = %(id)s 
                AND status = %(status)s;
                """
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def task_by_id(cls, id):
        data = {
            "id":id
        }
        query ="SELECT * FROM to_do_items WHERE id = %(id)s;"
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result[0]

    @classmethod
    def update_task(cls, data):
        query = """
            UPDATE to_do_items
            SET notes = %(notes)s, status = %(status)s, date_due =%(date_due)s, updated_at = NOW()
            WHERE id = %(id)s;
        """
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def update_task_status(cls, data):
        query = """
            UPDATE to_do_items
            SET status = %(status)s
            WHERE id = %(id)s;
        """
        return connectToMySQL(cls.DB).query_db(query, data)
