import MySQLdb

def connection():
    conn = MySQLdb.connect(host="localhost",
                           user = "root",
                           passwd = "mklmkl",
                           db = "pythonprogramming")
    c = conn.cursor()

    return c, conn
