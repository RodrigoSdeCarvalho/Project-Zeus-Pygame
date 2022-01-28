import pygame
from Characters.Character import Character
from Characters.Skill import Skill
from Characters.Weapon import Weapon

class Minion(Character):
    def __init__(self, name: str, health: int, max_health: int, 
                x_position: int, y_position: int, hitbox_x: int, 
                hitbox_y: int, speed: int, jump_height: int, 
                skill: Skill, weapon: Weapon):
        super().__init__(name, health, max_health, 
                        x_position, y_position, hitbox_x, 
                        hitbox_y, speed, jump_height, 
                        skill, weapon)