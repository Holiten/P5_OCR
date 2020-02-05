import mysql.connector
from constants import USER_NAME, USER_PASSWORD, USER_HOST, DB_NAME, PASSWORD_TYPE


class bdd_sql:

    def __init__(self):
        self.bdd_connect = mysql.connector.connect(user = USER_NAME,
                                                   password = USER_PASSWORD,
                                                   host = USER_HOST,
                                                   database = DB_NAME,
                                                   auth_plugin = PASSWORD_TYPE)

    def connect_db(self):
        self.bdd_connect.connect()

    def close_db(self):
        connection.close()


    def create_db(self):
        pass

    def db_fill(self):
        pass

    def db_save(self):
        pass







"""
db_connection = mysql.connector.connect(user=USER_NAME,
                                        password=USER_PASSWORD,
                                        host=USER_HOST,
                                        database=DB_NAME,
                                        auth_plugin=PASSWORD_TYPE)

cursor = db_connection.cursor()
"""