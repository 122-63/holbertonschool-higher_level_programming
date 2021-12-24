#!/usr/bin/python3
"""
takes in the name of a state as an argument and
lists all cities of that state
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    count = 0
    db = MySQLdb.connect(user=argv[1], password=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name FROM cities\
                LEFT JOIN states ON cities.state_id = states.id ORDER BY\
                cities.id ASC""")
    for city in cur.fetchall():
        if city[2] == argv[4]:
            if count > 0:
                print(", ", end="")
            print(city[1], end="")
            count = count + 1
    print()
    cur.close()
    db.close()
