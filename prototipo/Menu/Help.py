import pygame
from Menu.Button import Button

class Help(Button):
    def __init__(self, text: str, width: int, height: int, x: int, y: int, elevation: int, topColor: str, bottomColor: str, surface):
        super().__init__(text, width, height, x, y, elevation, topColor, bottomColor)
        self.screen = pygame.display.get_surface()
        self.window = surface

    def onClick(self):
        print('Not implemented')
