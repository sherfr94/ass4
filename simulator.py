import sys
import os
import sqlite3
import atexit


def main():
    check = os.path.isfile("world.db")
    if (check == True):
        dbcon = sqlite3.connect("world.db")

        with dbcon:
            cursor = dbcon.cursor()
            cursor.execute("SELECT * FROM Tasks")
            taskslist = cursor.fetchall()
            if (taskslist == []):
                check = False

            while (check):
                for task in taskslist:
                    cursor.execute("SELECT worker_id FROM Tasks WHERE task_id=(?)", (task[0],))
                    res1 = cursor.fetchone()  # worker_id
                    cursor.execute("SELECT status, name FROM Workers WHERE worker_id=(?)", (res1[0],))
                    res2 = cursor.fetchone()  # status,name
                    if (res2[0] == "busy"):
                        cursor.execute("SELECT task_id FROM Tasks WHERE worker_id=(?)", (res1[0],))
                        res3 = cursor.fetchone() #taskid
                        if (res3[0] == task[0]):  # work on me


                            if (task[3] == 0):  # timetowork =0
                                cursor.execute("DELETE FROM Tasks "
                                               "WHERE task_id=(?)", (task[0],))

                                cursor.execute("UPDATE Workers SET status=(?) "
                                               "WHERE worker_id=(?)", ("idle", res1[0],))
                                print(res2[1] + " says: All Done!")
                            else:  # timetowork!=0
                                cursor.execute("UPDATE Tasks SET time_to_make=(?) "
                                               "WHERE task_id=(?)", (task[3] - 1, task[0],))
                                print(res2[1] + " is busy " + task[1] + "...")



                    else:  # idle
                        cursor.execute("UPDATE Workers SET status=(?) "
                                       "WHERE worker_id=(?)", ("busy", res1[0],))
                        print(res2[1] + " says: work work")

                    cursor.execute("SELECT * FROM Tasks")
                    taskslist = cursor.fetchall()

                check = os.path.isfile("world.db")
                if (check == True):
                    cursor.execute("SELECT * FROM Tasks")
                    taskslist = cursor.fetchall()
                    if (taskslist == [] or taskslist==None):
                        check = False

                #
                #
                #
                #
                #
                #
                # #change worker to busy and print work work
                # for worker in workers:
                #     # print("in for")
                #     if(worker[2] == "idle"):
                #         cursor.execute("SELECT task_id, time_to_make "
                #                        "FROM Tasks "
                #                        "WHERE worker_id=(?)", (worker[0],))
                #
                #         res = cursor.fetchone()
                #         # print(str(res))
                #
                #         if res != [] and res!=None:
                #             cursor.execute("UPDATE Workers SET status=(?)"
                #                            "WHERE worker_id=(?)", ("busy", worker[0], ))
                #             print(str(worker[1]) + ' says: work work')
                #             # cursor.execute("UPDATE Tasks SET time_to_make=(?) "
                #             #                 "WHERE task_id=(?)", (res[1]-1, res[0],))
                #
                #     else: # busy worker
                #         cursor.execute("SELECT task_id, time_to_make, task_name "
                #                        "FROM Tasks "
                #                        "WHERE worker_id=(?)", (worker[0],))
                #
                #         res = cursor.fetchone()
                #
                #         # cursor.execute("UPDATE Tasks SET time_to_make=(?)"
                #         #                "WHERE task_id=(?)", (res[1] - 1, res[0],))
                #         #
                #
                #         #check if time to make =0
                #         if(res[1] ==0):
                #             cursor.execute("UPDATE Workers SET status=(?)"
                #                            "WHERE worker_id=(?)", ("idle", worker[0],))
                #
                #             cursor.execute("DELETE FROM Tasks "
                #                            "WHERE task_id=(?)", (res[0],))
                #
                #             print(worker[1]+" says: All Done!")
                #
                #             # cursor.execute("SELECT task_id, time_to_make "
                #             #                "FROM Tasks "
                #             #                "WHERE worker_id=(?)", (worker[0],))
                #             #
                #             # res1 = cursor.fetchone()
                #             # # print(str(res))
                #             #
                #             # if res1 != [] and res1 != None:
                #             #     cursor.execute("UPDATE Workers SET status=(?)"
                #             #                    "WHERE worker_id=(?)", ("busy", worker[0],))
                #             #     print(str(worker[1]) + ' says: work work')
                #             #     # cursor.execute("UPDATE Tasks SET time_to_make=(?) "
                #             #     #                 "WHERE task_id=(?)", (res[1]-1, res[0],))
                #
                #
                #
                #         #time to make !=0
                #         else:
                #             cursor.execute("UPDATE Tasks SET time_to_make=(?)"
                #                            "WHERE task_id=(?)", (res[1] - 1, res[0],))
                #             print(worker[1]+" is busy "+res[2]+"...")
                #
                #         check = os.path.isfile("world.db")
                #         if (check == True):
                #             cursor.execute("SELECT * FROM Tasks")
                #             taskslist = cursor.fetchall()
                #             if (taskslist == []):
                #                 check = False
                #


if __name__ == '__main__':
    main()
