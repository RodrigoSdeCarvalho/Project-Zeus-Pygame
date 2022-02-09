class Stage:
    def __init__(self, level: int, difficulty: int):
        self.__level = level 
        self.__difficulty = difficulty

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, level):
        self.__level = level

    @property
    def difficulty(self):
        return self.__difficulty

    @difficulty.setter
    def difficulty(self, difficulty):
        self.__difficulty = difficulty
