import mysql.connector


def getConnection():
    conn = mysql.connector.connect(host='localhost', user='root', passwd='Admin1234+', db='PAIIS07')
    return conn


def closeConnection(conn):
    conn.close()
