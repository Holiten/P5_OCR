"""V 2.0 - File to create the categories object and its methods"""

class Categories:
    """Class to create the product object and its methods"""

    def __init__(self, name):
        self.name = name

    def conv_cat(self):
        """Method to convert in tuple"""
        return (self.name,)

    def screen_cat(self):
        """Method to screen categories"""
        return [self.name]
