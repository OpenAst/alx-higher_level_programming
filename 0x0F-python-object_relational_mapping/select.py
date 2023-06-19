#!/usr/bin/python3
"""
This script creates gns table
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Acess to the database 
    and get the gns table
    """

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
            passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM gns ORDER BY matric_no ASC")

    rows = cur.fetchall()

    for row in rows:
        print(row)
