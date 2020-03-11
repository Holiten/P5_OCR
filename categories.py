"""V 2.0 - File to create the categories object and its methods"""

import mysql.connector
from constants import CONFIG_TABLES

class Categories:
    """Class to create the product object and its methods"""

    def __init__(self, name):
        self.name = name

    def conv_cat(self):
        """Method to convert in tuple"""
        return (self.name, )

    def insert_cat(self):
        """Method to insert categories in bdd"""
        cnx = mysql.connector.connect(**CONFIG_TABLES)
        cursor = cnx.cursor()
        sql = "INSERT INTO categories (name_cat) VALUES (%s)"
        cat = self.conv_cat()

        cursor.execute(sql, cat)
        print(cursor)
        cnx.commit()
