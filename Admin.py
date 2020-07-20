from Individual import *


class Admin(Individual):
    '''Contains functions for use of an administrator'''

    def __init__(self):
        print('A new admin has been created')

    def add_course(self, course_id):
        '''Adds a course to the database'''
        courseName = input("Enter the course name to add: ") #these variables may need to be changed in order to fit into the correct database spots
        course_ID = input("Enter the ID for the course: ")
        courseDept = input("Enter the department name: ")
        courseIName = input("Enter the instructor's name: ")
        courseTimeStart = input("Enter the time of the course: ")
        courseTimeEnd = input("Enter the time the course ends: ")
        courseDay = input("Enter the days the course takes place (separate the days with spaces): ")
        courseSemester = input("Enter what semester the course will be offered for: ")
        courseYear = input("Enter what year the course will be taking place: ")
        courseCredits = input("Enter how many credits the course is: ")
        courseCombine = ('INSERT INTO COURSE VALUES (\'' + courseName + '\',' + 
                          course_ID + ', \'' + courseDept + '\', \'' + courseIName + '\', ' + courseTimeStart + ', ' + courseTimeEnd + ', \'' + courseDay + '\', \'' + 
                          courseSemester + '\', ' + courseYear + ', ' + courseCredits + ')')
        cursor.execute(courseCombine)
        print("Course has been added.")

    def remove_course(self, course_id):
        '''Removes a course from the database'''
        course_ID = input("Enter the course CRN you wish to remove: ")
        courseRemove = ('DELETE FROM COURSE WHERE CRN = ' + course_ID)
        cursor.execute(courseRemove)
        print("Course has been removed.")

    def add_user(self, user_id, first_name, last_name):
        '''Adds a new user to the database'''
        # Adds ID and name in SQL to users table

    def remove_user(self, user_id):
        '''Removes a user from the database'''
        # Find user in SQL and remove them

    def add_user_to_course(self, user_id, course_id):
        '''Adds a user to a certain course'''
        def convertTuple(tup): #used for tuple conversion https://www.geeksforgeeks.org/python-program-to-convert-a-tuple-to-a-string/
            string = ''.join(tup)
            return string
        student_ID = input("Enter the student's ID: ")
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
        course = str(string + ' ' + student_ID)
        studentAddQuery = ('UPDATE COURSE SET STUDENT_LIST = \'' + student_ID + '\' WHERE CRN = ' + course_ID)
        cursor.execute(studentAddQuery)

    def remove_user_from_course(self, user_id, course_id):
        '''Removes a user from a course'''
        def convertTuple(tup): #used for tuple conversion https://www.geeksforgeeks.org/python-program-to-convert-a-tuple-to-a-string/
            string = ''.join(tup)
            return string
        def listToString(s): #used for list to string https://www.geeksforgeeks.org/python-program-to-convert-a-list-to-string/
            str1 = " " 
            return (str1.join(s))
        courseRemove = input("Enter the CRN of the course to remove: ")
        courseRemove = str(courseRemove)
        userID = input("Enter the student's ID: ")
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

    def add_instructor_to_course(self, user_id, course_id):
        def convertTuple(tup): #used for tuple conversion https://www.geeksforgeeks.org/python-program-to-convert-a-tuple-to-a-string/
            string = ''.join(tup)
            return string
        def listToString(s): #used for list to string https://www.geeksforgeeks.org/python-program-to-convert-a-list-to-string/
            str1 = " " 
            return (str1.join(s))
        courseAdd = input("Enter the CRN of the course to add: ")
        courseAdd = str(courseAdd)
        userID = input("Enter the instructor's ID: ")
        cursor.execute('SELECT COURSES FROM INSTRUCTOR WHERE ID = ' + userID)
        hold = cursor.fetchall()
        newlist = list(hold)
        holdResult = newlist[0]
        string = convertTuple(holdResult)
        string = convertTuple(holdResult)
        course = str(string + ' ' + courseAdd)
        courseAddFinal = ('UPDATE INSTRUCTOR SET COURSES = \'' + course + '\' WHERE ID = ' + userID)
        cursor.execute(courseRemoveFinal)

    def remove_instructor_from_course(self, user_id, course_id):
        def convertTuple(tup): #used for tuple conversion https://www.geeksforgeeks.org/python-program-to-convert-a-tuple-to-a-string/
            string = ''.join(tup)
            return string
        def listToString(s): #used for list to string https://www.geeksforgeeks.org/python-program-to-convert-a-list-to-string/
            str1 = " " 
            return (str1.join(s))
        courseRemove = input("Enter the CRN of the course to remove: ")
        courseRemove = str(courseRemove)
        userID = input("Enter the instructor's ID: ")
        cursor.execute('SELECT COURSES FROM INSTRUCTOR WHERE ID = ' + userID)
        hold = cursor.fetchall()
        newlist = list(hold)
        holdResult = newlist[0]
        string = convertTuple(holdResult)
        newList = string.split()
        newList.remove(courseRemove)
        cursor.execute('UPDATE INSTRUCTOR SET COURSES = \'\' WHERE ID = ' + userID)
        newString = listToString(newList)
        courseRemoveFinal = ('UPDATE INSTRUCTOR SET COURSES = \'' + newString + '\' WHERE ID = ' + userID)
        cursor.execute(courseRemoveFinal)
        cursor.execute('DELETE FROM COURSE WHERE CRN = ' + courseRemove)

    def search_roster(self, user_name, course_id):
        '''Searches a course for a specific user (searches by name)'''
        # Get table, search for name, print out results
        results = []
        return results

    def print_roster(self, course_id):
        results = []
        # Get data from sql and save it in results
        for user in results:
            print(results)

    def search_courses(self, course_name):
        results = []
        # Get data from SQL
        return results

    def print_courses(self):
        results = []
        # Query SQL for all courses and save names to results
        for course in results:
            print(course)

    def addStudent(self):
        ID = input("Enter the ID of the student: ")
        username = input("Enter the students username: ")
        fName = input("Enter the students first name: ")
        lName = input("Enter the students last name: ")
        gYear = input("Enter the students graduation year: ")
        major = input("Enter the students major: ")
        email = input("Enter the students email address: ")
        addStudent = ('INSERT INTO STUDENT VALUES(' + ID + ',\'' + username + '\',\'' + fName + '\',\'' + lName + '\',' + gYear + ',\'' + major + '\',\'' + email + '\',NULL)')
        cursor.execute(addStudent)
        print('Student has been added.')

    def addInstructor(self):
        ID = input("Enter the ID of the instructor: ")
        password = input("Ente the password for the instructor: ")
        fName = input("Enter the instructors first name: ")
        lName = input("Enter the instructors last name: ")
        title = input("Enter the instructors title: ")
        hYear = input("Enter the instructors hire year: ")
        dept = input("Enter the instructors department: ")
        email = input("Enter the instructors email address: ")
        addInstructor = ('INSERT INTO INSTRUCTOR VALUES(' + ID + ',\'' + password + '\',\'' + fName + '\',\'' + lName + '\',\'' + title + '\',' + hYear + ',\'' + dept + '\',\'' + email + '\',NULL)')
        cursor.execute(addInstructor)
        print('Instructor has been added.')