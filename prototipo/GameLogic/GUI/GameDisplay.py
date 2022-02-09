import pygame

class GameDisplay:
    def __init__(self, clock):
        self.__width = 800
        self.__height = 600
        self.display = pygame.display.set_mode((self.__width, self.__height))
        self.clock = clock

    @property
    def width(self):
        return self.__width
    
    @property 
    def height(self):
        return self.__height
    
    def draw_image(self, image, x, y):
        img = pygame.image.load(image)
        self.display.blit(img, (x, y))

    def draw_scaled_image(self, image, scale_x, scale_y, x, y):
        img = pygame.image.load(image)
        img = pygame.transform.scale(img, (scale_x, scale_y))
        self.display.blit(img, (x, y))
