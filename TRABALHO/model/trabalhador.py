class Trabalhador:
    def __init__(self, trabalhador, pessoa, numero, valor):
        self.__trabalhador = trabalhador
        self.__pessoa = pessoa
        self.__numero = numero
        self.__valor = valor

    # getter
    def get_trabalhador(self): 
        return self.__trabalhador 

    def get_pessoa(self):
        return self.__pessoa

    def get_numero(self):
        return self.__numero
    
    def get_valor(self):
    return self.__valor
      
    # setter 
    def set_trabalhador(self, trabalhador): 
        self.__trabalhador = trabalhador 

    def set_pessoa(self, pessoa):
        self.__pessoa = pessoa

    def set_numero(self, numero):
        self.__numero = numero

    def set_valor(self, valor):
        self.__valor = valor