from Individual import *
from database import *

class Instructor(Individual):
    '''Contains functions for use of an instructor or professor'''

    def __init__(self):
        self.schedule = []  # Instructor schedule
        print('A new instructor has been created')

    def search_course(self, course_name):
        '''Searches courses by name'''
        results = []
        # Search SQL database for matches, add to results
        return results

    def print_student_schedule(self, student):
        # Need SQL
        for course in student.schedule:
            print(course)

    def print_class_roster(self):
        roster = input("Enter the class roster (CRN) to print: ") 
        rosterQuery = 'SELECT STUDENT_LIST FROM COURSE WHERE CRN = ' 
        rosterQueryFinal = (rosterQuery + roster)
        cursor.execute(rosterQueryFinal)
        query_result = cursor.fetchall()
        for i in query_result:
            print(i)