from API_REST.model.tipo_bebida import TipoBebida
class Bebida:
    def __init__(self, nome, teor, tipo_bebida:TipoBebida, id=None):
        self.__nome = nome
        self.__teor = teor
        self.__tipo_bebida = tipo_bebida
        self.__id = id

