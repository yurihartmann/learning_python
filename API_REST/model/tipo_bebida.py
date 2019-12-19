class TipoBebida:
    def __init__(self, nome, descricao, id=None):
        self.__nome = nome
        self.__descricao = descricao
        self.__id = id

    def __repr__(self):
        return self.__nome