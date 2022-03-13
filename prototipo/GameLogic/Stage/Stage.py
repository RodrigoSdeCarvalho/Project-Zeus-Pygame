import pygame
from GameLogic.Characters.Player import Player
from GameLogic.Characters.Boss import Boss
from GameLogic.Characters.Skill import Skill
from GameLogic.Characters.Weapon import Weapon
from GameLogic.Characters.Minion import Minion
from GameLogic.Stage.Platform import Platform
from GameLogic.Stage.Map import Map
from Difficulty.Difficulty import Difficulty

#O int do level vai ser o index da lista com os objetos de Player, Boss etc, pois cada
#fase tem esses objetos diferentes.

#Se os componentes do stage, devido à diferença entre os stages, ficarem muito diferentes,
#Será necessário fazer arquivos diferentes para componentes diferentes. Ex: lógica de duas
#skills ficar muito diferente, rotina de mov dos bosses etc. Deve-se colocar esses novos 
#objetos nas listas da create_stage_components.

class Stage:
    def __init__(self, level: int, surface, stage_completed = False):
        self.__level = level
        self.__stage_completed = stage_completed
        self.window = surface

        self.__index = self.__level - 1

        self.__skills = [Skill("hit", 10, '', Player.x_position, Player.y_position, 0, 0, surface), 
                            Skill("thunder", 150*Difficulty().mode, '', 0, 0, 20, 20, surface)] 

        self.__weapons = []

        self.__minions = []

        self.__players = [Player("Computatus", ["prototipo\Images\square.png"], 1000,
                                 1000, 0, 540, 60, 60, 5, 12, self.skills[0],
                                 Weapon(10, 'prototipo\Images\sword_0.png', 60, 80, surface), 100, 100, 0, surface)]
 
        '''Adicionar mais players  aqui'''

        self.__bosses = [Boss("Zeus", ["prototipo\Images\zeus.png"], 1000,
                     1000, 200, 72, 120, 72, 1, 150, self.skills[1],
                     20, 60, surface)]

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

    def status(self, object, pos: list):
        pygame.draw.rect(self.window.display, (255,0,0), [pos[0], pos[1], object.max_health/8.5, 10])
        pygame.draw.rect(self.window.display, (0,255,0),[pos[0], pos[1], object.health/8.5, 10])
        self.window.write_on_display(f"{object.name} {object.health}/{object.max_health}", 10, [pos[0] + 60, pos[1] + 5])

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
    
    def reset_stage(self):
        self.stage_completed = False
    
    def pause(self):
        #p para pausar, c para continuar
        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        paused = False
            
            #próximas linhas ainda não funcionam
            self.window.display.fill((100, 100, 100))
            self.window.write_on_display("Pausado", 15, [300, 300])
            self.window.write_on_display("Pressione C para continuar",10, [400, 300])
            pygame.display.update()
    
    def vitoria(self):
        self.stage_completed = True
        run = True

        while run:
            self.window.display.fill((100, 100, 100))
            self.window.write_on_display("VITÓRIA", 50, [400, 250])
            self.window.write_on_display("PRESSIONE QUALQUER BOTÃO", 30, [400, 350])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    run = False

    def derrota(self):
        self.stage_completed = False
        run = True
        
        while run:
            self.window.display.fill((100, 100, 100))
            self.window.write_on_display("DERROTA", 50, [400, 250])
            self.window.write_on_display("PRESSIONE QUALQUER BOTÃO", 30, [400, 350])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    run = False

    def start(self):
        index = self.index
        player = self.players[index]
        boss = self.bosses[index]
        #weapon = self.weapons[index]
        #minion = self.minion[index]
        platforms = self.platforms

        clock = 0
        play = True
        boss_skill_run = True
        player_attacking = False
        jumping = False

        vitoria = True

        pygame.display.update()
        while play:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            keys = pygame.key.get_pressed()

            if keys[pygame.K_p]:
                self.pause() #p para pausar, c para continuar

            #Game loop only tells Player Class what keys were pressed
            #Player Class decides what movement happens based on key pressed
            player.movement(keys)

            if not jumping:
                if not (self.collision(platforms[0], player) or self.collision(platforms[1], player)):
                    player.fall()
                else:
                    player.fall(True)
                    player.y_position = platforms[0].y_position - platforms[0].height - 5

                if keys[pygame.K_SPACE] and (self.collision(platforms[0], player) or self.collision(platforms[1], player) or player.y_position == 540):
                    jumping = True
            else:
                finished = player.jump()
                if finished:
                    player.fall()
                    jumping = False
            
            self.window.display.fill((0, 0, 0))
            self.status(boss, [680, 20])
            self.status(player, [3, 20])

            for platform in platforms:
                platform.draw() 

            if boss.health > 0:
                boss.move()
                boss.draw()

                if player.health > 0:
                    if boss_skill_run and clock % (60 * 4):
                        boss.skill.draw()
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
            else:
                vitoria = True
                play = False                   

            if player.health > 0:    
                player.draw()
            else:
                vitoria = False
                play = False

            if not player_attacking:
                if keys[pygame.K_e] and clock % (10) == 0:
                    player_attacking = True
            else:
                finished = player.attack()
                if self.collision(player.weapon, boss):
                    boss.health -= player.weapon.damage
                if finished:
                    player_attacking = False

            clock += 1
            pygame.time.delay(10) #Define a velocidade do loop.
            pygame.display.update()
    
        if vitoria:
            self.vitoria()
        else:
            self.derrota()
