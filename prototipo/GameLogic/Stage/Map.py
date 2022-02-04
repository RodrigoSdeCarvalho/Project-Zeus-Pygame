class Map:
    def __init__(self, background: str, platforms: list):
        self.__background = background 
        self.__platforms = platforms

    @property
    def background(self):
        return self.__background

    @background.setter
    def background(self, background):
        self.__background = background

    @property
    def platforms(self):
        return self.__platforms

    @platforms.setter
    def platforms(self, platforms):
        self.__platforms = platforms
