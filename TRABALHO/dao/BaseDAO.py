import MySQLdb


class BaseDAO:
    def __init__(self):
        self.con = MySQLdb.connect(host='mysql.topskills.study',
                                   database='topskills03',
                                   user='topskills03',
                                   passwd='Yuri2019')
        self.cursor = self.con.cursor()

    def get_con(self):
        return self.con

    def get_cursor(self):
        return self.cursor