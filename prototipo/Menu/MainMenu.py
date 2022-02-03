import pygame

from Menu.Button import Button
from Menu.Help import Help
from Menu.Settings import Settings
from Menu.Play import Play


class MainMenu:
    def __init__(self, window):
        self.play = Play('Play', 300, 40, 250, 180, 5, '#614933', '#614933')
        self.help = Help('Help', 300, 40, 250, 280, 5, '#614933', '#614933')
        self.settings = Settings('Settings', 300, 40, 250, 380, 5, '#614933', '#614933')
        
        self.window = window
        self.__buttons = [self.play, self.help, self.settings]
        self.__menu_background = pygame.image.load("prototipo\Images\menu_background.jpg")

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
    #Drawing and displaying of buttons
    def buttons_draw(self):
        for button in self.buttons:
            button.draw_setup()
    
            pygame.draw.rect(self.window.display, button.bottom_color, button.bottom_rect, border_radius = 10)
            pygame.draw.rect(self.window.display, button.top_color, button.top_rect, border_radius = 10)
            self.window.display.blit(button.text_surf, button.text_rect)