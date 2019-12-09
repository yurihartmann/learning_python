from TRABALHO.dao.baseDAO import BaseDAO
from TRABALHO.model.trabalhador import Trabalhador


class TrabalhadorDAO(BaseDAO):

    def listar(self):
        lista = []
        self.cursor.execute(f'select * from trabalhador, pessoa where cd_trabalhador = cd_pessoa')
        for t in self.cursor.fetchall():
            print(t)
            lista.append(Trabalhador(t[5],t[6],t[2],t[3],t[0], t[1]))
        return lista


    def inserir(self, trabalhador:Trabalhador):
        self.cursor.execute(f'insert into pessoa values (DEFAULT, "{trabalhador.get_nome()}", "{trabalhador.get_idade()}")')
        self.con.commit()
        id = self.cursor.lastrowid
        self.cursor.execute(f'insert into trabalhador values (DEFAULT, "{id}", "{trabalhador.get_nome_cargo()}", "{trabalhador.get_salario()}")')
        self.con.commit()

    def update(self, trabalhador:Trabalhador):

        self.cursor.execute(f'update pessoa set nm_pessoa = "{trabalhador.get_nome()}", vl_idade = "{trabalhador.get_idade()}" where cd_linguagem = {trabalhador.get_id_pessoa()}')
        self.con.commit()
        self.cursor.execute(f'update trabalhador set nm_linguagem = "{trabalhador.get_nome()}" where cd_linguagem = {trabalhador.get_id()}')
        self.con.commit()

    # def delete(self, id):
    #     self.cursor.execute(f'delete from linguagem_de_programacao where cd_linguagem = {id}')
    #     self.con.commit()
    #
    # def dados_by_id(self, id):
    #     self.cursor.execute(f'select * from linguagem_de_programacao where cd_linguagem = {id}')
    #     l = self.cursor.fetchone()
    #     return Linguagem(l[1], l[0])


t = TrabalhadorDAO()


t.listar()