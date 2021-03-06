"""V.2.0 - File to create the products object and its methods"""


class Products:
    """Class to create the product object and its methods"""

    def __init__(self, cat, apidata):
        self.product_name = apidata[0]
        self.product_score = apidata[1]
        self.product_url = apidata[2]
        self.product_store = apidata[3]
        self.product_cat = cat
        self.conv = ()

    def conv_prod(self):
        """Method to convert in tuple"""
        self.conv = (self.product_name, self.product_score, self.product_url, self.product_store,)

    def screen_prod(self):
        """Method to screen product"""
        return [self.product_name, self.product_score, self.product_url, self.product_store, self.product_cat]
