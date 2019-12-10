import MySQLdb

# CLASSE PARA FAZER A CONECAO COM O BANCO DE DADOS

class BaseDAO:
    def __init__(self):
        self.con = MySQLdb.connect(host='mysql.topskills.study',
                                   database='topskills10',
                                   user='topskills10',
                                   passwd='Gabriel2019')
        self.cursor = self.con.cursor()

    def get_con(self):
        return self.con

    def get_cursor(self):
        return self.cursor