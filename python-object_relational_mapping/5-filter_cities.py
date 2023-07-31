#!/usr/bin/python3
"""module for gettin states that start with letter n"""
import MySQLdb
import sys


if __name__ == '__main__':
    u = sys.argv[1]
    p = sys.argv[2]
    d = sys.argv[3]
    db = MySQLdb.connect(host='localhost', port=3306, user=u, passwd=p, db=d,
                         charset='utf8')
    cur = db.cursor()
    query = " ".join([
        "SELECT cities.name",
        "FROM cities JOIN states ON cities.state_id = states.id",
        "WHERE states.name LIKE %s"
        ])
    cur.execute(query, (sys.argv[4], ))
    cities = cur.fetchall()
    i = 0
    for i in range(len(cities)):
        if i == len(cities) - 1:
            print("{}".format(cities[i][0]), end='')
        else:
            print("{}, ".format(cities[i][0]), end='')
    print()
    cur.close()
    db.close()
