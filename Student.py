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
        def convertTuple(tup): #used for tuple conversion https://www.geeksforgeeks.org/python-program-to-convert-a-tuple-to-a-string/
            str = ''.join(tup)
            return str
        student_ID = input("Enter your student ID: ")
        course_ID = input("Enter the ID of the course to add: ")
        course_ID = ('"' + course_ID + '"')
        student_ID = ('"' + student_ID + '"')
        studentQuery = ('SELECT COURSES FROM STUDENT WHERE ID = ' + student_ID)
        cursor.execute(studentQuery)
        hold = cursor.fetchall()
        newlist = list(hold)
        holdResult = newlist[0]
        str = convertTuple(holdResult)
        str = ('"' + str + '"')
        courseAddQuery = ('UPDATE STUDENT SET COURSES = ' + str + '"-"' + course_ID + ' WHERE ID = ' + student_ID)
        cursor.execute(courseAddQuery)
        studentQuery = ('SELECT COURSES FROM STUDENT WHERE ID = ' + student_ID)
        cursor.execute(studentQuery)
        studentAddQuery = ('UPDATE COURSE SET STUDENT_LIST = ' + str + '"-"' + student_ID + ' WHERE CRN = ' + course_ID)
        cursor.execute(studentAddQuery)

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
