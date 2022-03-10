import pygame
from pygame.math import Vector2

class Weapon:
    def __init__(self, damage: int, sprite: str, x_position: int, y_position: int, surface):
        self.__damage = damage 
        self.__sprite = pygame.transform.scale(pygame.image.load(sprite), (30, 70))
        self.__original_sprite = pygame.transform.scale(pygame.image.load(sprite), (30, 70))
        self.__x_position = x_position
        self.__y_position = y_position
        self.__hitbox_x = x_position + 30
        self.__hitbox_y = y_position + 70
        self.__image_rect = self.sprite.get_rect(center=(self.x_position, self.y_position))
        self.__pos = Vector2((self.x_position, self.y_position))
        self.__offset = Vector2(5, -25)
        self.__angle = 0
        self.window = surface

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
    def original_sprite(self):
        return self.__original_sprite
    
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
    def image_rect(self):
        return self.__image_rect

    @image_rect.setter
    def image_rect(self, image_rect):
        self.__image_rect = image_rect
    
    @property
    def pos(self):
        return self.__pos

    @pos.setter
    def pos(self, pos):
        self.__pos = pos
    
    @property
    def offset(self):
        return self.__offset

    @offset.setter
    def offset(self, offset):
        self.__offset = offset

    @property
    def angle(self):
        return self.__angle

    @angle.setter
    def angle(self, angle):
        self.__angle = angle

    def update_position(self, x_position, y_position):
        self.x_position = x_position
        self.y_position = y_position
        self.pos = (x_position, y_position)

    def rotate(self):
        self.sprite = pygame.transform.rotozoom(self.original_sprite, -self.angle, 1)
        offset_rotated = self.offset.rotate(self.angle)
        self.image_rect = self.sprite.get_rect(center=self.pos+offset_rotated)
    
    def update(self, direction='right'):
        if direction == 'right':
            self.angle += 12
        else:
            self.angle -= 12
        
        self.rotate()
        self.draw()

        if self.angle == 120 or self.angle == -120:
            self.angle = 0
            return True
    
    def draw(self):
        self.window.display.blit(self.sprite, self.image_rect)