class Cliente:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name.title()

    @name.setter
    def name(self, name):
        self.__name = name
