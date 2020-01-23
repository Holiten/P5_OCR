import requests
import json
import mysql.connector
from constants import PAGE_NUMBER
from constants import CATEGORIES
from constants import USER_NAME, USER_PASSWORD, USER_HOST, DB_NAME, PASSWORD_TYPE

db_connection = mysql.connector.connect(user=USER_NAME,
                                        password=USER_PASSWORD,
                                        host=USER_HOST,
                                        database=DB_NAME,
                                        auth_plugin=PASSWORD_TYPE)

class Products:

    def __init__(self):
        self.product_data = []

    def off_to_me(self):
        for page in range(0, PAGE_NUMBER):
            for cat_key, cat_value in CATEGORIES.items():
                if cat_key:
                    r_page = requests.get(cat_value + str(page + 1) + '.json')
                    r_page_json = r_page.json()
                    products_by_page = r_page_json[u'products']

                    with open('products.json', 'w') as fp:
                        json.dump(r_page_json, fp, indent=5)

                    for products in products_by_page:

                        cat_name = cat_key

                        try:
                            name_product = products['product_name']
                        except KeyError:
                            name_product = 'NO_DATA'

                        try:
                            score_product = products['nutriscore_grade']
                        except KeyError:
                            score_product = 'X'

                        try:
                            url_product = products['url']
                        except KeyError:
                            url_product = 'NO_DATA'

                        try:
                            store_product = products['stores']
                        except KeyError:
                            store_product = 'NO_DATA'

                        self.product_data.append([cat_name, name_product, score_product, url_product, store_product])


    def send_to_bdd(self):
        data = self.product_data[:]
        cursor = db_connection.cursor()
        cursor.execute("INSERT INTO categories (id_cat, cat_name) "
                 "VALUES (NULL, 'Viandes'), "
                 "(NULL, 'Fromages'), "
                 "(NULL, 'Bieres')")
        cursor.executemany("INSERT INTO products (id_product, cat_name, name_product, score_product, url_product, store_product) "
                           "VALUES (NULL, %s, %s, %s, %s, %s)", data)

        db_connection.commit()
        db_connection.close()

test = Products()
test.off_to_me()
test.send_to_bdd()


