from turtle import distance
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
        self.__min_speed = speed
        self.__speed = speed
        self.__max_speed = speed * 2.5
        self.__jump_height = jump_height
        self.__max_jump_height = jump_height
        self.__sprites = sprites
        self.window = surface
        self.__max_health = max_health
        self.falling_time = 0 

    @property
    def max_health(self):
        return self.__max_health

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
    def min_speed(self):
        return self.__min_speed

    @min_speed.setter
    def min_speed(self, speed):
        self.__min_speed = speed

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        self.__speed = speed

    @property
    def max_speed(self):
        return self.__max_speed

    @max_speed.setter
    def max_speed(self, speed):
        self.__max_speed = speed

    @property
    def jump_height(self):
        return self.__jump_height

    @jump_height.setter
    def jump_height(self, jump_height):
        self.__jump_height = jump_height

    @property
    def max_jump_height(self):
        return self.__max_jump_height

    @max_jump_height.setter
    def max_jump_height(self, jump_height):
        self.__max_jump_height = jump_height
        
    @property
    def sprites(self):
        return self.__sprites

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
    
    def move_left(self):
        if self.x_position >= 0:
            self.x_position -= self.speed

    def move_right(self):
        if self.x_position + self.hitbox_x <= self.window.width:
            self.x_position += self.speed
    
    def increase_speed(self):
        self.speed = self.max_speed

    def decrease_speed(self):
        self.speed = self.min_speed

    def jump(self):     
        if self.y_position >= 0:
            if self.jump_height >= 0:
                self.y_position -= (self.jump_height * abs(self.jump_height)) / 2
                self.jump_height -= 1
            else:
                self.jump_height = self.max_jump_height
                return True
        else:
            self.y_position = 0
            self.jump_height = self.max_jump_height
            return True

    def fall(self, collision = False):
        distance_floor = 600 - (self.y_position + self.hitbox_y)
        if distance_floor > 0:
            self.y_position += 2 * self.falling_time
            self.falling_time += 1 
        else:
            self.y_position = 540
            self.falling_time = 0
        
        if collision:
            self.falling_time = 0
