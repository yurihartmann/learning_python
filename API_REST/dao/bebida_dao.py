from API_REST.dao.base_dao import BaseDao
from API_REST.model.bebida import Bebida
from API_REST.model.tipo_bebida import TipoBebida

class BebidaDao(BaseDao):
    def inserir(self, nome, teor, id_tipo_bebida):
        comando_sql_insert = f'insert into BEBIDA_FESTA value (default, "{nome}", "{teor}", "{id_tipo_bebida}")'
        return super().inserir(comando_sql_insert)

    def alterar(self,id , nome, teor, id_tipo_bebida):
        comando_sql_alterar = f'update BEBIDA_FESTA set NOME = "{nome}", TEOR = "{teor}", TIPO_BEBIDA_ID = "{id_tipo_bebida}" where ID = "{id}"'
        super().alterar(comando_sql_alterar)
    
    def deletar(self, id):
        comando_sql_deletar = f'delete from BEBIDA_FESTA where ID = {id}'
        super().inserir(comando_sql_deletar)

    def listar(self):
        lista_bebidas = []
        comando_sql_listar = """SELECT 
                                B.NOME
                                ,B.TEOR
                                ,TB.NOME
                                ,TB.DESCRICAO
                                ,TB.ID
                                ,B.ID
                                FROM BEBIDA_FESTA AS B
                                JOIN TIPO_BEBIDA AS TB
                                ON B.TIPO_BEBIDA_ID = TB.ID"""
                                
        lista_tuplas = super().listar(comando_sql_listar)
        for l in lista_tuplas:
            tipo_bebida = TipoBebida(l[2], l[3], l[4]).__dict__
            bebida = Bebida( l[0], l[1], tipo_bebida, l[5] )
            lista_bebidas.append(bebida.__dict__)
        return lista_bebidas



    def buscar_por_id(self, id):
        comando_sql_buscar_id = f'''SELECT 
                                B.NOME
                                ,B.TEOR
                                ,TB.NOME
                                ,TB.DESCRICAO
                                ,TB.ID
                                ,B.ID
                                FROM BEBIDA_FESTA AS B
                                JOIN TIPO_BEBIDA AS TB
                                ON B.TIPO_BEBIDA_ID = TB.ID
                                where B.ID = {id}'''
        l = super().buscar_por_id(comando_sql_buscar_id)
        tipo_bebida = TipoBebida(l[2], l[3], l[4]).__dict__
        bebida = Bebida(l[0], l[1], tipo_bebida, l[5])
        return bebida.__dict__