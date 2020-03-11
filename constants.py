"""Constants file"""

CATEGORIES = {'Yaourts': 'https://fr.openfoodfacts.org/categorie/yaourts/',
              'Fromages': 'https://fr.openfoodfacts.org/categorie/fromages/',
              'Soupes': 'https://fr.openfoodfacts.org/categorie/soupes/'}



"""Get the size of a page"""
# PAGE_SIZE = url_r_json['page_size']

"""Get the number of products"""
# PRODUCT_NUMBER = url_r_json['count']

"""Get the number of pages (((PRODUCT_NUMBER/PAGE_SIZE)+1)round)"""
PAGE_NUMBER = 5

"""SQL connection parameter"""
USER_NAME = 'root'
USER_PASSWORD = ''
USER_HOST = 'localhost'
DB_NAME = "ocr_p5"
PASSWORD_TYPE = 'mysql_native_password'

"""BDD SQL configuration parameter"""
CONFIG_BDD = {'user' : USER_NAME,
              'password' : USER_PASSWORD,
              'host' : USER_HOST,
              'auth_plugin' : PASSWORD_TYPE
              }
"""BDD Tables SQL configuration parameter"""
CONFIG_TABLES = {'user' : USER_NAME,
                 'password' : USER_PASSWORD,
                 'host' : USER_HOST,
                 'database' : DB_NAME,
                 'auth_plugin' : PASSWORD_TYPE
                 }

CAT_1 = "Soupes"
CAT_2 = "Fromages"
CAT_3 = "Yaourts"
