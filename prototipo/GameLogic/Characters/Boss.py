import pygame
from Characters.Character import Character
from Characters.Skill import Skill
from Characters.Weapon import Weapon

class Boss(Character):
    def __init__(self, name: str, health: int, max_health: int, 
                x_position: int, y_position: int, hitbox_x: int, 
                hitbox_y: int, speed: int, jump_height: int, 
                skill: Skill, weapon: Weapon, weak_point_x: int, weak_point_y: int):
        super().__init__(name, health, max_health, 
                        x_position, y_position, hitbox_x, 
                        hitbox_y, speed, jump_height, 
                        skill, weapon)
        self.__weak_point_x: weak_point_x
        self.__weak_point_y: weak_point_y

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

    def summon_minions(self):
        pass