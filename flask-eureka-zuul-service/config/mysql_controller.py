import pymysql
import config

class mysql_controller:
    def __init__(self):
        self.conn = pymysql.connect(
            host=config.DB_HOST, user=config.DB_USER, password=config.DB_PASSWORD, db=config.DB_SCHEMA, charset='utf8')
        self.curs = self.conn.cursor()

    def insert_total(self, total):
        sql = 'INSERT INTO entire_nodes (count_of_nodes) VALUES (%s)'
        self.curs.execute(sql, (total,))
        self.conn.commit()
