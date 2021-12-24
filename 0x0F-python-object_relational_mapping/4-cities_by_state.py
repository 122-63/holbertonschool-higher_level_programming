#!/usr/bin/python3
"""
 lists all cities from the database hbtn_0e_4_usa
 take 3 arguments: mysql username, mysql password and database name
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities"
                "INNER JOIN states ON cities.state_id = states.id;")
    for city in cur.fetchall():
        print(city)
    cur.close()
    db.close()
