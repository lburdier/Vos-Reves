import pymysql
import csv
from datetime import datetime
def connect():
    conn=pymysql.connect(host="localhost",user="root",password="",db="remboursement")
    return conn

conn = pymysql.connect(
    host = "localhost",
    user = "root",
    password="",
)

cur = conn.cursor()

def CreateBaseMySQL():
    cur.execute("DROP DATABASE IF EXISTS remboursement")
    cur.execute("CREATE DATABASE remboursement")
    cur.execute("USE remboursement")

#Table remboursejour
    cur.execute("""CREATE TABLE remboursejour (numticket varchar(10) NOT NULL,
            date varchar(10) NOT NULL,
            prixnuit decimal(5,2) NOT NULL,
            premierrepas varchar(8) NOT NULL,
            deuxiemerepas varchar(8) NOT NULL,
            prixplein decimal(5,2) NOT NULL,
            prixpeage decimal(5,2) NOT NULL,
            PRIMARY KEY (numticket))""")

          

    conn.commit()
    cur.close()
    conn.close()
