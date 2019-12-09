class Equipe_trabalhadores:
    def __init__(self, equipe, trabalhador):
        self.__equipe = equipe
        self.__trabalhador = trabalhador

    # getter
    def get_equipe(self): 
        return self.__equipe 

    def get_trabalhador(self):
        return self.__trabalhador
      
    # setter 
    def set_equipe(self, equipe): 
        self.__equipe = equipe 

    def set_trabalhador(self, trabalhador):
        self.__trabalhador = trabalhador