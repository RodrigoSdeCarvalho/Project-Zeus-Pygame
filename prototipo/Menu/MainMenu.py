import pygame

from Menu.Help import Help
from Menu.Settings import Settings
from Menu.Play import Play

class MainMenu:
    def __init__(self, surface):
        self.window = surface
        
        self.__buttons = [Play('Play', 260, 40, 430, 85, 5, '#614933', '#614933', surface),
                          Settings('Easy Mode', 260, 40, 430, 170, 5, '#614933', '#614933', surface),
                          Help('Tutorial', 260, 40, 430, 255, 5, '#614933', '#614933', surface, self)]
        
        self.__menu_background = pygame.transform.scale(pygame.image.load("prototipo\Images\menu_background.png"), (800, 600))
        self.__run = True

    @property
    def buttons(self):
        return self.__buttons
    
    @property
    def menu_background(self):
        return self.__menu_background

    @property
    def run(self):
        return self.__run

    @run.setter
    def run(self, run):
        self.__run = run

    def quit(self):
        pygame.quit()
        quit()

    #Loop that displays the menu with a background, buttons and deals with button pressing
    def show_main_menu(self):
        self.window.display.blit(self.menu_background, (0, 0))
        self.buttons_draw()

        pygame.display.update()

        while self.run != False:

            self.window.display.blit(self.menu_background, (0, 0))
            self.buttons_draw()
            pygame.display.update()
            mouse_pos = pygame.mouse.get_pos()
            for button in self.buttons:
                self.run = button.check_click(mouse_pos)
                self.buttons_draw()
                pygame.display.update()
                

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()

    #Drawing and displaying buttons
    def buttons_draw(self):
        for button in self.buttons:
            button.draw(self.window.display)
