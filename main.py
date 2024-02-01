# from Product import Product
# from Category import Category
from Gestionnaire import Gestionnaire

# product_manager = Product()
# product_manager.create("Viande grillé", "Veau et Agneau", 8, 2, 3)
# print(product_manager.read())
# product_manager.update(5, 'Viande pour Kebab','Veau agneau et boeuf', 7, 2, 3)
# print(product_manager.find(2))

# modif_category = Category()
# modif_category.update(3, 'Boucherie')
# modif_category.create('Produit ménager')
# modif_category.delete(6)

gestionnaire = Gestionnaire
gestionnaire.createProduct(name='Epinard', description='Bio', price=6, quantity=6, id_category=2)