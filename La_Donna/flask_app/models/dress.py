from flask_app.config.mysqlconnection import connectToMySQL

class Dress: 
    DB = "la_donna_bridal_atelier"
    def __init__(self,dress_data):
        self.id = dress_data['id']
        self.employee_id = dress_data['employee_id']
        self.name = dress_data['name']
        self.style = dress_data['style']
        self.color = dress_data['color']
        self.fabric = dress_data['fabric']
        self.other = dress_data['other']
        self.status = dress_data['status']
        self.created_at = dress_data['created_at']
        self.updated_at = dress_data['updated_at']

    @classmethod
    def all_dresses(cls):
        query = "SELECT * FROM dresses;"
        return connectToMySQL(cls.DB).query_db(query)

    @classmethod
    def dress_by_status(cls, data):
        query = "SELECT * FROM dresses WHERE status = %(status)s ;"
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def add_dress(cls, data):
        query = "INSERT INTO dresses (employee_id, name, style, color, fabric, other, status, created_at, updated_at) VALUES (%(employee_id)s, %(name)s,%(style)s,%(color)s,%(fabric)s,%(other)s,%(status)s,NOW(), NOW() );"
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_dress_by_id(cls, id):
        data={
            "id":id
        }
        query = "SELECT * FROM dresses where id = %(id)s ;"
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result[0]

    @classmethod
    def update_dress_info(cls, updated_dress_data):
        query = """
                UPDATE dresses
                SET name = %(name)s, style=%(style)s, color=%(color)s, fabric=%(fabric)s, other=%(other)s, status=%(status)s, updated_at=NOW()
                WHERE id = %(id)s;
                """
        return connectToMySQL(cls.DB).query_db(query, updated_dress_data)

    @classmethod
    def update_dress_status_to_archive(cls, id):
        data={
            "id":id,
            "status":"archived"
        }
        query = "UPDATE dresses SET status = %(status)s WHERE id = %(id)s ;"
        connectToMySQL(cls.DB).query_db(query, data)