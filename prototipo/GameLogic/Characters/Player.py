import pygame
from Characters.Character import Character
from Characters.Skill import Skill
from Characters.Weapon import Weapon

class Player(Character):
    def __init__(self, name: str, health: int, max_health: int, 
                x_position: int, y_position: int, hitbox_x: int, 
                hitbox_y: int, speed: int, jump_height: int, 
                skill: Skill, weapon: Weapon, stamina: int, mana: int, xp: int):
        super().__init__(name, health, max_health, 
                        x_position, y_position, hitbox_x, 
                        hitbox_y, speed, jump_height, 
                        skill, weapon)
        self.__stamina = stamina
        self.__mana = mana
        self.__xp = xp

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

    def set_weapon_damage(self, xp):
        pass

    def set_skill_damage(self, xp):
        pass

    def lose(self):
        pass

    def win(self):
        pass