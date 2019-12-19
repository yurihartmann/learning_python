import MySQLdb

from produto import Produto


class ProdutoDao():

    def __init__(self):
        self.conexao = MySQLdb.connect(host="mysql.topskills.study", database="topskills03", user="topskills03", passwd="Yuri2019" )
        self.cursor = self.conexao.cursor()

    def inserir(self, produto: Produto):

        if produto.tipo == 'fruta':
            produto.id_tipo = 1
        elif produto.tipo == 'verdura':
            produto.id_tipo = 2
        else:
            produto.id_tipo = 3

        sql = f" insert into produto value (default, {produto.id_tipo}, '{produto.nome}', '{produto.valor}' )"     
        self.cursor.execute(sql)
        self.conexao.commit()

    def listar_by_tipo_id(self, id_tipo):
        sql = f" select * from produto p , tipo_produto tp where p.fk_tipo_produto = tp.cd_tipo_produto and fk_tipo_produto = {id_tipo}"     
        self.cursor.execute(sql)
        lista = []
        for a in self.cursor.fetchall():
            lista.append(Produto(a[2], a[5], a[3]))
        return lista
