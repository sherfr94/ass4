import sqlite3
import os
import sys

def main(args):
    input = args[1]
    with open(input) as input:
        for line in input:
            print(line, end='')

    os.remove("world.db")
    if not os.path.isfile("world.db"): #TODO: remove
        db = open("world.db", "w+")

    dbcon = sqlite3.connect('world.db')

    with dbcon:
        cursor = dbcon.cursor()
        cursor.execute("CREATE TABLE tasks("
                       "id INT PRIMARY KEY, "
                       "name TEXT NOT NULL, "
                       "worker_id INT, "
                       "time_to_make INT, "
                       "resource_name TEXT NOT NULL, "
                       "resource_amount INT, "
                       "FOREIGN KEY(worker_id) REFERENCES workers(id), "
                       "FOREIGN KEY(resource_name) REFERENCES resources(name)"
                       ")")

        cursor.execute("CREATE TABLE workers("
                       "id INT PRIMARY KEY, "
                       "name TEXT NOT NULL, "
                       "status TEXT NOT NULL" 
                       ")")

        cursor.execute("CREATE TABLE resources("
                       "name TEXT NOT NULL PRIMARY KEY, "
                       "amount INT"
                       ")")

    #     # let's get all students and print their entries
    # cursor.execute("SELECT * FROM Students");
    # studentslist = cursor.fetchall()
    # print("All students as list:")
    # print(studentslist)


if __name__ == '__main__':
    main(sys.argv)