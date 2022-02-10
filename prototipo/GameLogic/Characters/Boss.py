import pygame
from GameLogic.Characters.Character import Character
from GameLogic.Characters.Skill import Skill
from GameLogic.Characters.Weapon import Weapon

class Boss(Character):
    def __init__(self, name: str, sprites: list, health: int, max_health: int, 
                x_position: int, y_position: int, hitbox_x: int, 
                hitbox_y: int, speed: int, jump_height: int, 
                skill: Skill, weapon: Weapon, weak_point_x: int, weak_point_y: int):
        super().__init__(name, sprites, health, max_health, 
                        x_position, y_position, hitbox_x, 
                        hitbox_y, speed, jump_height, 
                        skill, weapon)
        self.__weak_point_x: weak_point_x
        self.__weak_point_y: weak_point_y
        self.__x_position = x_position
        self.__y_position = y_position
        self.__speed = speed
        self.__jump_height = jump_height
        self.__sprites = sprites
    
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
    def weak_point_x(self):
        return self.__weak_point_x

    @weak_point_x.setter
    def weak_point_x(self, weak_point_x):
        self.__weak_point_x = weak_point_x

    @property
    def weak_point_y(self):
        return self.__weak_point_y

    @weak_point_y.setter
    def weak_point_y(self, weak_point_y):
        self.__weak_point_y = weak_point_y
        
    @property
    def sprites(self):
        return self.__sprites

    def summon_minions(self):
        pass
    
    def move(self):
        pass