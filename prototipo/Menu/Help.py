import pygame
from Menu.Button import Button

class Help(Button):
    def __init__(self, text: str, width: int, height: int, x: int, y: int, elevation: int, topColor: str, bottomColor: str, surface):
        super().__init__(text, width, height, x, y, elevation, topColor, bottomColor)
        self.screen = pygame.display.get_surface()
        self.__tutorial_background = pygame.transform.scale(pygame.image.load("prototipo/Images/tutorial_background.png"), (800, 600))
        self.window = surface

    @property
    def tutorial_background(self):
        return self.__tutorial_background

    def onClick(self):
        self.help_start()
        return False
    
    def help_start(self):
        help = True

        while help:
            self.window.display.blit(self.tutorial_background, (0, 0))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

