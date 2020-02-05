from constants import PAGE_NUMBER, CATEGORIES
import requests

class off_api():

    def __init__(self):
        self.product_data = []

    def api_temp(self):
        for page in range(0, PAGE_NUMBER):
            for cat_key, cat_value in CATEGORIES.items():
                if cat_key:
                    r_page = requests.get(cat_value + str(page + 1) + '.json')
                    r_page_json = r_page.json()
                    products_by_page = r_page_json[u'products']

                    # with open('products.json', 'w') as fp:
                    # json.dump(r_page_json, fp, indent=5)

                    for products in products_by_page:

                        cat_name = cat_key
                        name_product = products.get('product_name_fr', 'NO_DATA') # Evitez le try except


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
