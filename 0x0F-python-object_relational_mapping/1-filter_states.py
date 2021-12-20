#!/usr/bin/python3
"""
lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
using three arguments: mysql username, mysql password and database
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQL.connect(user=argv[1], password=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")
    for states in cur.fetchall():
        if states[1][0] == "N":
            print(states)
    cur.close()
    db.close()
