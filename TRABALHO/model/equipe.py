class Equipe:

    def __init__(self, nome, id_linguagem, id = None):
        self.__nome = nome
        self.__id_linguagem = id_linguagem
        self.__id = id

    def get_nome(self):
        return self.__nome

    def get_id_linguagem(self):
        return self.__id_linguagem

    def get_id(self):
        return self.__id
