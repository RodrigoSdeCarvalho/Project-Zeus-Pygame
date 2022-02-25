class Platform:
    def __init__(self, x_position: int, y_position: int, hitbox_x: int, 
                hitbox_y: int, sprite, width: int, height: int, color: str, surface):
        self.__x_position = x_position
        self.__y_position = y_position
        self.__hitbox_x = hitbox_x
        self.__hitbox_y = hitbox_y
        self.__sprite = sprite
        self.__width: width
        self.__height: height
        self.__color: color
        self.window = surface

    @property
    def x_position(self):
        return self.__x_position

    # @x_position.setter
    # def x_position(self, x_position):
    #     self.__x_position = x_position

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
    def y_position(self):
        return self.__y_position

    @y_position.setter
    def y_position(self, y_position):
        self.__y_position = y_position
        
    @property
    def sprite(self):
        return self.__sprite

    @sprite.setter
    def sprite(self, sprite):
        self.__sprite = sprite

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    def draw(self): #Erro
        self.window.draw_scaled_image(self.__sprite, 
                    self.__hitbox_x, self.__hitbox_y, 
                    self.__x_position, self.__y_position)
    # #Colocar plataforma apenas nas posições y = 150, 300 ou 450, devido ao jump = 150px
