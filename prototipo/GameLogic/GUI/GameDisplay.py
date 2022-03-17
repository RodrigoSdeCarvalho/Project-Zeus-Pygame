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

    def write_on_display(self, text, size, pos, color = (0, 0, 0)):
        largeText = pygame.font.Font('freesansbold.ttf', size)
        TextSurf = largeText.render(text, True, color)
        TextRect = TextSurf.get_rect()
        TextRect.center = ((pos[0], pos[1]))
        self.display.blit(TextSurf, TextRect)
