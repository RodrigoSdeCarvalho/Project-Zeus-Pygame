import pygame

class Skill:
    def __init__(self, name: str, damage: int, sprite: list):
        self.__name = name
        self.__damage = damage 
        self.__sprite = sprite 

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

    def attack(self):
        pass