import pygame

class Skill:
    def __init__(self, name: str, damage: int, sprite: list, x_position, y_position):
        self.__name = name
        self.__damage = damage 
        self.__sprite = sprite 
        self.__x_position = x_position
        self.__y_position = y_position

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, damage):
        self.__damage = damage

    @property
    def sprite(self):
        return self.__sprite

    @sprite.setter
    def sprite(self, sprite):
        self.__sprite = sprite

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

    def attack(self, target):
        if target.health > 0:
            target.health -= self.damage

    def thunder(self, target):
        pass