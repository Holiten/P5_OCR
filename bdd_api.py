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


class BddApi():
    """
    Create bdd_api object to use data from Open food Fact API, create SQL BDD, create SQL Tables,
    add data from api to bdd.
    """

    def __init__(self):
        self.product_data = []

    def api_temp(self):
        """
        Request Open food Fact API into variable with json and fill the empty list
        """
        print("Loading Open Food Fact API Data...")
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
                        url_product = products.get('url', 'Non renseigné')
                        store_product = products.get('stores', 'Non renseigné')

                        if name_product not in ["", "NULL"] and score_product not in["", "N"]:
                            self.product_data.append([name_cat, name_product, score_product, url_product, store_product])

        print("The data has been loaded successfully")
    @staticmethod
    def create_db():
        """
        Create a bdd named 'open_food_fact'
        """

        cnx = mysql.connector.connect(**CONFIG_BDD)
        cursor = cnx.cursor()

        cursor.execute("DROP DATABASE IF EXISTS open_food_fact")

        try:
            cursor.execute(
                "CREATE DATABASE IF NOT EXISTS `open_food_fact` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci"
            )
        except cnx.Error as err:
            print(err)
            exit(1)

    @staticmethod
    def create_tables():
        """
        Create tables 'products / categorie / user_data' in the bdd create previously by 'create_db(self)'
        """

        cnx = mysql.connector.connect(**CONFIG_TABLES)
        cursor = cnx.cursor()
        drop = "DROP TABLE IF EXISTS products, categories, user_data"

        prod_table = "CREATE TABLE IF NOT EXISTS products (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name_cat VARCHAR(50) NOT NULL, name_product VARCHAR(500) NOT NULL, score_product VARCHAR(1) NOT NULL, url_product VARCHAR(5000) NOT NULL, store_product VARCHAR(255) NOT NULL, INDEX(name_cat), CONSTRAINT blabla FOREIGN KEY(name_cat) REFERENCES categories(name_cat))"

        cat_table = "CREATE TABLE IF NOT EXISTS categories(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name_cat VARCHAR(50) NOT NULL, INDEX(name_cat))"

        user_data = "CREATE TABLE IF NOT EXISTS user_data(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, id_product INT NOT NULL, INDEX(id_product), CONSTRAINT id_product FOREIGN KEY(id_product) REFERENCES products(id))"

        try:
            cursor.execute(drop)
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

        insert_cat = "INSERT INTO categories (id, name_cat) VALUES (NULL, 'Snacks'), (NULL, 'Fromages'),(NULL, 'Boissons')"

        try:
            cursor.execute(insert_cat)
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

        insert_prod = "INSERT INTO products(id, name_cat, name_product, score_product, url_product, store_product) VALUES (NULL, %s, %s, %s, %s, %s)"
        clean_prod = "DELETE FROM products WHERE name_product='NULL' OR name_product='' OR score_product='N'"

        try:
            cursor.executemany(insert_prod, data)
            cursor.execute(clean_prod)
            cnx.commit()
            cnx.close()

        except mysql.connector.Error as err:
            print(err)
            exit(1)
