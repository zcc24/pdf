#coding=utf-8
import MySQLdb
class dbexecute():
    def __init__(self):
        pass
    def select(self,sql):
        self.sql=sql
        self.conn=MySQLdb.connect(host='127.0.0.1',port=3306,user='root',passwd='xlndxwh',db='detector',charset='utf8')
        self.cur=self.conn.cursor()
        aa=self.cur.execute(self.sql)
        info=self.cur.fetchmany(aa)
        return info
    def close(self):
        if(self.conn):
            try:
                if(type(self.cur)=='object'):
                    self.cur.close()
                if(type(self.conn)=='object'):
                    self.conn.close()
            except Exception,data:
                self.logger.warn("close database exception, %s,%s,%s" % (data, type(self._cursor), type(self._conn)))
