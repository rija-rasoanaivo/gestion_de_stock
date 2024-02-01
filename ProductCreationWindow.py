import pygame
from pygame.locals import *
from Gestionnaire import Gestionnaire

# Initialisation de Pygame
pygame.init()

class ProductCreationWindow:
    def __init__(self):
        self.screen = pygame.display.set_mode((400, 300))
        pygame.display.set_caption("Création de produit")
        self.clock = pygame.time.Clock()
        self.gestionnaire = Gestionnaire()

        self.font = pygame.font.SysFont(None, 24)
        self.input_fields = {
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

            # Afficher les champs de saisie et les boutons
            for i, (label, value) in enumerate(self.input_fields.items()):
                text_surface = self.font.render(label + ": " + value, True, (0, 0, 0))
                self.screen.blit(text_surface, (50, 50 + i * 30))

            pygame.display.update()
            self.clock.tick(30)

            # Gérer les événements
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == MOUSEBUTTONDOWN:
                    self.handle_mouse_click(pygame.mouse.get_pos())
                elif event.type == KEYDOWN:
                    self.handle_key_press(event.key)

    def handle_mouse_click(self, pos):
        # Vérifier si le clic de souris se trouve dans un champ de saisie
        for i, (label, value) in enumerate(self.input_fields.items()):
            if 50 <= pos[0] <= 250 and 50 + i * 30 <= pos[1] <= 50 + (i + 1) * 30:
                self.active_field = label
                break
        else:
            self.active_field = None

    def handle_key_press(self, key):
        if self.active_field:
            # Gérer la saisie dans le champ de saisie actif
            if key == K_BACKSPACE:
                self.input_fields[self.active_field] = self.input_fields[self.active_field][:-1]
            elif key == K_RETURN:
                self.active_field = None
            else:
                # Vérifier si la touche Majuscule est enfoncée
                shift_pressed = pygame.key.get_pressed()[K_LSHIFT] or pygame.key.get_pressed()[K_RSHIFT]
                # Utiliser la table de correspondance de Pygame pour obtenir le caractère correspondant à la touche
                char = pygame.key.name(key)
                if len(char) == 1:
                    # Si la longueur du caractère est égale à 1, cela signifie que la touche est une lettre
                    # et nous devons vérifier si Majuscule est enfoncée pour obtenir la majuscule correspondante
                    if shift_pressed:
                        char = char.upper()
                    self.input_fields[self.active_field] += char
                elif key == K_SPACE:
                    # Si la touche est la touche d'espace, ajouter un espace à la saisie
                    self.input_fields[self.active_field] += " "
            # Si le champ de saisie actif est None, cela signifie que l'utilisateur a appuyé sur Entrée,
            # nous pouvons donc créer le produit
            if self.active_field is None:
                self.create_product()

    def create_product(self):
        name = self.input_fields["Nom"]
        description = self.input_fields["Description"]
        price = self.input_fields["Prix"]
        quantity = self.input_fields["Quantité"]
        id_category = self.input_fields["ID de catégorie"]

        # Appel de la méthode createProduct de la classe Gestionnaire pour ajouter le produit à la base de données
        self.gestionnaire.createProduct(name, description, price, quantity, id_category)

# # Créer une instance de ProductCreationWindow
# window = ProductCreationWindow()

# # Lancer la boucle principale
# window.run()
