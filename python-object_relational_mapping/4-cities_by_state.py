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
        "SELECT cities.id, cities.name, states.name",
        "FROM cities JOIN states ON cities.state_id = states.id"
        ])
    cur.execute(query)
    cities = cur.fetchall()
    for city in cities:
        print(city)
    cur.close()
    db.close()
