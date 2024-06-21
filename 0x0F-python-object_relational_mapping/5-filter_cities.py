#!/usr/bin/python3
import MySQLdb
from sys import argv
'''module to get all cities'''


if __name__ == '__main__':

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        database=argv[3])

    cursor = db.cursor()
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id WHERE states.name = %s
    ORDER BY cities.id ASC;
    """
    cursor.execute(query, (argv[4],))
    rows = cursor.fetchall()
    cities_names = [row[0] for row in rows]
    print(", ".join(cities_names))
    cursor.close()
    db.close()
