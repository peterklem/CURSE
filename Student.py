from Individual import *
from database import *

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

    def add_course(self):
        '''Adds this student to a course specified by course ID'''
        def convertTuple(tup): #used for tuple conversion https://www.geeksforgeeks.org/python-program-to-convert-a-tuple-to-a-string/
            string = ''.join(tup)
            return string
        student_ID = input("Enter your student ID: ")
        course_ID = input("Enter the ID of the course to add: ")
        course_ID = str(course_ID)
        studentQuery = ('SELECT COURSES FROM STUDENT WHERE ID = ' + student_ID)
        cursor.execute(studentQuery)
        hold = cursor.fetchall()
        newlist = list(hold)
        holdResult = newlist[0]
        string = convertTuple(holdResult)
        course = str(string + ' ' + course_ID)
        courseAddQuery = ('UPDATE STUDENT SET COURSES = \'' + course + '\' WHERE ID = ' + student_ID)
        cursor.execute(courseAddQuery)
        studentQuery = ('SELECT COURSES FROM STUDENT WHERE ID = ' + student_ID)
        cursor.execute(studentQuery)
        student_ID = str(student_ID)
        studentQuery = ('SELECT STUDENT_LIST FROM COURSE WHERE CRN = ' + course_ID)
        cursor.execute(studentQuery)
        hold = cursor.fetchall()
        newlist = list(hold)
        holdResult = newlist[0]
        string = convertTuple(holdResult)
        student = str(string + ' ' + student_ID)
        studentAddQuery = ('UPDATE COURSE SET STUDENT_LIST = \'' + student + '\' WHERE CRN = ' + course_ID)
        cursor.execute(studentAddQuery)


    def drop_course(self):
        '''Removes this student to a course specified by course ID'''
        def convertTuple(tup): #used for tuple conversion https://www.geeksforgeeks.org/python-program-to-convert-a-tuple-to-a-string/
            string = ''.join(tup)
            return string
        def listToString(s): #used for list to string https://www.geeksforgeeks.org/python-program-to-convert-a-list-to-string/
            str1 = " " 
            return (str1.join(s))
        courseRemove = input("Enter the CRN of the course to remove: ")
        courseRemove = str(courseRemove)
        userID = input("Enter your ID: ")
        cursor.execute('SELECT COURSES FROM STUDENT WHERE ID = ' + userID)
        hold = cursor.fetchall()
        newlist = list(hold)
        holdResult = newlist[0]
        string = convertTuple(holdResult)
        newList = string.split()
        newList.remove(courseRemove)
        cursor.execute('UPDATE STUDENT SET COURSES = \'\' WHERE ID = ' + userID)
        newString = listToString(newList)
        courseRemoveFinal = ('UPDATE STUDENT SET COURSES = \'' + newString + '\' WHERE ID = ' + userID)
        cursor.execute(courseRemoveFinal)
        cursor.execute('SELECT STUDENT_LIST FROM COURSE WHERE CRN = ' + courseRemove)
        hold = cursor.fetchall()
        newlist = list(hold)
        holdResult = newlist[0]
        string = convertTuple(holdResult)
        newList = string.split()
        userID = str(userID)
        newList.remove(userID)
        cursor.execute('UPDATE COURSE SET STUDENT_LIST = \'\' WHERE CRN = ' + courseRemove)
        newString = listToString(newList)
        userRemoveFinal = ('UPDATE COURSE SET STUDENT_LIST = \'' + newString + '\' WHERE CRN = ' + courseRemove)
        cursor.execute(userRemoveFinal)

    def print_courses(self):
        '''Prints out student's schedule'''
        roster = input("Enter your ID: ") 
        rosterQuery = 'SELECT COURSES FROM STUDENT WHERE ID = ' 
        rosterQueryFinal = (rosterQuery + roster)
        cursor.execute(rosterQueryFinal)
        query_result = cursor.fetchall()
        for i in query_result:
            print(i)
