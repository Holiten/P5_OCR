from constants import PAGE_NUMBER, CATEGORIES, CONFIG_TABLES, CONFIG_BDD
import requests
import json
import mysql.connector

class bdd_api():

    def __init__(self):
        self.product_data = []

    def api_temp(self):
        print("Veuillez patientez pendant le chargement...")
        for page in range(0, PAGE_NUMBER):
            for cat_key, cat_value in CATEGORIES.items():
                if cat_key:
                    r_page = requests.get(cat_value + str(page + 1) + '.json')
                    r_page_json = r_page.json()
                    products_by_page = r_page_json[u'products']

                    with open('products.json', 'w') as fp:
                        json.dump(r_page_json, fp, indent=5)

                    for products in products_by_page:

                        name_cat = cat_key
                        name_product = products.get('product_name_fr', 'NULL')
                        score_product = products.get('nutriscore_grade', 'NULL')
                        url_product = products.get('url', 'Non renseigné')
                        store_product = products.get('store', 'Non renseigné')

                        self.product_data.append([name_cat, name_product, score_product, url_product, store_product])
        print("Merci d'avoir patienter !")

    def create_db(self):

        cnx = mysql.connector.connect(**CONFIG_BDD)
        cursor = cnx.cursor()

        cursor.execute("DROP DATABASE IF EXISTS open_food_fact")

        try :
            cursor.execute(
                "CREATE DATABASE IF NOT EXISTS `open_food_fact` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci"
            )
        except cnx.Error as err:
            print("Erreur lors de la création de la base de donnée")
            exit(1)

    def create_tables(self):

        cnx = mysql.connector.connect(**CONFIG_TABLES)
        cursor = cnx.cursor()
        drop = "DROP TABLE IF EXISTS products, categories "

        prod_table = "CREATE TABLE IF NOT EXISTS products (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name_cat VARCHAR(50) NOT NULL, name_product VARCHAR(500) NOT NULL, score_product VARCHAR(1) NOT NULL, url_product VARCHAR(5000) NOT NULL, store_product VARCHAR(255) NOT NULL, INDEX(name_cat), CONSTRAINT blabla FOREIGN KEY(name_cat) REFERENCES categories(name_cat))"

        cat_table = "CREATE TABLE IF NOT EXISTS categories(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name_cat VARCHAR(50) NOT NULL, INDEX(name_cat))"

        try :
            cursor.execute(drop)
            cursor.execute(cat_table)
            cursor.execute(prod_table)
        except mysql.connector.Error as err :
            print(err)
            exit(1)

        cnx.close()

    def send_cat_to_db(self):

        cnx = mysql.connector.connect(**CONFIG_TABLES)
        cursor = cnx.cursor()

        insert_cat = "INSERT INTO categories (id, name_cat) VALUES (NULL, 'Snacks'), (NULL, 'Fromages'),(NULL, 'Boissons')"

        cursor.execute(insert_cat)
        cnx.commit()
        cnx.close()

    def send_product_to_db(self):
        data = self.product_data[:]

        cnx = mysql.connector.connect(**CONFIG_TABLES)
        cursor = cnx.cursor()

        insert_prod = "INSERT INTO products(id, name_cat, name_product, score_product, url_product, store_product) VALUES (NULL, %s, %s, %s, %s, %s)"

        cursor.executemany(insert_prod, data)
        cnx.commit()
        cnx.close()

    def erase_void(self):
        cnx = mysql.connector.connect(**CONFIG_TABLES)
        cursor = cnx.cursor()

        delete_score_null = "DELETE FROM products WHERE score_product='N'"
        delete_name_null = "DELETE FROM products WHERE name_product='NULL' AND name_product=''"

        cursor.execute(delete_score_null)
        cursor.execute(delete_name_null)
        cnx.commit()
        cnx.close