class Linguagem:
    def __init__(self, nome, id = None):
        self.__nome = nome
        self.__id = id

    # getter
    def get_nome(self):
        return self.__nome

    def get_id(self):
        return self.__id
      
    # setter 
    def set_nome(self, nome):
        self.__nome = nome

    def set_id(self, id):
        self.__id = id