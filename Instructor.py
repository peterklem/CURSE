from Individual import *

class Instructor(Individual):
    '''Contains functions for use of an instructor or professor'''

    def __init__(self, id):
        self.__id = id
        self.schedule = []  # Instructor schedule
        print('A new instructor has been created')


    def print_class_roster(self, course_id):
       
        def r_Print(roster):
            cursor.execute (rosterQueryFinal)
        roster = input("Enter the class roster (CRN) to print: ") 
        rosterQuery = 'SELECT STUDENT_LIST FROM COURSE WHERE CRN = ' 
        rosterQueryFinal = (rosterQuery + roster)
        r_Print(roster)


    def print_schedule(self):
        '''Gets the schedule of a professor'''
        print('SCHEDULE FOR INSTRUCTOR ' + str(self.__id) + ': \n\n')
        db = sqlite3.connect('assignment2.db')
        cursor = db.cursor()
        command = "SELECT COURSES FROM INSTRUCTOR WHERE ID = " + str(self.__id) + ";"
        cursor.execute(command)

        student_course_ids = cursor.fetchall()
        course_ids = student_course_ids[0][0]
        ids_split = course_ids.split()

        for crn in ids_split:
            command = "SELECT * FROM COURSE WHERE CRN = " + crn + ";"
            cursor.execute(command)
            course_data = cursor.fetchall()
            print('Title: ' + course_data[0][0])
            print('CRN: ' + str(course_data[0][1]))
            print('Department: ' + course_data[0][2])
            #print('Instructor: ' + course_data[0][3])
            print('Start Time: ' + str(course_data[0][4]))
            print('End Time: ' + str(course_data[0][5]))
            print('Days: ' + course_data[0][6])
            print('Semester: ' + course_data[0][7])
            print('Credits: ' + str(course_data[0][8]) + '\n\n')

        db.close()