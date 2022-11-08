from flask_app.config.mysqlconnection import connectToMySQL

class Measurement:
    DB = "la_donna_bridal_atelier"
    def __init__(self, ms_data):
        self.id = ms_data['id']
        self.bride_id = ms_data['id']
        self.height = ms_data['height']
        self.waist = ms_data['waist']
        self.created_at = ms_data['created_at']
        self.updated_at = ms_data['updated_at']

    @classmethod
    def all_measurements(cls):
        query = "SELECT * FROM measurements;"
        return connectToMySQL(cls.DB).query_db(query)

    @classmethod
    def add_measurement(cls, m_data):
        query = "INSERT INTO measurements (bride_id, height, waist, created_at, updated_at) VALUES (%(bride_id)s, %(height)s, %(waist)s, NOW(), NOW()) ;"
        return connectToMySQL(cls.DB).query_db(query, m_data)

    @classmethod
    def measurement_by_bride_id(cls, the_brides_id):
        data={
            "id":the_brides_id
        }
        query = "SELECT * FROM measurements WHERE bride_id = %(id)s ; "
        result =  connectToMySQL(cls.DB).query_db(query, data)
        return result[0]

    @classmethod
    def update_measurements(cls, m_data):
        query="""
            UPDATE measurements
            SET bride_id = %(bride_id)s, height=%(m_height)s, waist=%(m_waist)s, updated_at=NOW()
            WHERE id = %(m_id)s ;
        """
        return connectToMySQL(cls.DB).query_db(query,m_data)