import pymysql

import config.develoment


class Database:
    def __init__(self):
        self.db = pymysql.connect(host=config.develoment.DB_HOST,
                                  user=config.develoment.DB_USER,
                                  password=config.develoment.DB_PASSWORD,
                                  db=config.develoment.DB_NAME,
                                  charset='utf8')
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)

    def execute(self, query, args={}):
        self.cursor.execute(query, args)

    def executeOne(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchone()
        return row

    def executeAll(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchall()
        return row

    def commit(self):
        self.db.commit()

    def close(self):
        self.db.close()