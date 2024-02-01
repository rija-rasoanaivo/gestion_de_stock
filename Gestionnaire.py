from Product import Product
from Category import Category

class Gestionnaire:
    def __init__(self):
        self.product = Product()
        self.category = Category()

    def createProduct(self, name, description, price, quantity, id_category):
        self.product.create(name, description, price, quantity, id_category)

    def readProduct(self):
        return self.product.read()
    
    def updateProduct(self, id, name, description, price, quantity, id_category):
        self.product.update(name, description, price, quantity, id_category, id)

    def deleteProduct(self, id):
        self.product.delete(id)

    def createCategory(self, name):
        self.category.create(name)

    def readCategory(self):
        return self.category.read()

    def updateCategory(self, id, name):
        self.category.update(id, name)

    def deleteCategory(self, id):
        self.category.delete(id)