from turtle import distance
import pygame
from GameLogic.Characters.Character import Character
from GameLogic.Characters.Skill import Skill
from GameLogic.Characters.Weapon import Weapon

class Player(Character):
    def __init__(self, name: str, sprites: list, health: int, max_health: int, 
                x_position: int, y_position: int, hitbox_x: int, 
                hitbox_y: int, speed: int, jump_height: int, 
                skill: Skill, weapon: Weapon, stamina: int, mana: int, xp: int, surface, facing: str = 'right'):
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
        self.__hitbox_x = hitbox_x
        self.__hitbox_y = hitbox_y
        self.__facing = facing

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
    
    @property
    def facing(self):
        return self.__facing

    @facing.setter
    def facing(self, facing):
        self.__facing = facing

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
            self.facing = 'left'
            self.update_weapon_position()

    def move_right(self):
        if self.x_position + self.hitbox_x <= self.window.width:
            self.x_position += self.speed
            self.facing = 'right'
            self.update_weapon_position()
    
    def increase_speed(self):
        self.speed = self.max_speed

    def decrease_speed(self):
        self.speed = self.min_speed
    
    def attack(self):
        stop = self.weapon.update(self.facing)
        self.weapon.draw()

        return stop
    
    def update_weapon_position(self):
        if self.facing == 'right':
            self.weapon.update_position(self.x_position + self.hitbox_x, self.y_position + self.hitbox_y / 2)
        else:
            self.weapon.update_position(self.x_position, self.y_position + self.hitbox_y / 2)

    def jump(self):     
        if self.y_position >= 0:
            if self.jump_height >= 0:
                self.y_position -= (self.jump_height * 4)
                self.jump_height -= 1
                self.update_weapon_position()
            else:
                self.jump_height = self.max_jump_height
                self.update_weapon_position()
                return True
                
        else:
            self.y_position = 0
            self.jump_height = self.max_jump_height
            self.update_weapon_position()
            return True

    def fall(self, collision = False):
        distance_floor = 600 - (self.y_position + self.hitbox_y)
        if distance_floor > 0:
            self.y_position += 2 * self.falling_time
            self.falling_time += 1 
            self.update_weapon_position()
        else:
            self.y_position = 540
            self.falling_time = 0
            self.update_weapon_position()
        
        if collision:
            self.falling_time = 0
            self.update_weapon_position()

    def draw(self):
        self.window.draw_scaled_image("prototipo\Images\pygame_player.png", 
                    self.__hitbox_x, self.__hitbox_y, 
                    self.__x_position, self.__y_position)
