from abc import ABC, abstractmethod
import pygame

#Alterar encapsulamento dos atributos
#Mudar cursor do mouse ao dar hover sobre botao
class Button(ABC):
    def __init__(self, text: str, width: int, height: int, x: int, y: int, elevation: int, topColor: str, bottomColor: str):
        #Initial state and position of the button
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation  #Used to generate a button with elevation
        self.original_y_pos = y
        self.original_x_pos = x
        self.pos = (self.original_x_pos, self.original_y_pos)
        
        self.width = width
        self.height = height

        #Creates a rectangle which represents the top part of the button
        self.top_rect = pygame.Rect(self.pos, (self.width, self.height))
        self.top_color = topColor

        #Creates a rectangle which represents the bottom part of the button - this creates a feeling of depth
        self.bottom_rect = pygame.Rect(self.pos, (self.width, self.height))
        self.bottom_color = bottomColor
        
        #Rendering the text inside the button
        self.text = text
        self.font = pygame.font.SysFont('Montserrat', 27)
        self.text_surf = self.font.render(self.text, True, '#FFFFFF')
        self.text_rect = self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

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
                    self.onClick()
                    self.pressed = False
        else:
            self.dynamic_elevation = self.elevation
            self.top_color = '#A16E40'
            self.bottom_color = '#614933' 
            self.text_surf = self.font.render(self.text, True, '#ffffff')

    @abstractmethod
    def onClick(self):
        pass
