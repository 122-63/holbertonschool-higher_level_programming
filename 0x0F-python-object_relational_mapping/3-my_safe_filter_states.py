#!/usr/bin/python3
"""
takes in arguments and displays all values in the
states table of hbtn_0e_0_usa
take 4 arguments: mysql username, mysql password,
database name and state name searched
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], password=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    for states in cur.fetchall():
        if states[1] == sys.argv[4]:
            print(states)
