import pygame

class Weapon:
    def __init__(self, damage: int, sprite: list):
        self.__damage = damage 
        self.__sprite = sprite 

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