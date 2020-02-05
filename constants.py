import requests
import json
import mysql.connector

# Catégories choisies depuis Open Food Fact (Viandes, Fromages, Bieres)
CATEGORIES = {'Viandes': 'https://fr.openfoodfacts.org/categorie/viandes/',
              'Fromages': 'https://fr.openfoodfacts.org/categorie/fromages/',
              'Bieres': 'https://fr.openfoodfacts.org/categorie/bieres/'}

"""
CAT_1 = 'Viandes'
CAT_2 = 'Fromages'
CAT_3 = 'Bieres'
"""

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
PAGE_NUMBER = 3
# TEST OK : print(PAGE_NUMBER)

# PARAMETRE DE CONNECTION SQL :
USER_NAME = 'root'
USER_PASSWORD = ''
USER_HOST = 'localhost'
DB_NAME = 'OPENFOODFACT'
PASSWORD_TYPE = 'mysql_native_password'
