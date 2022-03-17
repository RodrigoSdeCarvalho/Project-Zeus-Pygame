import pygame
from GameLogic.Characters.Player import Player
from GameLogic.Characters.Boss import Boss
from GameLogic.Characters.Skill import Skill
from GameLogic.Characters.Weapon import Weapon
from GameLogic.Stage.Platform import Platform
from Difficulty.Difficulty import Difficulty
from GameLogic.Stage.Collision import Collision

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

        self.__skills = [Skill("hit", 10, '', Player.x_position, 
                               Player.y_position, 0, 0, surface), 
                        Skill("thunder", 150*Difficulty().mode, 
                              {'down': 'prototipo\Images\shunder0.png',
                               'right': 'prototipo\Images\shunder90.png',
                               'left': 'prototipo\Images\shunder270.png',
                               'up': 'prototipo\Images\shunder180.png'},
                              0, 0, 20, 30, surface)] 

        self.__weapons = []

        self.__minions = []

        self.__players = [Player("Computatus", ["prototipo\Images\square.png"], 1000,
                                 1000, 0, 540, 60, 60, 3, 16, self.skills[0],
                                 Weapon(10, 'prototipo\Images\sword_0.png', 60, 80, surface), surface)]
 
        '''Adicionar mais players  aqui'''

        self.__bosses = [Boss("Zeus", ["prototipo\Images\zeus.png"], 1000,
                     1000, 200, 72, 120, 72, 1, 150, self.skills[1], surface)]
        self.__players = [Player("Computatus", ["prototipo\Images\pygame_player.png"], 1000,
                                 1000, 0, 540, 60, 60, 5, 12, self.skills[0],
                                 Weapon(10, 'prototipo\Images\sword_0.png', 60, 80, surface), 100, 100, 0, surface)]
 
        '''Adicionar mais players  aqui'''

        self.__bosses = [Boss("Zeus", ["prototipo\Images\pygame_boss.png"], 1000,
                     1000, 200, 72, 120, 72, 1, 150, self.skills[1],
                     20, 60, surface)]

        self.__platforms = [Platform(80, 350, 250, 50 , "prototipo\Images\platform.png", 250, 50, surface),
                            Platform(470, 350, 250, 50 , "prototipo\Images\platform.png", 250, 50, surface)]

        self.__backgrounds = [pygame.transform.scale(pygame.image.load("prototipo/Images/background_stage.jpg"), (800, 600))]

        self.collision = Collision

        self.__lose = pygame.transform.scale(pygame.image.load("prototipo/Images/lose_background.jpg"), (800, 600))
        self.__win = pygame.transform.scale(pygame.image.load("prototipo/Images/win_background.jpg"), (800, 600))

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

    @property
    def backgrounds(self):
        return self.__backgrounds
    
    @property
    def lose(self):
        return self.__lose

    @property
    def win(self):
        return self.__win

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
            self.window.display.fill(('#614933'))
            self.window.write_on_display("Pausado", 30, [400, 270], ('#FFD56D'))
            self.window.write_on_display("Pressione C para continuar", 20, [400, 320], ('#CF9158'))
            pygame.display.update()
    
    def vitoria(self):
        self.stage_completed = True
        run = True

        while run:
            self.window.display.blit(self.win, (0, 0))
            self.window.write_on_display("VITÓRIA", 50, [400, 300], ('#E1BC61'))
            self.window.write_on_display("PRESSIONE QUALQUER BOTÃO", 30, [400, 350], ('#E1BC61'))
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
            self.window.display.blit(self.lose, (0, 0))
            self.window.write_on_display("DERROTA", 50, [400, 300], ('#FFD56D'))
            self.window.write_on_display("PRESSIONE QUALQUER BOTÃO", 30, [400, 350], ('#FFD56D'))
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
        background = self.backgrounds[index]
        platforms = self.platforms

        clock = 0
        play = True
        skill_ground_collision = False
        player_hit = False
        attacked_boss = False
        canJump = False

        vitoria = False
        derrota = False

        pygame.display.update()
        while play:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_p]:
                self.pause() #p para pausar, c para continuar


            #Game loop only tells Player Class what keys were pressed and if he can jump
            #Player Class decides what movement happens based on key pressed
            canFall = player.movement(keys, canJump)
            pygame.display.update()
            
            #Game loop tells Player Class what keys were pressed, if he hit the target, the target and the clock
            player.attack(keys, attacked_boss, boss, clock)
            pygame.display.update()

            #If player dies he loses
            derrota = player.die()

            #Checks if the player's weapon hit the Boss
            if self.collision.check(player.weapon, boss):
                    attacked_boss = True
            else:
                attacked_boss = False

            #Checks if player is above a platform
            #If so he can jump
            #Was not able to put this in a loop due to bad performance
            if (self.collision.check(platforms[0], player) or self.collision.check(platforms[1], player)):
                canJump = True
            else:
                canJump = False

            #If player is not jumping, he falls to a platform or to the ground
            if not canFall:
                if not (self.collision.check(platforms[0], player) or self.collision.check(platforms[1], player)):
                    player.fall()
                else:
                    player.fall(platforms[0].y_position, platforms[0].height, True)

            self.window.display.blit(background, (0, 0))

            #Player and Boss health bars
            boss.status([680, 20])
            player.status([3, 20])

            for platform in platforms:
                platform.draw() 

            #Boss movement and attacking
            boss.move()
            clock = boss.attack(skill_ground_collision, player, player_hit, clock)

            #Tells the boss if a collision with his skill and player occurred
            if self.collision.check(boss.skill, player):
                player_hit = True
            else:
                player_hit = False
            
            #Tells the boss if a collision with his skill and a platform occurred
            if self.collision.check(boss.skill, platforms[0]) or self.collision.check(boss.skill, platforms[1]):
                skill_ground_collision = True
            else:
                skill_ground_collision = False

            #If boss dies player wins
            vitoria = boss.die()

            #If player wins or loses game loop stops running
            if vitoria or derrota:
                play = False


            clock += 1
            pygame.time.delay(10) #Define a velocidade do loop.
            pygame.display.update()

        #Shows winning or losing screens 
        if vitoria:
            self.vitoria()
        if derrota:
            self.derrota()
