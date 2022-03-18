import pygame
from GameLogic.Characters.Character import Character
from GameLogic.Characters.Skill import Skill
from GameLogic.Characters.Weapon import Weapon

class Player(Character):
    def __init__(self, name: str, sprites: list, health: int, max_health: int, 
                x_position: int, y_position: int, hitbox_x: int, 
                hitbox_y: int, speed: int, jump_height: int, 
                skill: Skill, weapon: Weapon, surface, facing: str = 'right'):
        super().__init__(name, sprites, health, max_health, 
                        x_position, y_position, hitbox_x, 
                        hitbox_y, speed, jump_height, 
                        skill, weapon)
        self.__min_speed = speed
        self.__speed = speed
        self.__max_speed = speed * 2.5
        self.__max_jump_height = jump_height
        self.__jumping = False
        self.__falling_time = 0 
        self.__attacking = False
        self.__facing = facing
        self.window = surface

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
    def max_jump_height(self):
        return self.__max_jump_height

    @max_jump_height.setter
    def max_jump_height(self, jump_height):
        self.__max_jump_height = jump_height
    
    @property
    def jumping(self):
        return self.__jumping
    
    @jumping.setter
    def jumping(self, jumping):
        self.__jumping = jumping
    
    @property
    def falling_time(self):
        return self.__falling_time

    @falling_time.setter
    def falling_time(self, falling_time):
        self.__falling_time = falling_time

    @property
    def facing(self):
        return self.__facing

    @facing.setter
    def facing(self, facing):
        self.__facing = facing

    @property
    def attacking(self):
        return self.__attacking

    @attacking.setter
    def attacking(self, attacking):
        self.__attacking = attacking

    def movement(self, keys, canJump):
        if keys[pygame.K_d]:
            self.move_right()

        if keys[pygame.K_a]:
            self.move_left()

        if keys[pygame.K_LSHIFT]:
            self.increase_speed()

        if not keys[pygame.K_LSHIFT]:
            self.decrease_speed()
            
        if not self.jumping:
            if canJump or self.y_position == 540:
                if keys[pygame.K_SPACE]:
                    self.jumping = True
        else:
            finished = self.jump()
            if finished:
                self.jumping = False

        return self.jumping
    
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
    
    def attack(self, keys, attacked_boss, target, clock):
        if not self.attacking:
            if keys[pygame.K_e] and (clock % 5 == 0):
                self.attacking = True
        else:
            finished = self.weapon.update(self.facing)
            self.weapon.draw()

            if attacked_boss:
                self.weapon.hit(target)

            if finished:
                self.attacking = False
    
    def update_weapon_position(self):
        if self.facing == 'right':
            self.weapon.update_position(self.x_position + self.hitbox_x - 5, self.y_position + self.hitbox_y / 2 + 5)
        else:
            self.weapon.update_position(self.x_position + 5, self.y_position + self.hitbox_y / 2 + 8)

    def jump(self):     
        if self.y_position >= 0:
            if self.jump_height >= 0:
                self.y_position -= self.jump_height * 2
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

    def fall(self, reset_y_position = 0, reset_height = 0, collision = False):
        distance_floor = 600 - (self.y_position + self.hitbox_y)
        if distance_floor > 0:
            self.y_position += 2 * self.falling_time
            self.falling_time += 1 
            self.update_weapon_position()
        else:
            self.y_position = 540
            self.falling_time = 0
            self.update_weapon_position()
            return True
        
        if collision:
            self.falling_time = 0
            self.y_position = reset_y_position - reset_height - 5
            self.update_weapon_position()
            return True

    def draw(self, sprite):
        if self.health > 0:
            self.window.draw_scaled_image(sprite, 
                        self.hitbox_x, self.hitbox_y, 
                        self.x_position, self.y_position)

    def animation(self):
        sprites = self.sprites

        if self.facing == "right":
            self.draw(sprites[0])
        
        if self.facing == "left":
            self.draw(sprites[1])
