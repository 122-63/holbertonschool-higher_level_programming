#!/usr/bin/python3
"""
takes in the name of a state as an argument and
lists all cities of that state
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], password=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name FROM cities\
                LEFT JOIN states ON cities.state_id = states.id ORDER BY\
                cities.id ASC""")
    print(", ".join([ct[2] for ct in c.fetchall() if ct[4] == argv[4]]))
    cur.close()
    db.close()
