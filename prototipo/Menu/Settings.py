import pygame
from Menu.Button import Button

class Settings(Button):
    def __init__(self, text: str, width: int, height: int, x: int, y: int, elevation: int, topColor: str, bottomColor: str, surface):
        super().__init__(text, width, height, x, y, elevation, topColor, bottomColor)
        #self.screen = pygame.display.get_surface()
        self.window = surface
        self.texts = ['Easy Mode', 'Hard Mode']
        self.current_text = 0

    def onClick(self):
        self.current_text += 1
        if self.current_text >= len(self.texts):
            self.current_text = 0
        
        self.text = self.texts[self.current_text]

