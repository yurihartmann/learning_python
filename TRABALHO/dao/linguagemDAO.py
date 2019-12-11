from dao.baseDAO import BaseDAO
from model.linguagem import Linguagem


class LinguagemDAO(BaseDAO):


    # LISTA TODOS AS LINGUAGEM
    def listar(self):
        lista = []
        self.cursor.execute('select * from linguagem_de_programacao')
        for l in self.cursor.fetchall():
            lista.append(Linguagem(l[1], l[0]))
        return lista

    # INSERE UMA LINGUAGEM NO BANCO DE DADOS
    def inserir(self, linguagem:Linguagem):
        self.cursor.execute(f'insert into linguagem_de_programacao values (DEFAULT, "{linguagem.get_nome()}")')
        self.con.commit()

    # ALTUALIZA UMA LINGUAGEM NO BANCO DE DADOS
    def update(self, linguagem:Linguagem):
        self.cursor.execute(f'update linguagem_de_programacao set nm_linguagem = "{linguagem.get_nome()}" where cd_linguagem = {linguagem.get_id()}')
        self.con.commit()

    # DELETA UMA LINGAGUEM DO BANCO DE DADOS
    def delete(self, id):
        self.cursor.execute(f'delete from linguagem_de_programacao where cd_linguagem = {id}')
        self.con.commit()

    # BUSCA OS DADOS DE UMA LINGUAGEM NO BANCO DE DADOS
    def dados_by_id(self, id):
        self.cursor.execute(f'select * from linguagem_de_programacao where cd_linguagem = {id}')
        l = self.cursor.fetchone()
        return Linguagem(l[1], l[0])
