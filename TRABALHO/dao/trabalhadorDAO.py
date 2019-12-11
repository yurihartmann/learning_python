from dao.baseDAO import BaseDAO
from model.trabalhador import Trabalhador


class TrabalhadorDAO(BaseDAO):

    # LISTA TODOS OS TRABALHADORES
    def listar(self):
        lista = []
        self.cursor.execute(f'select * from trabalhador, pessoa where fk_pessoa = cd_pessoa')
        for t in self.cursor.fetchall():
            lista.append(Trabalhador(t[5],t[6],t[2],t[3],t[0], t[1]))
        return lista

    # INSERE UM TRABALHADOR NO BANCO DE DADOS
    def inserir(self, trabalhador:Trabalhador):
        self.cursor.execute(f'insert into pessoa values (DEFAULT, "{trabalhador.get_nome()}", "{trabalhador.get_idade()}")')
        self.con.commit()
        id = self.cursor.lastrowid
        self.cursor.execute(f'insert into trabalhador values (DEFAULT, "{id}", "{trabalhador.get_cargo()}", "{trabalhador.get_salario()}")')
        self.con.commit()

    # ALTUALIZA UM TRABALHADOR NO BANCO DE DADOS
    def update(self, trabalhador:Trabalhador):
        self.cursor.execute(f'update pessoa set nm_pessoa = "{trabalhador.get_nome()}", vl_idade = "{trabalhador.get_idade()}" where cd_pessoa = {trabalhador.get_id_pessoa()}')
        self.con.commit()
        self.cursor.execute(f'update trabalhador set nm_cargo = "{trabalhador.get_cargo()}", vl_salario = "{trabalhador.get_salario()}" where cd_trabalhador = {trabalhador.get_id()}')
        self.con.commit()

    # DELETA UM TRABALHADOR DO BANCO DE DADOS
    def delete(self, id_pessoa, id_trabalhador):
        self.cursor.execute(f'delete from trabalhador where cd_trabalhador = {id_trabalhador}')
        self.con.commit()
        self.cursor.execute(f'delete from pessoa where cd_pessoa = {id_pessoa}')
        self.con.commit()


    # BUSCA OS DADOS DE UM TRABALHADOR NO BANCO DE DADOS
    def dados_by_id(self, id_trabalhador):
        self.cursor.execute(f'select * from trabalhador t, pessoa p where t.fk_pessoa = p.cd_pessoa and t.cd_trabalhador = {id_trabalhador}')
        t = self.cursor.fetchone()
        return Trabalhador(t[5],t[6],t[2],t[3],t[0], t[1])
