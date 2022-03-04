import pygame

from Menu.Button import Button
from GameLogic.Stage.Stage import Stage

class Play(Button):
    def __init__(self, text: str, width: int, height: int, x: int, y: int, elevation: int, topColor: str, bottomColor: str, surface):
        super().__init__(text, width, height, x, y, elevation, topColor, bottomColor)
        #self.screen = pygame.display.get_surface()
        self.__stage_list = [Stage(1, 1, surface, False)]
        self.window = surface

    @property
    def stage_list(self):
        return self.__stage_list

    def current_stage(self):
        for stage in self.stage_list:
            if stage.stage_completed == False:
                print(stage.level)
                return stage

    def start_current_stage(self):
        current_stage = self.current_stage()
        current_stage.start()

    def onClick(self):
            self.window.display.fill('#ffffff') #Retirar depois
            for i in range(len(self.stage_list)):
                self.current_stage()
                self.start_current_stage()
            return False
