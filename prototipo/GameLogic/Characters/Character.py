import pygame
from abc import ABC
from GameLogic.Characters.Skill import Skill
from GameLogic.Characters.Weapon import Weapon

class Character(ABC):
    def __init__(self, name: str, sprites: list, health: int, max_health: int, 
                x_position: int, y_position: int, hitbox_x: int, 
                hitbox_y: int, speed: int, jump_height: int, 
                skill: Skill = "", weapon: Weapon = ""):
        self.__name = name
        self.__sprites = sprites
        self.__health = health
        self.__max_health = max_health
        self.__x_position = x_position
        self.__y_position = y_position
        self.__hitbox_x = hitbox_x
        self.__hitbox_y = hitbox_y
        self.__speed = speed
        self.__jump_height = jump_height
        self.__skill = skill
        self.__weapon = weapon

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def sprites(self):
        return self.__sprites

    @sprites.setter
    def sprites(self, sprites):
        self.__sprites = sprites

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, health):
        self.__health = health

    @property
    def max_health(self):
        return self.__max_health

    @max_health.setter
    def max_health(self, max_health):
        self.__max_health = max_health

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
    def hitbox_x(self):
        return self.__hitbox_x

    @hitbox_x.setter
    def hitbox_x(self, hitbox_x):
        self.__hitbox_x = hitbox_x

    @property
    def hitbox_y(self):
        return self.__hitbox_y

    @hitbox_y.setter
    def hitbox_y(self, hitbox_y):
        self.__hitbox_y = hitbox_y

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

    @property
    def skill(self):
        return self.__skill

    @skill.setter
    def skill(self, skill):
        self.__skill = skill

    @property
    def weapon(self):
        return self.__weapon

    @weapon.setter
    def weapon(self, weapon):
        self.__weapon = weapon

    def status(self, pos: list):
        pygame.draw.rect(self.window.display, (255,0,0), [pos[0], pos[1], self.max_health/8.5, 10])
        pygame.draw.rect(self.window.display, (0,255,0),[pos[0], pos[1], self.health/8.5, 10])
        self.window.write_on_display(f"{self.name} {self.health}/{self.max_health}", 10, [pos[0] + 60, pos[1] + 5])

    def skill_attack(self, target):
        if self.health > 0:
            self.skill.attack(target)

    def weapon_attack(self):
        self.weapon.attack()

    def take_damage(self, damage_taken):
        self.health -= damage_taken

        if self.health <= 0:
            self.die()

    def die(self):
        if self.health <= 0:
            self.health = 0
            return True
        
        return False