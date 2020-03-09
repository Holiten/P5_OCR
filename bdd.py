"""V.2.0 - File to create the bdd object and its methods"""

import sys
import mysql.connector
import requests
from products import Products
from constants import CONFIG_BDD, PAGE_NUMBER, CATEGORIES

class Bdd:
    """Class to create the bdd object and its methods"""
    def __init__(self):
        self.products_data = []
        self.cnx = mysql.connector.connect(**CONFIG_BDD)
        self.cursor = self.cnx.cursor()
        self.cat_choice = ""
        self.product_choice = ""
        self.user_save = ""
        self.exist = []

    def load_data(self):
        """Method to load data from Api"""
        if self.exist == [('ocr_p5',)]:
            print("")
        else:
            for page in range(0, PAGE_NUMBER + 1):
                for cat_key, cat_value in CATEGORIES.items():
                    if cat_key:
                        r_page = requests.get(cat_value + str(page + 1) + ".json")
                        r_page_json = r_page.json()
                        products_by_page = r_page_json[u'products']

                        for products in products_by_page:
                            prod = Products(cat_key, [
                                products.get('product_name_fr', 'NULL'),
                                products.get('nutriscore_grade', 'NULL'),
                                products.get('url', 'No data'),
                                products.get('stores', 'No data')])
                            if prod.product_name not in ['', 'NULL'] and \
                                    prod.product_score not in ['', 'N'] and \
                                    prod.product_store not in ['', 'No data']:
                                self.products_data.append(prod)

    def bdd_exist(self):
        """Method to verify if bdd exist"""
        sql = "SHOW DATABASES like 'ocr_p5'"
        self.cursor.execute(sql)
        for elems in self.cursor:
            self.exist.append(elems)
            return self.exist


    def bdd_create(self):
        """Method to create bdd"""
        sql = "CREATE DATABASE IF NOT EXISTS `ocr_p5` CHARACTER SET utf8"
        try:
            self.cursor.execute(sql)
            self.cnx.commit()
            print("The database has been successfully created")

        except mysql.connector.errors as error:
            print(error)
            print("A problem occurred during the creation of the bdd, please check your SQL server")
            sys.exit()

    def bdd_use(self):
        """Method to use bdd"""
        self.cnx.database = "ocr_p5"

    def bdd_tables(self):
        """Method to tables in bdd"""
        sql_cat_table = "CREATE TABLE IF NOT EXISTS categories" \
                        "(id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY," \
                        "name_cat VARCHAR(50) UNIQUE NOT NULL," \
                        "INDEX(name_cat))"

        sql_products_table = "CREATE TABLE IF NOT EXISTS products" \
                             "(id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY," \
                             "name_cat VARCHAR(50) NOT NULL," \
                             "name_product VARCHAR(500) NOT NULL," \
                             "score_product VARCHAR(1) NOT NULL," \
                             "url_product VARCHAR(5000) UNIQUE NOT NULL," \
                             "store_product VARCHAR(255) NOT NULL," \
                             "INDEX(name_cat)," \
                             "CONSTRAINT FOREIGN KEY(name_cat) REFERENCES categories(name_cat))"

        sql_user_sav = "CREATE TABLE IF NOT EXISTS user_save" \
                       "(id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY," \
                       "id_product INT(11) NOT NULL," \
                       "id_sub INT(11) NOT NULL," \
                       "INDEX(id_product)," \
                       "CONSTRAINT FOREIGN KEY(id_product) REFERENCES products(id))"

        self.cursor.execute(sql_cat_table)
        self.cursor.execute(sql_products_table)
        self.cursor.execute(sql_user_sav)
        self.cnx.commit()

    def apidata_to_bdd(self):
        """Method to send data from Api to bdd"""
        data_cat = []
        data_prod = []
        sql_cat = "INSERT IGNORE INTO categories (name_cat) VALUES (%s)"
        sql_products = "INSERT IGNORE INTO products" \
                       "(name_product, score_product, url_product, store_product, name_cat)" \
                       " VALUES (%s, %s, %s, %s, %s)"

        for cat in CATEGORIES:
            data_cat.append([cat])

        for products in self.products_data:
            data_prod.append(products.screen_prod())

        self.cursor.executemany(sql_cat, data_cat)
        self.cursor.executemany(sql_products, data_prod)
        self.cnx.commit()

    def get_cat(self, choice):
        """Retrieving categories and displaying them on the screen and choose one"""
        self.cat_choice = choice
        sql = "SELECT * FROM categories"
        self.cursor.fetchone()
        self.cursor.execute(sql)
        # for table_cat in cursor:
        # self.cat_list.append(table_cat[1])
        self.cat_choice = str(choice)
        self.cat_choice = (self.cat_choice,)
        print(self.cat_choice)

    def get_product(self, choice):
        """Retrieving products and displaying them on the screen and choose one"""
        self.cat_choice = choice
        choice = (choice,)
        sql = "SELECT * FROM products WHERE name_cat=%s"
        self.cursor.fetchall()
        self.cursor.execute(sql, choice)

        for table_prod in self.cursor:
            print("ID :", table_prod[0],
                  "/ Product :", table_prod[2],
                  "/ Nutriscore :", table_prod[3],
                  "/ URL :", table_prod[4],
                  "/ Store :", table_prod[5])
        self.product_choice = input("\nChoose a product by id number : ")
        self.product_choice = int(self.product_choice)
        self.product_choice = (self.product_choice,)


    def save_product(self):
        """Method save a product"""
        print(self.product_choice)
        sql = "INSERT INTO user_save (id_product) VALUES (%s)"
        self.cursor.fetchall()
        self.cursor.execute(sql, self.product_choice)
        self.cnx.commit()

    def get_saved(self):
        """Method to get the saved products"""
        sql = "SELECT name_product, score_product, url_product, store_product FROM products" \
              " INNER JOIN user_save ON products.id = user_save.id_product"
        # A revoir
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        print("Here are the saved products :")
        for i in data:
            print("Product :", i[0],
                  "/ Nutriscore :", i[1],
                  "/ URL :", i[2],
                  "/ Store :", i[3])

    def substitute(self):
        """Offer a substitute for the chosen product"""
        self.cat_choice = (self.cat_choice,)
        sql = "SELECT * FROM products WHERE id=%s"
        self.cursor.execute(sql, self.product_choice)
        user_product = self.cursor.fetchone()
        print("You have chosen",
              str(user_product[2]).upper(),
              "with a score of",
              str(user_product[3]).upper(),
              "of nutriscore")
        sql = "SELECT * FROM products WHERE score_product='a' AND name_cat=%s ORDER BY RAND()"
        self.cursor.execute(sql, self.cat_choice)
        comp_substitue = self.cursor.fetchone()
        print("We recommend :",
              str(comp_substitue[2]),
              "from nutriscore",
              str(comp_substitue[3]).upper(),
              "buyable in stores :",
              str(comp_substitue[5]),
              "and available online at this URL :",
              str(comp_substitue[4]))
        self.user_save = input("\nDo you want to save your product ? ")

test = Bdd()
test.bdd_exist()
test.load_data()