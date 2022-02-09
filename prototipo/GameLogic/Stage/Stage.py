import pygame

from platform import platform
from GameLogic.Characters.Player import Player
from GameLogic.Characters.Boss import Boss
from GameLogic.Characters.Skill import Skill
from GameLogic.Characters.Weapon import Weapon
from GameLogic.Characters.Minion import Minion
from GameLogic.Stage.Platform import Platform
from GameLogic.Stage.Map import Map

#O int do level vai ser o index da lista com os objetos de Player, Boss etc, pois cada
#fase tem esses objetos diferentes.

#Se os componentes do stage, devido à diferença entre os stages, ficarem muito diferentes,
#Será necessário fazer arquivos diferentes para componentes diferentes. Ex: lógica de duas
#skills ficar muito diferente, rotina de mov dos bosses etc. Deve-se colocar esses novos 
#objetos nas listas da create_stage_components.

class Stage:
    def __init__(self, level: int, difficulty: int, surface, stage_completed = False):
        self.__level = level 
        self.__difficulty = difficulty
        self.__stage_completed = stage_completed
        self.window = surface

        self.__index = self.__level - 1

        self.__skills = [] 

        self.__weapons = []

        self.__minions = []

        self.__players = [Player("Computatus", ["prototipo\Images\square.png"], 100,
                                 100, 50, 50, 60, 60, 15, 150, Skill("hit", 10, ''),
                                 Weapon(10, ''), 100, 100, 0, surface)]
 
        '''Adicionar mais players  aqui'''

        self.__bosses = [Boss("Zeus", ["prototipo\Images\zeus.png"], 100,
                     100, 40, 72, 40, 72, 1, 150, Skill("hitm", 10, ''),
                     Weapon(10, ''), 20, 60)]

        self.__platforms = [Platform(0, 0, 600, 1, (0, 0, 0))]

        self.__maps = [Map("prototipo\Images\olympus.png", self.__platforms[self.__index])]

    @property
    def index(self):
        return self.__index

    @property
    def skills(self):
        return self.__skills

    @property
    def players(self):
        return self.__players

    @property
    def weapons(self):
        return self.__weapons

    @property
    def minions(self):
        return self.__minions

    @property
    def platforms(self):
        return self.__platforms

    @property
    def bosses(self):
        return self.__bosses

    @property
    def maps(self):
        return self.__maps

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, level):
        self.__level = level

    @property
    def difficulty(self):
        return self.__difficulty

    @difficulty.setter
    def difficulty(self, difficulty):
        self.__difficulty = difficulty

    @property
    def stage_completed(self):
        return self.__stage_completed

    @stage_completed.setter
    def stage_completed(self, stage_completed):
        self.__stage_completed = stage_completed
   
    # def draw_player(self):
    #     self.window.draw_scaled_image("prototipo\Images\square.png", 
    #                           player.hitbox_x, player.hitbox_y, 
    #                           player.x_position, player.y_position)

    def start(self):
        index = self.index
        player = self.players[index]
        #boss = self.bosses[index]
        #skill = self.skills[index]
        #weapon = self.weapons[index]
        #minion = self.minion[index]
        map = self.maps[index]

        play = True
        right_change = 0
        left_change = 0
        up_change = 0
        down_change = 0

        pygame.display.update()

        while play:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                # if event.type == pygame.KEYDOWN:
                #     if event.key == pygame.K_a:
                #         left_change = 10

                #     if event.key == pygame.K_d:
                #         right_change = 10

                #     #if event.key == pygame.K_SPACE:
                #         #up_change = 150

                #     if event.key == pygame.K_LSHIFT:
                #         player.__speed = 2

                # if event.type == pygame.KEYUP:
                #     if event.key == pygame.K_a:
                #         left_change = 0

                #     if event.key == pygame.K_d:
                #         right_change = 0

                #     #if event.key == pygame.K_SPACE:
                #         #up_change = 0

                #     if event.key == pygame.K_LSHIFT:
                #         player.__speed = 1

                # x_change = player.speed * (right_change - left_change)
                # player.x_position += x_change
                # #self.y_position = up_change - down_change

            keys = pygame.key.get_pressed()

            if keys[pygame.K_d]:
                player.x_position += player.speed
            
            if keys[pygame.K_a]:
                player.x_position -= player.speed

            if keys[pygame.K_LSHIFT]:
                player.speed = 20

            if keys[pygame.K_SPACE]:
                player.y_position -= 10

            self.window.display.fill((0, 0, 0))
            self.window.draw_scaled_image("prototipo\Images\square.png", 
                                player.hitbox_x, player.hitbox_y, 
                                player.x_position, player.y_position)

            pygame.time.delay(10)
            pygame.display.update()

#Banco de dados com stage_completed (true ou false), para verificar qual a próxima fase.