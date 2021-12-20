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
    cur.execute("SELECT cities.name FROM cities "
                "INNER JOIN states ON states.id = cities.state_id "
                "WHERE states.name LIKE BINARY '%{}%' "
                "ORDER BY cities.id")
    print(", ".join([cty[2] for cty in cur.fetchall()
                     if cty[4] == sys.argv[4]]))
    cur.close()
    db.close()
