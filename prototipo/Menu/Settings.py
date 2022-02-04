import pygame
from Menu.Button import Button

class Settings(Button):
    def __init__(self, text: str, width: int, height: int, x: int, y: int, elevation: int, topColor: str, bottomColor: str):
        super().__init__(text, width, height, x, y, elevation, topColor, bottomColor)
        self.screen = pygame.display.get_surface()

    def onClick(self):
        self.screen.fill('#ffffff')