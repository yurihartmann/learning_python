from TRABALHO.dao.baseDAO import BaseDAO
from TRABALHO.model.equipe import Equipe

class EquipeDAO(BaseDAO):

    # LISTA TODOS AS LINGUAGEM
    def listar(self):
        lista = []
        self.cursor.execute('select * from equipe')
        for e in self.cursor.fetchall():
            lista.append(Equipe(e[1], e[2], e[0]))
        return lista

    # INSERE UMA LINGUAGEM NO BANCO DE DADOS
    def inserir(self, equipe:Equipe):
        self.cursor.execute(f'insert into equipe values (DEFAULT, "{equipe.get_nome()}", "{equipe.get_id_linguagem()}")')
        self.con.commit()

    # ALTUALIZA UMA LINGUAGEM NO BANCO DE DADOS
    def update(self, equipe:Equipe):
        self.cursor.execute(f'update equipe set nm_equipe = "{equipe.get_nome()}", fk_linguagem = "{equipe.get_id_linguagem()}" where cd_equipe = {equipe.get_id()}')
        self.con.commit()

    # DELETA UMA LINGAGUEM DO BANCO DE DADOS
    def delete(self, id):
        # falta deletar equipe_trabalhador antes
        self.cursor.execute(f'delete from equipe where cd_equipe = {id}')
        self.con.commit()

    # BUSCA OS DADOS DE UMA LINGUAGEM NO BANCO DE DADOS
    def dados_by_id(self, id):
        self.cursor.execute(f'select * from equipe where cd_equipe = {id}')
        e = self.cursor.fetchone()
        return Equipe(e[1], e[2], e[0])



