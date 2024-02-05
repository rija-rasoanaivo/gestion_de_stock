import pygame
from pygame.locals import *
from Gestionnaire import Gestionnaire

pygame.init()

class UpdateProductWindow:
    def __init__(self):
        self.screen = pygame.display.set_mode((450, 300))
        pygame.display.set_caption("Modifier un produit")
        self.clock = pygame.time.Clock()
        self.gestionnaire = Gestionnaire()

        self.font = pygame.font.SysFont(None, 24)
        self.input_fields_search = {
            "Veuillez entrer l'Id du produit, puis ENTRER": ""
        }
        self.input_fields_update = {
            "Id" : "",
            "Nom": "",
            "Description": "",
            "Prix": "",
            "Quantité": "",
            "ID de catégorie": ""
        }
        self.active_field = None

    def run(self):
        running = True
        while running:
            self.screen.fill((255, 255, 255))
            
            for i, (label, value) in enumerate(self.input_fields_search.items()):
                text_surface_search = self.font.render(label + ": " + value, True, (0, 0, 0))
                self.screen.blit(text_surface_search, (20,10))

            for i, (label, value) in enumerate(self.input_fields_update.items()):
                text_surface_update = self.font.render(label + ": " + value, True, (0, 0, 0))
                self.screen.blit(text_surface_update, (20, 50 + i *30))

            # Met à jour l'affichage à l'intérieur de la boucle
            pygame.display.update()

            self.clock.tick(30)

            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.handle_mouse_click(event.pos)
                elif event.type == KEYDOWN:
                    self.handle_key_press(event.key)


    def handle_mouse_click(self, pos):
        for label, value in self.input_fields_search.items():
            text_width, text_height = self.font.size(label + ": " + value)
            input_field_rect = pygame.Rect(20, 10, text_width, text_height)
            if input_field_rect.collidepoint(pos):
                self.active_field = label
                break
        else:
            self.active_field = None
            # Si un ID de produit est sélectionné, afficher ses détails
            product_id = self.input_fields_search["Veuillez entrer l'Id du produit, puis ENTRER"]
            if product_id.isdigit():
                product_details = self.gestionnaire.readProduct(int(product_id))
                
            

    def handle_key_press(self, key):
        if self.active_field:
            if key == K_BACKSPACE:
                self.input_fields_search[self.active_field] = self.input_fields_search[self.active_field][:-1]
            elif key == K_RETURN:
                self.active_field = None
                # Si le champ de saisie actif est "Veuillez entrer l'Id du produit, puis ENTRER"
                # alors afficher les détails du produit correspondant à cet ID
                if self.input_fields_search["Veuillez entrer l'Id du produit, puis ENTRER"]:
                    product_id = self.input_fields_search["Veuillez entrer l'Id du produit, puis ENTRER"]
                    if product_id.isdigit():  # Vérifie si la valeur est un nombre
                        product_id = int(product_id)
                        product_details = self.gestionnaire.readProduct(product_id)
                        self.display_product(product_details)  # Afficher les détails du produit
            elif isinstance(key, int):  # Vérifie si la touche appuyée est un entier
                self.input_fields_search[self.active_field] = str(key)  # Convertit la touche en chaîne de caractères
            else:
                char = pygame.key.name(key)
                if len(char) == 1:
                    self.input_fields_search[self.active_field] += char
                elif key == K_SPACE:
                    self.input_fields_search[self.active_field] += " "

    def update_product(self):
        name = self.input_fields_update["Nom"]
        description = self.input_fields_update["Description"]
        price = self.input_fields_update["Prix"]
        quantity = self.input_fields_update["Quantité"]
        id_category = self.input_fields_update["ID de catégorie"]

        id = self.input_fields_search["Veuillez entrer l'Id du produit, puis ENTRER"]

        self.gestionnaire.updateProduct(name, description, price, quantity, id_category, id)

# window = UpdateProductWindow()
# window.run()
