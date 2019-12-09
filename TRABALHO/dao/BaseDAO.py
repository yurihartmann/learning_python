import MySQLdb


class BaseDao:
    def __init__(self):
        self.con = MySQLdb.connect(host='mysql.topskills.study',
                                   database='topskills03',
                                   user='topskills03',
                                   passwd='Yuri2019')
        self.cursor = self.con.cursor()
