import pygame
from ProductCreationWindow import ProductCreationWindow

class Graphic:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400, 300))
        pygame.display.set_caption("Interface Graphique")
        self.font = pygame.font.SysFont(None, 24)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.handle_click(event.pos)

            self.screen.fill((255, 255, 255))
            self.draw_interface()
            pygame.display.flip()

        pygame.quit()

    def draw_interface(self):
        # Dessiner les éléments de l'interface graphique, y compris le texte "1. Créer un produit"
        text_surface = self.font.render('1. Créer un produit', True, (0, 0, 0))
        self.screen.blit(text_surface, (50, 50))

    def handle_click(self, pos):
        # Vérifier si le clic de souris se trouve dans la zone de texte "1. Créer un produit"
        if 50 <= pos[0] <= 50 + 200 and 50 <= pos[1] <= 50 + 30:
            window = ProductCreationWindow()
            # Lancer la boucle principale
            window.run()

    # def set_main(self, main_instance):
        
    #     self.main = main_instance # Stocker une référence à l'instance de la classe Main


# graphic = Graphic()
# graphic.run()
        

