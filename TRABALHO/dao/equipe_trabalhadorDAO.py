from TRABALHO.dao.baseDAO import BaseDAO
from TRABALHO.model.trabalhador import Trabalhador

class EquipeTrabalhadorDAO(BaseDAO):

    # insere uma pessoa em uma equipe
    def inserir(self, id_equipe, id_trabalhador):
        self.cursor.execute(f'INSERT INTO equipe_trabalhador VALUES ({id_equipe},{id_trabalhador})')
        self.con.commit()

    # deleta uma pessoa de uma equipe
    def deletar(self, id_equipe, id_trabalhador):
        self.cursor.execute(f'DELETE from equipe_trabalhador WHERE fk_equipe = {id_equipe} and fk_trabalhador = {id_trabalhador}')
        self.con.commit()

    def lista_pessoas_by_id_equipe(self, id_equipe):
        lista = []
        self.cursor.execute(f'select p.cd_pessoa, p.nm_pessoa, p.vl_idade, t.nm_cargo, t.vl_salario, t.cd_trabalhador, p.cd_pessoa from equipe_trabalhador et, trabalhador t, pessoa p where et.fk_trabalhador = t.cd_trabalhador and t.fk_pessoa = p.cd_pessoa and et.fk_equipe = {id_equipe}')
        for t in self.cursor.fetchall():
            lista.append(Trabalhador(t[1], t[2], t[3],t[4], t[5], t[0]))
        return lista


