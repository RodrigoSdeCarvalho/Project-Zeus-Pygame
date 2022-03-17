import pygame
from GameLogic.GUI.GameDisplay import GameDisplay
from Menu.MainMenu import MainMenu
from pygame.locals import *
from pygame import mixer

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Project Zeus")
        pygame.display.set_icon(pygame.transform.scale(pygame.image.load('prototipo/Images/game_icon.png'), (75,75)))
        
        mixer.init()
        mixer.music.load("prototipo\Sons\song.ogg")
        mixer.music.play()

        fps = 60
        self.clock = pygame.time.Clock()
        self.clock.tick(fps)
        self.window = GameDisplay(self.clock)
        self.mainMenu = MainMenu(self.window)
        self.mainMenu.show_main_menu()
