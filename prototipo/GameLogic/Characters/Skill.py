class Skill:
    def __init__(self, name: str, damage: int, sprites: dict, x_position, y_position, hitbox_x, hitbox_y, surface):
        self.__name = name
        self.__damage = damage 
        self.__sprites = sprites
        self.__x_position = x_position
        self.__y_position = y_position
        self.__initial_hitbox_x = hitbox_x
        self.__initial_hitbox_y = hitbox_y
        self.__hitbox_x = hitbox_x
        self.__hitbox_y = hitbox_y
        self.window = surface

        self.__facing = 'down'

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
    def sprites(self):
        return self.__sprites

    @sprites.setter
    def sprites(self, sprites):
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
    def initial_hitbox_x(self):
        return self.__initial_hitbox_x

    @property
    def initial_hitbox_y(self):
        return self.__initial_hitbox_y

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
    def facing(self):
        return self.__facing

    @facing.setter
    def facing(self, facing):
        self.__facing = facing

    def attack(self, target):
        if target.health > 0:
            target.health -= self.damage

    def move(self, target):
        if self.x_position <= int(target.x_position):
            self.x_position += 3
        elif self.x_position > int(target.x_position):
            self.x_position -= 3

        if self.y_position <= int(target.y_position):
            self.y_position += 3
        elif self.y_position > int(target.y_position):
            self.y_position -= 3
        
        self.facing_calc(target)
        
    def facing_calc(self, target):
        if target.y_position - 3 <= self.y_position <= target.y_position + 3:
            self.hitbox_x = self.initial_hitbox_y
            self.hitbox_y = self.initial_hitbox_x
            if self.x_position < target.x_position:
                self.facing = 'right'
            else:
                self.facing = 'left'
        else:
            self.hitbox_x = self.initial_hitbox_x
            self.hitbox_y = self.initial_hitbox_y
            if self.y_position <= target.y_position:
                self.facing = 'down'
            else:
                self.facing = 'up'

    def reset(self, x_position, y_position):
        self.x_position = x_position
        self.y_position = y_position

    def draw(self):
        self.window.draw_scaled_image(self.sprites[self.facing],
                    self.__hitbox_x, self.__hitbox_y, 
                    self.__x_position, self.__y_position)
