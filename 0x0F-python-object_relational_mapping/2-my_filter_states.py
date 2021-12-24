#!/usr/bin/python3
"""
takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.

using four arguments: mysql username, mysql password, database name
and state name searched
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE '{}'ORDER BY id ASC"
                .format(argv[4]))
    for state in cur.fetchall():
        print(state)
    cur.close()
    db.close()
