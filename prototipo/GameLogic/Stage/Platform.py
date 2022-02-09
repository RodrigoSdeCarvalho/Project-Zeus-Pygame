class Platform:
    def __init__(self, x_pos: int, y_pos: int, width: int, height: int, color):
        self.__x_pos: x_pos
        self.__y_pos: y_pos
        self.__width: width
        self.__height: height
        self.__color: color
    
    @property
    def x_pos(self):
        return self.__x_pos

    @x_pos.setter
    def x_pos(self, x_pos):
        self.__x_pos = x_pos

    @property
    def y_pos(self):
        return self.__y_pos

    @y_pos.setter
    def y_pos(self, y_pos):
        self.__y_pos = y_pos

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

    #Colocar plataforma apenas nas posições y = 150, 300 ou 450, devido ao jump = 150px