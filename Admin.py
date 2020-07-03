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
        courseIFName = input("Enter the instructor's first name: ")
        courseILName = input("Enter the instrucor's last name: ")
        courseTimeStart = input("Enter the time of the course: ")
        courseTimeEnd = input("Enter the time the course ends: ")
        courseDay = input("Enter the days the course takes place (separate the days with spaces): ")
        courseSemester = input("Enter what semester the course will be offered for: ")
        courseYear = input("Enter what year the course will be taking place: ")
        courseCredits = input("Enter how many credits the course is: ")
        courseCombine = ('INSERT INTO COURSE VALUES (\'' + courseName + '\',' + 
                          course_ID + ', \'' + courseDept + '\', \'' + courseIFName + '\', \'' + 
                          courseILName + '\', ' + courseTimeStart + ', ' + courseTimeEnd + ', \'' + courseDay + '\', \'' + 
                          courseSemester + '\', ' + courseYear + ', ' + courseCredits + ')')
        cursor.execute(courseCombine)
        print("Course has been added.")
#        add_another_day = True  # Flag for adding additional meeting days/times
#        choice = 'y'
#        course = {}
#        course['Days'] = []
#        course['Start Time'] = []
#        course['End Times'] = []
#        course_name = input('Enter course name: ')
#        while add_another_day == True:
#            course['Days'].append(input('Enter a day to meet: '))
#            course['Start Time'].append(input('Enter a starting time for this day: '))
#            course['End Time'].append(input('Enter an ending time for this day: '))
#
#            choice = input("Add another meeting time? ([y] or [n]")
#            if choice == 'y':
#                add_another_day = True
#            else:
#                add_another_day = False
#
 #       # All information passed to SQL here
 #       print('{} has been added'.format(course_id))

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
        # Modifies a course roster in SQL

    def remove_user_from_course(self, user_id, course_id):
        '''Removes a user from a course'''
        # Remove user in SQL database

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