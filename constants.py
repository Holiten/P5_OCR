import requests
import json
import mysql.connector

# Catégories choisies depuis Open Food Fact (Viandes, Fromages, Bieres)
CATEGORIES = {'Snacks': 'https://fr.openfoodfacts.org/categorie/snacks/',
              'Fromages': 'https://fr.openfoodfacts.org/categorie/fromages/',
              'Boissons': 'https://fr.openfoodfacts.org/categorie/boissons/'}

# Convertion URL de CATEGORIES en JSON - Récupération des données Open Food Fact
for cat_key, cat_value in CATEGORIES.items():
    if cat_key:
        url_r = requests.get(cat_value + '1.json')
        url_r_json = url_r.json()

# Enregistrement vers un fichier JSON pour vérification
with open('cat_verif.json', 'w') as ct:
    json.dump(url_r_json, ct, indent=5)

# RECUPERATION DE LA TAILLE DE LA PAGE (20) :
PAGE_SIZE = url_r_json['page_size']
# TEST OK : print(PAGE_SIZE)

# RECUPERATION DU NOMBRE DE PRODUCTS (2347) :
PRODUCT_NUMBER = url_r_json['count']
# TEST OK : print(PRODUCT_NUMBER)

# RECUPERATION DU NOMBRE DE PAGE VIA PRODUCT_NUMBER / PAGE_SIZE (2347 / 20) = 117.35 + 1 (arrondi) = 118
# TROP DE DONNEES : PAGE_NUMBER = round((PRODUCT_NUMBER / PAGE_SIZE) + 1)
PAGE_NUMBER = 5
# TEST OK : print(PAGE_NUMBER)

# PARAMETRE DE CONNECTION SQL :
USER_NAME = 'root'
USER_PASSWORD = ''
USER_HOST = 'localhost'
DB_NAME = 'open_food_fact'
PASSWORD_TYPE = 'mysql_native_password'

CONFIG_BDD = {'user' : USER_NAME,
              'password' : USER_PASSWORD,
              'host' : USER_HOST,
              'auth_plugin' : PASSWORD_TYPE
              }

CONFIG_TABLES = {'user' : USER_NAME,
                 'password' : USER_PASSWORD,
                 'host' : USER_HOST,
                 'database' : DB_NAME,
                 'auth_plugin' : PASSWORD_TYPE
                 }

