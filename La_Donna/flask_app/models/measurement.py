from flask_app.config.mysqlconnection import connectToMySQL

class Measurement:
    DB = "la_donna_bridal_atelier"
    def __init__(self, ms_data):
        self.id = ms_data['id']
        self.bride_id = ms_data['id']
        self.bk_sh_wdth = ms_data['bk_sh_wdth']
        self.one_shoulder = ms_data['bk_sh_wdth']
        self.bust = ms_data['bk_sh_wdth']
        self.waist = ms_data['waist']
        self.hip = ms_data['bk_sh_wdth']
        self.underbust = ms_data['bk_sh_wdth']
        self.bp_to_bp = ms_data['bk_sh_wdth']
        self.chest = ms_data['bk_sh_wdth']
        self.sh_to_waist_fr = ms_data['bk_sh_wdth']
        self.sh_to_waist_bk = ms_data['bk_sh_wdth']
        self.waist_to_floor_fr = ms_data['bk_sh_wdth']
        self.waist_to_floor_bk = ms_data['bk_sh_wdth']
        self.hollow_to_floor = ms_data['bk_sh_wdth']
        self.hollow_to_neckline = ms_data['bk_sh_wdth']
        self.armhole = ms_data['bk_sh_wdth']
        self.bicep = ms_data['bk_sh_wdth']
        self.arm_circumfrence = ms_data['bk_sh_wdth']
        self.sleeve_lngth = ms_data['bk_sh_wdth']
        self.elbow = ms_data['bk_sh_wdth']
        self.wrist = ms_data['bk_sh_wdth']
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