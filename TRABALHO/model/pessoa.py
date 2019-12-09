class Pessoa:
    def __init__(self, codigo, nome, idade):
        self.__codigo = codigo
        self.__nome = nome
        self.__idade = idade

    # getter
    def get_codigo(self): 
        return self.__codigo 

    def get_nome(self):
        return self.__nome

    def get_idade(self):
        return self.__idade
      
    # setter 
    def set_codigo(self, codigo): 
        self.__codigo = codigo 

    def set_nome(self, nome):
        self.__nome = nome

    def set_idade(self, idade):
        self.__idade = idade