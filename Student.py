from Individual import *


class Student(Individual):
    '''Contains functions that pertain to students'''

    def __init__(self):
        pass

    def add_course(self, course_id):
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
        course = str(string + ' ' + student_ID)
        studentAddQuery = ('UPDATE COURSE SET STUDENT_LIST = \'' + student_ID + '\' WHERE CRN = ' + course_ID)
        cursor.execute(studentAddQuery)


    def drop_course(self, course_id):
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

    def check_conflicts(self):
        '''Checks the schedule for conflicts'''
        # Get courses that student is taking 
        db = sqlite3.connect('assignment2.db')
        cursor = db.cursor()
        command = "SELECT COURSES FROM STUDENT WHERE ID = " + str(self.__id) + ";"
        cursor.execute(command)

        all_crn = cursor.fetchall()
        crn_split = all_crn[0][0].split() # Split with spaces
        
        reg_courses = []
        for crn in crn_split: # Loop through courses
            command = "SELECT TITLE, START_TIME, END_TIME, DAYS_OF_WEEK FROM COURSE WHERE CRN = " + crn + ";"
            cursor.execute(command)
            course_data = cursor.fetchall()
            course_dict = {}
            course_dict['title'] = course_data[0][0]
            course_dict['start_time'] = course_data[0][1]
            course_dict['end_time'] = course_data[0][2]
            course_dict['days_of_week'] = course_data[0][3].split()
            reg_courses.append(course_dict) # Add to registered courses list
        
        for i in range(len(reg_courses)):
            for j in range(i + 1, len(reg_courses)):
                # Check day of week
                for day in reg_courses[i]['days_of_week']:
                    if day in reg_courses[j]['days_of_week']:
                        # Same day, Check start times and end times
                        if reg_courses[i]['start_time'] >= reg_courses[j]['start_time'] and reg_courses[i]['start_time'] <= reg_courses[j]['end_time']:
                            print('Conflict between ' + reg_courses[i]['title'] + ' and ' + reg_courses[j]['title'] + '. Day: ' + day)
                        elif reg_courses[j]['start_time'] >= reg_courses[i]['start_time'] and reg_courses[j]['start_time'] <= reg_courses[i]['end_time']:
                            print('Conflict between ' + reg_courses[i]['title'] + ' and ' + reg_courses[j]['title'] + '. Day: ' + day)
            
        db.close()


    def print_schedule(self):
        '''Prints student schedule'''

        print('SCHEDULE FOR STUDENT ' + str(self.__id) + ': \n\n')
        db = sqlite3.connect('assignment2.db')
        cursor = db.cursor()
        command = "SELECT COURSES FROM STUDENT WHERE ID = " + str(self.__id) + ";"
        cursor.execute(command)

        student_course_ids = cursor.fetchall()
        course_id_list = student_course_ids[0][0].split()

        for crn in course_id_list:
            command = "SELECT * FROM COURSE WHERE CRN = " + crn + ";"
            cursor.execute(command)
            course_data = cursor.fetchall()
            print('Title: ' + course_data[0][0])
            print('CRN: ' + str(course_data[0][1]))
            print('Department: ' + course_data[0][2])
            print('Instructor: ' + course_data[0][3])
            print('Start Time: ' + str(course_data[0][4]))
            print('End Time: ' + str(course_data[0][5]))
            print('Days: ' + course_data[0][6])
            print('Semester: ' + course_data[0][7])
            print('Credits: ' + str(course_data[0][8]) + '\n\n')

        db.close()
            
            



