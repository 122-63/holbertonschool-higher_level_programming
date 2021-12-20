#!/usr/bin/python3
"""
 lists all cities from the database hbtn_0e_4_usa
 take 3 arguments: mysql username, mysql password and database name
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], password=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELET cities.id, cities.name, states.name FROM cities"
                "INNER JOIN states ON states.id = cities.state_id"
                "ORDER BY cities.id ASC")
    for cities in cur.fetchall():
        print(cities)
    cur.close()
    db.close()