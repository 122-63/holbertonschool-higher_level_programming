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
    cur.execute("SELET * FROM states")
    for states in cur.fetchall():
        if states[1] == sys.argv[4]:
            print(states)
    cur.close()
    db.close()
