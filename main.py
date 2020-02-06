from bdd_api import bdd_api
from constants import USER_NAME, USER_PASSWORD, USER_HOST, DB_NAME, PASSWORD_TYPE, CONFIG_BDD

bdd = bdd_api()

bdd.api_temp()
bdd.create_db()
bdd.create_tables()

bdd.send_cat_to_db()
bdd.send_product_to_db()

bdd.erase_void()