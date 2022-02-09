import pygame
from GameLogic.Characters.Character import Character
from GameLogic.Characters.Skill import Skill
from GameLogic.Characters.Weapon import Weapon

class Player(Character):
    def __init__(self, name: str, sprites: list, health: int, max_health: int, 
                x_position: int, y_position: int, hitbox_x: int, 
                hitbox_y: int, speed: int, jump_height: int, 
                skill: Skill, weapon: Weapon, stamina: int, mana: int, xp: int, surface):
        super().__init__(name, sprites, health, max_health, 
                        x_position, y_position, hitbox_x, 
                        hitbox_y, speed, jump_height, 
                        skill, weapon)
        self.__stamina = stamina
        self.__mana = mana
        self.__xp = xp
        self.__x_position = x_position
        self.__y_position = y_position
        self.__speed = speed
        self.__jump_height = jump_height
        self.window = surface

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, stamina):
        self.__stamina = stamina

    @property
    def mana(self):
        return self.__mana

    @mana.setter
    def mana(self, mana):
        self.__mana = mana

    @property
    def xp(self):
        return self.__xp

    @xp.setter
    def xp(self, xp):
        self.__xp = xp

    @property
    def x_position(self):
        return self.__x_position
    
    @x_position.setter
    def x_position(self, x_position):
        self.__x_position = x_position

    @property
    def y_position(self):
        return self.__y_position

    @y_position.setter
    def y_position(self, y_position):
        self.__y_position = y_position

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        self.__speed = speed

    @property
    def jump_height(self):
        return self.__jump_height

    @jump_height.setter
    def jump_height(self, jump_height):
        self.__jump_height = jump_height

    '''
    def move(self):
        pressed_keys = pygame.key.get_pressed() 

        surface = pygame.display.get_surface()
        screen_width = surface.get_width()
        screen_height = surface.get_height()

        if self.rect.left > 0 and pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(self.speed, 0)
        
        if self.rect.right < screen_width and pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(self.speed, 0)

        if self.rect.up < screen_height and pressed_keys[pygame.K_UP]:
            self.jump()
    '''

    def set_weapon_damage(self, xp):
        pass

    def set_skill_damage(self, xp):
        pass

    def lose(self):
        pass

    def win(self):
        pass
    
    
    def move(self):
        pass
        '''
        right_change = 0
        left_change = 0
        up_change = 0
        down_change = 0

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    left_change = 10

                elif event.key == pygame.K_d:
                    right_change = 10

                #if event.key == pygame.K_SPACE:
                    #up_change = 150

                if event.key == pygame.K_LSHIFT:
                    self.speed(2)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    left_change = 0

                elif event.key == pygame.K_d:
                    right_change = 0

                #if event.key == pygame.K_SPACE:
                    #up_change = 0

                if event.key == pygame.K_LSHIFT:
                    self.speed(1)
            
            x_change = right_change - left_change
            self.__x_position += x_change
            #self.y_position = up_change - down_change

            self.window.draw_scaled_image("prototipo\Images\square.png", 
                                  self.hitbox_x, self.hitbox_y, 
                                  self.x_position, self.y_position)
'''