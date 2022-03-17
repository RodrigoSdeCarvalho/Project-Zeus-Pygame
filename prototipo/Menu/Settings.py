import pygame
from Menu.Button import Button
from Difficulty.Difficulty import Difficulty

class Settings(Button):
    def __init__(self, text: str, width: int, height: int, x: int, y: int, elevation: int, topColor: str, bottomColor: str, surface):
        super().__init__(text, width, height, x, y, elevation, topColor, bottomColor)
        #self.screen = pygame.display.get_surface()
        self.window = surface
        self.__texts = ['Easy Mode', 'Hard Mode']
        self.__current_text = 0

    @property
    def texts(self):
        return self.__texts

    @property
    def current_text(self):
        return self.__current_text

    @current_text.setter
    def current_text(self, current_text):
        self.__current_text = current_text

    def onClick(self):
        self.current_text += 1
        Difficulty().increase()
        if self.current_text >= len(self.texts):
            self.current_text = 0
            Difficulty.reset()
        
        self.text = self.texts[self.current_text]
