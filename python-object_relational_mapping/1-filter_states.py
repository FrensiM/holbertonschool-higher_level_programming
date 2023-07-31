#!/usr/bin/python3
"""script that lists all states with a name
starting with N from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


if __name__ == '__main__':
<<<<<<< HEAD
    if len(sys.argv) <= 3:
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=sys.argv[1], passwd=sys.argv[2],
                             db=sys.argv[3], charset="utf8")
        cr = db.cursor()
        cr.execute("SELECT * FROM states")
        res = cr.fetchall()
        for rows in res:
            print(rows)
        cr.close()
        db.close()
=======

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], charset="utf8")
    cr = db.cursor()
    myQuery = " ".join([
        "SELECT * FROM states",
        "WHERE name LIKE BINARY 'N%'",
        "ORDER BY id ASC"])
    cr.execute(myQuery)
    res = cr.fetchall()
    for rows in res:
        print(rows)
    cr.close()
    db.close()
>>>>>>> 4c58391515582e480b2325ac2386ba2397ad0b6e
