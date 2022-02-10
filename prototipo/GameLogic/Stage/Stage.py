import pygame

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

        self.__players = [Player("Computatus", ["prototipo\Images\square.png"], 1000,
                                 1000, 0, 540, 60, 60, 5, 150, Skill("hit", 10, '', Player.x_position, Player.y_position),
                                 Weapon(10, ''), 100, 100, 0, surface)]
 
        '''Adicionar mais players  aqui'''

        self.__bosses = [Boss("Zeus", ["prototipo\Images\zeus.png"], 1000,
                     1000, 120, 72, 120, 72, 1, 150, Skill("thunder", 10, '', Boss.x_position, Boss.y_position),
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
   
    # def draw_object(self, object):
    #     self.window.draw_scaled_image(object.sprites[0], 
    #                           object.hitbox_x, object.hitbox_y, 
    #                           object.x_position, object.y_position)

    def draw_player(self, object):
        self.window.draw_scaled_image("prototipo\Images\square.png", 
                    object.hitbox_x, object.hitbox_y, 
                    object.x_position, object.y_position)

    def draw_boss(self, object):
        self.window.draw_scaled_image("prototipo\Images\qlue.png", 
                object.hitbox_x, object.hitbox_y, 
                object.x_position, object.y_position)
    
    def write_on_display(self,text, size, pos):
        largeText = pygame.font.Font('freesansbold.ttf', size)
        TextSurf = largeText.render(text, True, (0,0,0))
        TextRect = TextSurf.get_rect()
        TextRect.center = ((pos[0], pos[1]))
        self.window.display.blit(TextSurf, TextRect)

    def status(self, object, pos:list):
        pygame.draw.rect(self.window.display, (255,0,0), [pos[0], pos[1], object.max_health/10, 10])
        pygame.draw.rect(self.window.display, (0,255,0),[pos[0], pos[1], object.health/10, 10])
        self.write_on_display(f"{object.name} {object.health}/{object.max_health}", 10, [pos[0] + 45, pos[1] +5])

    def collision(self, object_1, object_2):
        top_left_x_1 = object_1.x_position
        top_left_y_1 = object_1.y_position
        bottom_left_y_1 = object_1.y_position + object_1.hitbox_y
        top_right_x_1 = object_1.x_position + object_1.hitbox_x

        top_left_x_2 = object_2.x_position
        top_left_y_2 = object_2.y_position
        bottom_left_y_2 = object_2.y_position + object_2.hitbox_y
        top_right_x_2 = object_2.x_position + object_2.hitbox_x

        if bottom_left_y_1 <= top_left_y_2:
            return False
        
        if top_left_y_1 >= bottom_left_y_2 :
            return False

        if top_right_x_1 <= top_left_x_2:
            return False

        if top_left_x_1 >= top_right_x_2:
            return False

        return True



    def start(self):
        index = self.index
        player = self.players[index]
        boss = self.bosses[index]
        #skill = self.skills[index]
        #weapon = self.weapons[index]
        #minion = self.minion[index]
        map = self.maps[index]

        play = True
        #thunder = False
        pygame.display.update()

        clock = 0
        while play:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            keys = pygame.key.get_pressed()

            if keys[pygame.K_d]:
                player.x_position += player.speed
            
            if keys[pygame.K_a]:
                player.x_position -= player.speed
                
            if keys[pygame.K_s]:
                player.y_position += player.speed

            if keys[pygame.K_LSHIFT]:
                player.speed = 10

            if keys[pygame.K_SPACE]:
                player.y_position -= 5

            if keys[pygame.K_e]:
                if self.collision(player, boss):
                    player.skill.attack(boss)
                    
            #if clock % (60 * 8):
                #thunder = True
                #self.window.draw_scaled_image("prototipo\Images\shunder.png", 10, 15, boss.x_position, boss.y_position)
                
            
            self.window.display.fill((0, 0, 0))
            self.status(boss, [700, 0])
            self.status(player, [0,0])

            if boss.health > 0:
                self.draw_boss(boss)

            if player.health > 0:    
                self.draw_player(player)
            
            clock += 1
            pygame.time.delay(10)
            pygame.display.update()

#Banco de dados com stage_completed (true ou false), para verificar qual a próxima fase.