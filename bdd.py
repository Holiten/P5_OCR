"""
Version 1.4 :  Optimisation & Suppression function 'erase_void'
Version 1.3 : PEP convention
Version 1.2 : Modifications & optimisation
Version 1.1 : Pseudo-code
Version 1.0 : Initialisation
The following scripts manage the Open food fact's API and the database
"""

import requests
import mysql.connector
from constants import PAGE_NUMBER, CATEGORIES, CONFIG_BDD, CONFIG_TABLES

class Bdd():
    """
    Create BddApi object to use data from Open food Fact API, create SQL BDD, create SQL Tables,
    add data from api to bdd.
    """

    def __init__(self):
        self.product_data = []
        self.cat_list = []
        self.cat_choice = ""
        self.product_choice = 0
        self.user_save = 0

    def api_temp(self):
        """
        Request Open food Fact API into variable with json and fill the empty list
        """

        for cat_key, cat_value in CATEGORIES.items():
            if cat_key:
                url_r = requests.get(cat_value + "1.json")
                url_r_json = url_r.json()

        print("Loading Open Food Fact API Data... \n")
        for page in range(0, PAGE_NUMBER+1):
            for cat_key, cat_value in CATEGORIES.items():
                if cat_key:
                    r_page = requests.get(cat_value + str(page + 1) + '.json')
                    r_page_json = r_page.json()
                    products_by_page = r_page_json[u'products']

                    for products in products_by_page:
                        name_cat = cat_key
                        name_product = products.get('product_name_fr', 'NULL')
                        score_product = products.get('nutriscore_grade', 'NULL')
                        url_product = products.get('url', 'No data')
                        store_product = products.get('stores', 'No data')

                        if name_product not in ["", "NULL"] \
                                and score_product not in ["", "N"] \
                                and store_product not in ["", "No data"]:
                            self.product_data.append([name_cat,
                                                      name_product,
                                                      score_product,
                                                      url_product,
                                                      store_product])

        print("The data has been loaded successfully")

    @staticmethod
    def create_db():
        """
        Create a bdd named 'open_food_fact'
        """

        cnx = mysql.connector.connect(**CONFIG_BDD)
        cursor = cnx.cursor()

        try:
            cursor.execute(
                "CREATE DATABASE IF NOT EXISTS `open_food_fact` "
                "DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci"
            )
        except cnx.Error as err:
            print(err)
            exit(1)

    @staticmethod
    def create_tables():
        """
        Create tables 'products / categorie / user_data'
        in the bdd create previously by 'create_db(self)'
        """

        cnx = mysql.connector.connect(**CONFIG_TABLES)
        cursor = cnx.cursor()

        prod_table = "CREATE TABLE IF NOT EXISTS products " \
                     "(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY," \
                     " name_cat VARCHAR(50) NOT NULL," \
                     " name_product VARCHAR(500) NOT NULL," \
                     " score_product VARCHAR(1) NOT NULL," \
                     " url_product VARCHAR(5000) UNIQUE NOT NULL," \
                     " store_product VARCHAR(255) NOT NULL, INDEX(name_cat)," \
                     " CONSTRAINT blabla FOREIGN KEY(name_cat) REFERENCES categories(name_cat))"
        cat_table = "CREATE TABLE IF NOT EXISTS categories(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY," \
                    " name_cat VARCHAR(50) NOT NULL, INDEX(name_cat))"
        user_data = "CREATE TABLE IF NOT EXISTS user_data(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY," \
                    " id_product INT NOT NULL," \
                    " INDEX(id_product)," \
                    " CONSTRAINT id_product FOREIGN KEY(id_product) REFERENCES products(id))"

        try:
            cursor.execute(cat_table)
            cursor.execute(prod_table)
            cursor.execute(user_data)

        except mysql.connector.Error as err:
            print(err)
            exit(1)

        cnx.close()

    @staticmethod
    def send_cat_to_db():
        """
        Send data from list create with 'api_temp' to categories table
        """

        cnx = mysql.connector.connect(**CONFIG_TABLES)
        cursor = cnx.cursor()
        sql = "INSERT IGNORE INTO categories" \
              " (id, name_cat) VALUES (1, 'Yaourts'), (2, 'Fromages'),(3, 'Boissons')"
        try:
            cursor.execute(sql)
            cnx.commit()
            cnx.close()

        except mysql.connector.Error as err:
            print(err)
            exit(1)

    def send_product_to_db(self):
        """
        Send data from list create with 'api_temp' to products table
        """
        data = self.product_data[:]

        cnx = mysql.connector.connect(**CONFIG_TABLES)
        cursor = cnx.cursor()
        sql = "INSERT IGNORE INTO products(name_cat, name_product, score_product, url_product, store_product)" \
              " VALUES (%s, %s, %s, %s, %s)"
        clean_prod = "DELETE FROM products WHERE name_product='NULL' OR name_product='' OR score_product='N'"

        try:
            cursor.executemany(sql, data)
            cnx.commit()
            cursor.execute(clean_prod)
            cnx.commit()
            cnx.close()

        except mysql.connector.Error as err:
            print(err)
            exit(1)

        print("The bdd was successfully created or loaded")

    def get_cat(self, choice):
        """
        Retrieving categories and displaying them on the screen and choose one
        """
        self.cat_choice = choice
        cnx = mysql.connector.connect(**CONFIG_TABLES)
        cursor = cnx.cursor()
        sql = "SELECT * FROM categories"
        cursor.fetchone()
        cursor.execute(sql)
        # for table_cat in cursor:
            # self.cat_list.append(table_cat[1])
        self.cat_choice = str(choice)
        self.cat_choice = (self.cat_choice,)


    def get_product(self, choice):
        """
        Retrieving products and displaying them on the screen and choose one
        """
        self.cat_choice = choice
        choice = (choice,)
        cnx = mysql.connector.connect(**CONFIG_TABLES)
        cursor = cnx.cursor()
        sql = "SELECT * FROM products WHERE name_cat=%s"
        cursor.execute(sql, choice)
        print(cursor)
        for table_prod in cursor:
            print("ID :", table_prod[0],
                  "/ Product :", table_prod[2],
                  "/ Nutriscore :", table_prod[3],
                  "/ URL :", table_prod[4],
                  "/ Store :", table_prod[5])
        self.product_choice = input("\nChoose a product by id number : ")
        self.product_choice = int(self.product_choice)
        self.product_choice = (self.product_choice,)

    def substitute(self):
        """
        Offer a substitute for the chosen product
        """
        self.cat_choice = (self.cat_choice,)
        cnx = mysql.connector.connect(**CONFIG_TABLES)
        cursor = cnx.cursor()
        sql = "SELECT * FROM products WHERE id=%s"
        cursor.execute(sql, self.product_choice)
        user_product = cursor.fetchone()
        print("You have chosen",
              str(user_product[2]).upper(),
              "with a score of",
              str(user_product[3]).upper(),
              "of nutriscore")
        sql = "SELECT * FROM products WHERE score_product='a' AND name_cat=%s ORDER BY RAND()"
        cursor.execute(sql, self.cat_choice)
        comp_substitue = cursor.fetchone()
        print("We recommend :",
              str(comp_substitue[2]),
              "from nutriscore",
              str(comp_substitue[3]).upper(),
              "buyable in stores :",
              str(comp_substitue[5]),
              "and available online at this URL :",
              str(comp_substitue[4]))
        self.user_save = input("\nDo you want to save your product ? ")

    def save_product(self):
        """
        Save product choosen
        """
        print(self.product_choice)
        cnx = mysql.connector.connect(**CONFIG_TABLES)
        cursor = cnx.cursor()
        sql = "INSERT INTO user_data (id_product) VALUES (%s)"
        cursor.execute(sql, self.product_choice)
        cnx.commit()

    def get_save_product(self):
        """
        Get product choosen
        """
        cnx = mysql.connector.connect(**CONFIG_TABLES)
        cursor = cnx.cursor()
        sql = "SELECT name_product, score_product, url_product, store_product FROM products" \
              " INNER JOIN user_data ON products.id = user_data.id_product"
        cursor.execute(sql)
        data = cursor.fetchall()
        print("Here are the saved products :")
        for i in data:
            print("Product :", i[0],
            "/ Nutriscore :", i[1],
            "/ URL :", i[2],
            "/ Store :", i[3])
