from TRABALHO.model.pessoa import Pessoa

class Trabalhador(Pessoa):
    def __init__(self, nome, idade, nome_cargo, salario, id = None, id_pessoa = None):
        super().__init__(nome, idade)
        self.__nome_cargo = nome_cargo
        self.__salario = salario
        self.__id = id
        self.__id_pessoa = id_pessoa

    def get_nome_cargo(self):
        return self.__nome_cargo

    def get_salario(self):
        return self.__salario

    def get_id(self):
        return self.__id

    def get_id_pessoa(self):
        return self.__id_pessoa


