import pygame

class MainMenu:
    def __init__(self, window):
        self.__buttons = []
        self.__menu_background = pygame.image.load("prototipo\Images\menu_background.jpg")
        self.__window = window

    def open_play(self):
        #play = Play()
        pass

    def open_help(self):
        #help = Help()
        pass

    def open_settings(self):
        #settings = Settings()
        pass

    def show_main_menu(self):
        while True:
            self.__window.display.blit(self.__menu_background, (0, 0))
            pygame.display.update()
