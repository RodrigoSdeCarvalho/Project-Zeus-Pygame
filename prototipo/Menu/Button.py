from abc import ABC, abstractmethod
import pygame

#Alterar encapsulamento dos atributos
#Mudar cursor do mouse ao dar hover sobre botao
class Button(ABC):
    def __init__(self, text: str, width: int, height: int, x: int, y: int, elevation: int, topColor: str, bottomColor: str):
        #Initial state and position of the button
        self.__pressed = False
        self.__elevation = elevation
        self.__dynamic_elevation = elevation  #Used to generate a button with elevation
        self.__original_y_pos = y
        self.__original_x_pos = x
        self.__pos = (self.original_x_pos, self.original_y_pos)
        
        self.__width = width
        self.__height = height

        #Creates a rectangle which represents the top part of the button
        self.__top_rect = pygame.Rect(self.pos, (self.width, self.height))
        self.__top_color = topColor

        #Creates a rectangle which represents the bottom part of the button - this creates a feeling of depth
        self.__bottom_rect = pygame.Rect(self.pos, (self.width, self.height))
        self.__bottom_color = bottomColor
        
        #Rendering the text inside the button
        self.__text = text
        self.__font = pygame.font.SysFont('Montserrat', 27)
        self.__text_surf = self.font.render(self.text, True, '#FFFFFF')
        self.__text_rect = self.text_surf.get_rect(center = self.top_rect.center)

    @property
    def pressed(self):
        return self.__pressed

    @pressed.setter
    def pressed(self, pressed):
        self.__pressed = pressed

    @property
    def elevation(self):
        return self.__elevation

    @property
    def dynamic_elevation(self):
        return self.__dynamic_elevation

    @dynamic_elevation.setter
    def dynamic_elevation(self, dynamic_elevation):
        self.__dynamic_elevation = dynamic_elevation

    @property
    def original_y_pos(self):
        return self.__original_y_pos

    @property
    def original_x_pos(self):
        return self.__original_x_pos

    @property
    def pos(self):
        return self.__pos
    
    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height
    
    @property
    def top_rect(self):
        return self.__top_rect
    
    @top_rect.setter
    def top_rect(self, top_rect):
        self.__top_rect = top_rect

    @property
    def top_color(self):
        return self.__top_color

    @top_color.setter
    def top_color(self, top_color):
        self.__top_color = top_color

    @property
    def bottom_rect(self):
        return self.__bottom_rect

    @bottom_rect.setter
    def bottom_rect(self, bottom_rect):
        self.__bottom_rect = bottom_rect

    @property
    def bottom_color(self):
        return self.__bottom_color

    @bottom_color.setter
    def bottom_color(self, bottom_color):
        self.__bottom_color = bottom_color

    @property
    def text(self):
        return self.__text

    @property
    def font(self):
        return self.__font

    @property
    def text_surf(self):
        return self.__text_surf
    
    @text_surf.setter
    def text_surf(self, text_surf):
        self.__text_surf = text_surf

    @property
    def text_rect(self):
        return self.__text_rect
    
    @text_rect.setter
    def text_rect(self, text_rect):
        self.__text_rect = text_rect

    #Calculates the button depth
    def draw(self, surface):
        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center 

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

        pygame.draw.rect(surface, self.bottom_color, self.bottom_rect, border_radius = 10)
        pygame.draw.rect(surface, self.top_color, self.top_rect, border_radius = 10)
        surface.blit(self.text_surf, self.text_rect)

    #Checks if there is a mouse hover, if button is pressed and released or not
    def check_click(self, mouse_pos):
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = '#FFD56D'
            self.text_surf = self.font.render(self.text, True, '#664528')
            self.bottom_color = '#D1B05E'
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
                self.pressed = True
            else:
                self.dynamic_elevation = self.elevation
                if self.pressed == True:
                    self.pressed = False
                    return self.onClick()
        else:
            self.dynamic_elevation = self.elevation
            self.top_color = '#A16E40'
            self.bottom_color = '#614933' 
            self.text_surf = self.font.render(self.text, True, '#ffffff')

    @abstractmethod
    def onClick(self):
        pass
