#!/usr/bin/python3
'''module to get all states'''
import MySQLdb
from sys import argv


if __name__ == '__main__':

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        database=argv[3])

    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name\
    LIKE BINARY '{:s}' ORDER BY id ASC".format(argv[4])
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
