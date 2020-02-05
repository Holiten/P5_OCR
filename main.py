from bdd import bdd_sql
from constants import USER_NAME, USER_PASSWORD, USER_HOST, DB_NAME, PASSWORD_TYPE

bdd = bdd_sql()

bdd.connect_db()
