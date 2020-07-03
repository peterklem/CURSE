from Individual import *

class Student(Individual):
    '''Contains functions that pertain to students'''

    def __init__(self):
        self._schedule = []  # Student schedule
        print('A new student has been created')

    def search_course(self, course_name):
        '''Searches courses by name'''
        results = []
        # Search SQL database for matches, add to results
        return results

    def add_course(self, course_id):
        '''Adds this student to a course specified by course ID'''
        course_id = input("Enter the CRN of the course to add: ")
        courseAddStart = 'SELECT * FROM COURSE WHERE CRN = '
        courseAddFinal = (courseAddStart + courseAdd)
        cursor.execute(courseFinal)
        result = cursor.execute()
        #need to add to students database

    def drop_course(self, course_id):
        '''Removes this student to a course specified by course ID'''
        courseRemove = input("Enter the CRN of the course to remove: ")
        courseRemoveStart = 'DELETE FROM SCHEDULE WHERE CRN = '
        courseRemoveFinal = (courseRemoveStart + courseRemove)
        cursor.execute(courseRemoveFinal)

    def print_schedule(self):
        '''Prints out student's schedule'''
        for i in self._schedule:
            print(i)
