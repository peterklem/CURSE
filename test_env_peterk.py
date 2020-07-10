from Individual import *
from Student import *
from Instructor import *
from Admin import *
import sqlite3

if __name__ == '__main__':

    db = sqlite3.connect('assignment2.db')
    cursor = db.cursor()
    command = "SELECT * FROM COURSE WHERE INSTRUCTOR LIKE '%carp%'"
    cursor.execute(command)

    results = cursor.fetchall()
    print(results)


    db.close()
