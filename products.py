"""File to create the product object and its methods"""

import mysql.connector
from constants import CONFIG_TABLES

class Products:
    """Class to create the product object and its methods"""
    def __init__(self, cat, apidata):
        self.product_name = apidata[0]
        self.product_score = apidata[1]
        self.product_url = apidata[2]
        self.product_store = apidata[3]
        self.product_cat = cat
        self.conv = ()

    def conv_prod(self):
        """Method to convert in tuple"""
        self.conv = (self.product_name, self.product_score, self.product_url, self.product_store,)

    def insert(self):
        """Method to insert products in bdd"""
        cnx = mysql.connector.connect(**CONFIG_TABLES)
        cursor = cnx.cursor()

        sql = "INSERT INTO products (name_product, score_product, product_url, product_store)" \
              "VALUES (%s, %s, %s, %s)"

        cursor.execute(sql, self.conv)
        cnx.commit()

    def screen_prod(self):
        """Method to screen product"""
        return [self.product_name, self.product_score, self.product_url, self.product_store, self.product_cat]
