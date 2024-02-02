import pygame
from pygame.locals import *
from Gestionnaire import Gestionnaire

pygame.init()

class ReadProductWindow:
    def __init__(self):
        self.screen = pygame.display.set_mode((1000, 300))
        pygame.display.set_caption("Affichage des produits")
        self.clock = pygame.time.Clock()
        self.gestionnaire = Gestionnaire()

        self.font = pygame.font.SysFont(None, 20)

        # Positions initiales pour chaque colonne
        self.column_positions = {
            "Id": (50, 50),
            "Nom": (100, 50),
            "Description": (300, 50),
            "Prix": (650, 50),
            "Quantité": (750, 50),
            "ID de catégorie": (850, 50)
        }
    
    def run(self):
        running = True
        while running:
            self.screen.fill((255, 255, 255))

            # Lire les produits depuis le gestionnaire
            products = self.gestionnaire.readProduct()

            # Début des produits en dessous de chaque colonne
            y_offset = 20

            # Afficher les informations de chaque produit par colonne
            for product in products:
                # Réinitialiser la position horizontale pour chaque produit
                x = 50
                # Afficher les informations de chaque colonne
                for column, position in self.column_positions.items() :
                    info_text = f"{column }: {product[column]}"
                    text_surface = self.font.render(info_text, True, (0, 0, 0))
                    self.screen.blit(text_surface, (position[0] , y_offset))
                    # Augmenter la position horizontale pour la prochaine colonne
                    x += 100
                # Augmenter la position verticale pour le prochain produit
                y_offset += 20

            pygame.display.update()
            self.clock.tick(30)

            # Gestion des événements
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False  # Mettre fin à la boucle lorsque la fenêtre est fermée

# window = ReadProductWindow()
# window.run()
