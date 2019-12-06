import MySQLdb

from crud_mysql.models.Cliente import Cliente

class ClienteDAO:

    def __init__(self):
        self.con = MySQLdb.connect(host='mysql.topskills.study',
                              database='topskills03',
                              user='topskills03',
                              passwd='Yuri2019')
        self.cursor = self.con.cursor()

    def salvar_cliente(self, cliente:Cliente):
        self.cursor.execute(f'insert into clientes values (default, "{cliente.nome}", "{cliente.sobrenome}", "{cliente.cpf}")')
        self.con.commit()

    def ler_clientes(self):
        lista = []
        self.cursor.execute('select * from clientes')
        for p in self.cursor.fetchall():
            lista.append(Cliente(p[1], p[2], p[3], p[0]))
        return lista

    def ler_cliente_by_id(self, id):
        self.cursor.execute(f'select * from clientes where cd_cliente = {id}')
        p = self.cursor.fetchone()
        return Cliente(p[1], p[2], p[3], p[0])

    def excluir_cliente_by_id(self, id):
        self.cursor.execute(f'delete from clientes where cd_cliente = {id}')
        self.con.commit()

    def editar_cliente_by_id(self, cliente:Cliente):
        self.cursor.execute(f'update clientes set nome_cliente = "{cliente.nome}", sobrenome_cliente = "{cliente.sobrenome}", ds_cpf = "{cliente.cpf}" where cd_cliente = {cliente.id}')
        self.con.commit()

