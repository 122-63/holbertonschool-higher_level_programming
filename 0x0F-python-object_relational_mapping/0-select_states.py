#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa
using three arguments: mysql username, mysql password and database
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], password=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    for states in cur.fetchall():
        print(states)
    cur.close()
    db.close()
