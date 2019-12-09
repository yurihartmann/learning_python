class Linguagem:
    def __init__(self, linguagem, numero):
        self.__linguagem = linguagem
        self.__numero = numero

    # getter
    def get_linguagem(self): 
        return self.__linguagem 

    def get_numero(self):
        return self.__numero
      
    # setter 
    def set_linguagem(self, linguagem): 
        self.__linguagem = linguagem 

    def set_numero(self, numero):
        self.__numero = numero