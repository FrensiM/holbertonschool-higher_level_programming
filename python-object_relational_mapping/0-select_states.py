#!/usr/bin/python3
'''script that list all state from db hbtn_0e_0_usa'''
import MySQLdb
import sys


if __name__ == '__main__':
    
    db = MySQLdb.connect(host="localhost", port="3306",
                         user="sys.argv[1]", passwd="sys.argv[2]",
                         db="sys.argv[3]", charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM state ORDER BY state.id")
    res =cur.fetchall()
    for rows in res:
        print(rows)
    cur.close()
    db.close()
