import pygame

from Menu.Button import Button
from Menu.Help import Help
from Menu.Settings import Settings
from Menu.Play import Play

class MainMenu:
    def __init__(self, surface):
        self.window = surface
        
        self.__buttons = [Play('Play', 260, 40, 430, 85, 5, '#614933', '#614933', surface),
                          Settings('Settings', 260, 40, 430, 170, 5, '#614933', '#614933', surface),
                          Help('Help', 260, 40, 430, 255, 5, '#614933', '#614933', surface)]
        
        self.__menu_background = pygame.transform.scale(pygame.image.load("prototipo\Images\menu_background.png"), (800, 600))

    @property
    def buttons(self):
        return self.__buttons
    
    @property
    def menu_background(self):
        return self.__menu_background
    
    # def open_play(self):
    #     #play = Play()
    #     pass

    # def open_help(self):
    #     #help = Help()
    #     pass

    # def open_settings(self):
    #     #settings = Settings()
    #     pass

    def quit(self):
        pygame.quit()
        quit()

    #Loop that displays the menu with a background, buttons and deals with button presses
    def show_main_menu(self):
        self.window.display.blit(self.menu_background, (0, 0))
        self.buttons_draw()

        pygame.display.update()

        while True: 
            mouse_pos = pygame.mouse.get_pos()
            for button in self.buttons:
                button.check_click(mouse_pos)
                self.buttons_draw()
                pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()

    #Alterar - alto acoplamento em relacao aos botoes
    #Drawing and displaying buttons
    def buttons_draw(self):
        for button in self.buttons:
            button.draw(self.window.display)