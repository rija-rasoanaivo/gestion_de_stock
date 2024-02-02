# from Gestionnaire import Gestionnaire
from Graphic import Graphic

class Main:
    def __init__(self):
        # self.gestionnaire = Gestionnaire()
        self.graphic = Graphic()
        # self.graphic.set_main(self)  
        self.graphic.run()
        
    # def menu(self):
    #     print("1. Creer un produit ")
    #     print("2. Lire les produits ")
    #     print("3. Modifier un produit ")
    #     print("4. Supprimer un produit ")
    #     print("5. Rechercher un produit ")
    #     print("6. Creer une categorie ")
    #     print("7. Lire les categories ")
    #     print("8. Modifier une categorie ")
    #     print("9. Supprimer une categorie ")
    #     choice = input("Que voulez vous faire ? ")

    #     if choice == "1" or choice.lower() == "creer un produit":
    #         self.createProduct()
    #     elif choice == "2" or choice.lower() == "lire les produits":
    #         self.readProduct()
    #     else:
    #         print("Commande invalide")
    #         time.sleep(1)
    #         self.menu()

    # def createProduct(self):
    #     name = input("Nom : ")
    #     description = input("Description du produit : ")
    #     price = input("Prix : ")
    #     quantity =  input("Quantité : ")
    #     id_category = input("Veuillez assigner l'ID du produit : ")
    #     self.gestionnaire.createProduct(name, description, price, quantity, id_category)

    # def readProduct(self):
    #     for product in self.gestionnaire.readProduct():
    #         print("---------------Produit---------------")
    #         print(f"ID : {product[0]}")
    #         print(f"Nom : {product[1]}")
    #         print(f"Description : {product[2]}")
    #         print(f"Prix : {product[3]}")
    #         print(f"Quantité : {product[4]}")
    #         print(f"ID de la catégorie : {product[5]}")
    #         print("=====================================")
    #         time.sleep(1)
    #     self.menu()

Main()