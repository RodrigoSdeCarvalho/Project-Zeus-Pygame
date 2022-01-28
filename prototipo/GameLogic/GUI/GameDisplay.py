import pygame

class GameDisplay:
    def __init__(self):
        self.__width = 800
        self.__height = 600
        self.display = pygame.display.set_mode((self.__width, self.__height)) #Don't make this a private attribute
        #self.__display_background = pygame.transform.scale(pygame.image.load('prototipo\Images\menu_background.jpg'), (self.__width, self.__height))

        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, height):
            self.__height = height

        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, width):
            self.__width = width

        #@property
        #def display(self):
        #    return self.__display

        #@display.setter
        #def display(self, display):
        #    self.__display = display
