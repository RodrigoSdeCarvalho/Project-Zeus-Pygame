from tkinter import font
import pygame
from Menu.Button import Button

class Help(Button):
    def __init__(self, text: str, width: int, height: int, x: int, y: int, elevation: int, topColor: str, bottomColor: str, surface):
        super().__init__(text, width, height, x, y, elevation, topColor, bottomColor)
        self.screen = pygame.display.get_surface()
        self.window = surface
        self.__tutorial_background = pygame.transform.scale(pygame.image.load("prototipo/Images/tutorial_background.png"), (800, 600))
        self.__tutorial_icons = [pygame.transform.scale(pygame.image.load('prototipo/Images/movement.png'), (60, 60)),
                                 pygame.transform.scale(pygame.image.load('prototipo/Images/attack.png'), (60, 60)),
                                 pygame.transform.scale(pygame.image.load('prototipo/Images/defense.png'), (60, 60)),
                                 pygame.transform.scale(pygame.image.load('prototipo/Images/health.png'), (60, 60)),
                                 pygame.transform.scale(pygame.image.load('prototipo/Images/magic.png'), (60, 60)),
                                 pygame.transform.scale(pygame.image.load('prototipo/Images/enemy.png'), (60, 60))]
        font = pygame.font.Font('freesansbold.ttf', 17)
        text_color = '#CA8D56'
        self.__movement_text = [font.render('Para andar pressione as teclas \'A\' e \'D\'.', True, text_color),
                                font.render('Para pular pressione a barra de espaço.', True, text_color)]
        self.__movement_text_rect = []

        self.__attack_text = [font.render('Para atacar pressione a tecla \'E\'.', True, text_color)]
        self.__attack_text_rect = []

        self.__defense_text = [font.render('Para se defender use as plataformas.', True, text_color)]
        self.__defense_text_rect = []

        self.__health_text = [font.render('A vida do herói aparece no canto superior esquerdo da tela.', True, text_color),
                              font.render('A vida do inimigo aparece no canto superior direito da tela.', True, text_color)]
        self.__health_text_rect = []

        self.__magic_text = [font.render('O inimigo possui magias para lhe atacar, tome cuidado.', True, text_color)]
        self.__magic_text_rect = []

        self.__enemy_text = [font.render('Seu objetivo é matar os Deuses do Olimpo. Boa sorte.', True, text_color)]
        self.__enemy_text_rect = []

        for text in self.movement_text:
            self.movement_text_rect.append(text.get_rect())
            self.movement_text_rect[-1].left = 285
            self.movement_text_rect[-1].top = 85 + 25*len(self.movement_text_rect)
        
        for text in self.attack_text:
            self.attack_text_rect.append(text.get_rect())
            self.attack_text_rect[-1].left = 310
            self.attack_text_rect[-1].top = 180 + 25*len(self.attack_text_rect)
        
        for text in self.defense_text:
            self.defense_text_rect.append(text.get_rect())
            self.defense_text_rect[-1].left = 290
            self.defense_text_rect[-1].top = 260 + 25*len(self.defense_text_rect)
        
        for text in self.health_text:
            self.health_text_rect.append(text.get_rect())
            self.health_text_rect[-1].left = 210
            self.health_text_rect[-1].top = 327 + 25*len(self.health_text_rect)
        
        for text in self.magic_text:
            self.magic_text_rect.append(text.get_rect())
            self.magic_text_rect[-1].left = 230
            self.magic_text_rect[-1].top = 420 + 25*len(self.magic_text_rect)

        for text in self.enemy_text:
            self.enemy_text_rect.append(text.get_rect())
            self.enemy_text_rect[-1].left = 235
            self.enemy_text_rect[-1].top = 500 + 25*len(self.enemy_text_rect)
        
        self.__tutorial_text = [self.movement_text, self.attack_text, self.defense_text,
                                self.health_text, self.magic_text, self.enemy_text]
        self.__tutorial_text_rect = [self.movement_text_rect, self.attack_text_rect,
                                     self.defense_text_rect, self.health_text_rect,
                                     self.magic_text_rect, self.enemy_text_rect]

    @property
    def tutorial_background(self):
        return self.__tutorial_background
    
    @property
    def tutorial_icons(self):
        return self.__tutorial_icons

    @property
    def movement_text(self):
        return self.__movement_text
    
    @property
    def movement_text_rect(self):
        return self.__movement_text_rect

    @property
    def attack_text(self):
        return self.__attack_text

    @property
    def attack_text_rect(self):
        return self.__attack_text_rect
    
    @property
    def defense_text(self):
        return self.__defense_text

    @property
    def defense_text_rect(self):
        return self.__defense_text_rect

    @property
    def health_text(self):
        return self.__health_text

    @property
    def health_text_rect(self):
        return self.__health_text_rect
    
    @property
    def magic_text(self):
        return self.__magic_text

    @property
    def magic_text_rect(self):
        return self.__magic_text_rect
    
    @property
    def enemy_text(self):
        return self.__enemy_text

    @property
    def enemy_text_rect(self):
        return self.__enemy_text_rect
    
    @property
    def tutorial_text(self):
        return self.__tutorial_text

    @property
    def tutorial_text_rect(self):
        return self.__tutorial_text_rect

    def onClick(self):
        self.help_start()
        return False
    
    def help_start(self):
        help = True

        self.window.display.blit(self.tutorial_background, (0, 0))
        icon_y_position = 100
        for icon in self.tutorial_icons:
            self.window.display.blit(icon, (100, icon_y_position))
            icon_y_position += 80

        for section in range (0, len(self.tutorial_text)):
            for text in range (0, len(self.tutorial_text[section])):
                self.window.display.blit(self.tutorial_text[section][text], self.tutorial_text_rect[section][text])

        pygame.display.update()

        while help:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

