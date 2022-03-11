import pygame

from Menu.Button import Button
from GameLogic.Stage.Stage import Stage

class Play(Button):
    def __init__(self, text: str, width: int, height: int, x: int, y: int, elevation: int, topColor: str, bottomColor: str, surface):
        super().__init__(text, width, height, x, y, elevation, topColor, bottomColor)
        #self.screen = pygame.display.get_surface()
        self.__stage_list = [Stage(1, 1, surface, False)]
        self.window = surface
        self.surface = surface

    @property
    def stage_list(self):
        return self.__stage_list
    
    @stage_list.setter
    def stage_list(self, lista):
        self.__stage_list = lista

    def current_stage(self):
        for stage in self.stage_list:
            if stage.stage_completed == False:
                print(stage.level)
                return stage
        
        return 'jogo-completo'

    def start_current_stage(self):
        current_stage = self.current_stage()
        if current_stage == 'jogo-completo':
            for stage in self.stage_list:
                stage.reset_stage()
            
            current_stage = self.current_stage()
        
        current_stage.start()

    def onClick(self): #Retirar depois
        #a próxima linha garante que toda vez que o jogador clicar no botão de jogar, uma nova instância da lista de estágios é carregada.
        #Essa implementação pode gerar problemas caso hajam vários estágios, porém como é só um deve funcionar corretamente.
        self.stage_list = [Stage(1, 1, self.surface, False)]

        for i in range(len(self.stage_list)):
            self.start_current_stage()
        #self.window.display.fill('#ffffff') #Retirar depois 
        #self.current_stage()
        self.start_current_stage()
        return False
