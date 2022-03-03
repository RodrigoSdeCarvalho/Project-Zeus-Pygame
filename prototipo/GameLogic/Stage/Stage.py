from re import L
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

        self.__skills = [Skill("hit", 10, '', Player.x_position, Player.y_position, 0, 0), 
                            Skill("thunder", 200, '', 0, 0, 20, 20)] 

        self.__weapons = []

        self.__minions = []

        self.__players = [Player("Computatus", ["prototipo\Images\square.png"], 1000,
                                 1000, 0, 540, 60, 60, 5, 12, self.skills[0],
                                 Weapon(10, ''), 100, 100, 0, surface)]
 
        '''Adicionar mais players  aqui'''

        self.__bosses = [Boss("Zeus", ["prototipo\Images\zeus.png"], 1000,
                     1000, 200, 72, 120, 72, 1, 150, self.skills[1],
                     Weapon(10, ''), 20, 60)]

        self.__platforms = [Platform(80, 350, 250, 50 , "prototipo\Images\platform.png", 250, 50, "white", surface),
                            Platform(470, 350, 250, 50 , "prototipo\Images\platform.png", 250, 50, "white", surface)]

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

    #alterar
    def draw_player(self, object):
        self.window.draw_scaled_image("prototipo\Images\square.png", 
                    object.hitbox_x, object.hitbox_y, 
                    object.x_position, object.y_position)

    def draw_boss(self, object):
        self.window.draw_scaled_image("prototipo\Images\qlue.png", 
                object.hitbox_x, object.hitbox_y, 
                object.x_position, object.y_position)

    def draw_skill(self, object, x, y):
        self.window.draw_scaled_image("prototipo\Images\white.jpg",
                object.hitbox_x, object.hitbox_y,
                x, y)
    
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

    def platform_collision(self, object_1, object_2): #Differs from the collision method because it affects how the player moves differently depending on  which side a collision is detected. 
        top_left_x_1 = object_1.x_position
        top_left_y_1 = object_1.y_position
        bottom_left_y_1 = object_1.y_position + object_1.hitbox_y
        top_right_x_1 = object_1.x_position + object_1.hitbox_x

        top_left_x_2 = object_2.x_position
        top_left_y_2 = object_2.y_position
        bottom_left_y_2 = object_2.y_position + object_2.hitbox_y
        top_right_x_2 = object_2.x_position + object_2.hitbox_x      

        if bottom_left_y_1 > top_left_y_2: #Player above platform
            platform_collision_sides["up"] = True
            return

        if top_left_y_1 < bottom_left_y_2 : #Player below platform
            platform_collision_sides["down"] = True
            return

        if top_right_x_1 > top_left_x_2: #Player on the left of the platform
            platform_collision_sides["left"] = True
            return

        if top_left_x_1 < top_right_x_2: #Player on the right of the platform
            platform_collision_sides["right"] = True
            return

        return

    def start(self):
        global platform_collision_sides

        index = self.index
        player = self.players[index]
        boss = self.bosses[index]
        #skill = self.skills[index]
        #weapon = self.weapons[index]
        #minion = self.minion[index]
        platforms = self.platforms
        map = self.maps[index]

        play = True
        #thunder = False
        pygame.display.update()

        clock = 0
        boss_skill_run = True
        jumping = False

        while play:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            
            keys = pygame.key.get_pressed()

            platform_collision_sides = {"up": False, "down": False, "left": False, "right": False}
            
            if self.collision(player, platforms[0]) or self.collision(player, platforms[1]):
                for platform in platforms:
                     self.platform_collision(player, platform)

            if keys[pygame.K_d] and platform_collision_sides["left"] == False:
                player.move_right()

            if keys[pygame.K_a] and platform_collision_sides["right"] == False:
                player.move_left()

            if keys[pygame.K_LSHIFT]:
                player.increase_speed()
            
            if not keys[pygame.K_LSHIFT]:
                player.decrease_speed()

            if keys[pygame.K_e]:
                if self.collision(player, boss):
                    player.skill_attack(boss)

            if not jumping:
                if not platform_collision_sides['up']:
                    player.fall()
                
                if keys[pygame.K_SPACE] and (platform_collision_sides['up'] or player.y_position == 540):
                    jumping = True
            else:
                if not platform_collision_sides['down']:
                    finished = player.jump()
                    if finished:
                        player.fall()
                        jumping = False
                else:
                    jumping = False
            
            self.window.display.fill((0, 0, 0))
            self.status(boss, [700, 0])
            self.status(player, [0,0])

            for platform in platforms:
                platform.draw() 

            if boss.health > 0:
                boss.move()
                self.draw_boss(boss) 
                if player.health > 0:
                    if boss_skill_run and clock % (60 * 4):
                        self.draw_skill(boss.skill, boss.skill.x_position, boss.skill.y_position)
                        boss.skill.move(player)
                        if self.collision(boss.skill, player):
                            boss.skill_attack(player)
                            boss_skill_run = False
                        if self.collision(boss.skill, platforms[0]) or self.collision(boss.skill, platforms[1]):
                            boss_skill_run = False
                    else:
                        boss.skill_reset()
                        
                        if clock % (60) == 0:  
                            clock = 0
                            boss_skill_run = True                         

            if player.health > 0:    
                self.draw_player(player)

            clock += 1
            pygame.time.delay(10) #Define a velocidade do loop.
            pygame.display.update()

#Banco de dados com stage_completed (true ou false), para verificar qual a próxima fase.