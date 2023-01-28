from flask_app.config.mysqlconnection import connectToMySQL

class Bride:
    DB = "la_donna_bridal_atelier"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.phone = data['phone']
        self.wedding_date = data['wedding_date']
        self.other = data['other']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dress_id = []

    @classmethod
    def all_brides(cls):
        query = "SELECT * FROM brides;"
        return connectToMySQL(cls.DB).query_db(query)

    @classmethod
    def add_a_bride(cls, data):
        query = "INSERT INTO brides (first_name, last_name, email, phone, wedding_date, other, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(phone)s, %(wedding_date)s, %(other)s, NOW(), NOW() );"
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def add_a_bride_basic(cls, data):
        query = "INSERT INTO brides (first_name, last_name, created_at, updated_at) VALUES (%(bride_first_name)s, %(bride_last_name)s, NOW(), NOW() );"
        return connectToMySQL(cls.DB).query_db(query, data)
        
    @classmethod
    def get_bride_by_id(cls, id):
        data={
            "id":id
        }
        query = "SELECT * FROM brides WHERE id = %(id)s ;"
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result[0]

    @classmethod
    def update_bride_by_id(cls, data):
        query ="""
            UPDATE brides
            SET first_name = %(first_name)s, last_name=%(last_name)s, email=%(email)s, phone=%(phone)s, wedding_date=%(wedding_date)s, other=%(notes)s, updated_at=NOW()
            WHERE id = %(id)s ;
                """
        return connectToMySQL(cls.DB).query_db(query, data)

