from Individual import *


class Student(Individual):
    '''Contains functions that pertain to students'''

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
        # Get CRN's of courses registered for
        db = sqlite3.connect('assignment2.db')
        cursor = db.cursor()
        command = "SELECT COURSES FROM STUDENT WHERE ID = '" + str(self._id) + "';"
        cursor.execute(command)
        raw_courses = cursor.fetchall() # Contains hyphenated list of course ID's
        course_ids = raw_courses[0][0] # get data as single string
        id_lst = course_ids.split('-')
        #print(id_lst)

        full_schedule = []
        for course in id_lst:
            command = "SELECT * FROM COURSE WHERE CRN = " + course + ";"
            cursor.execute(command)
            course_dict = {} # Holds all data seperated out from SQL returned data
            data = cursor.fetchall()
            # Seperate and organize data
            course_dict['Title'] = data[0][0]
            course_dict['CRN'] = data[0][1]
            course_dict['Department'] = data[0][2]
            course_dict['Instructor'] = data[0][3]
            course_dict['Start Time'] = data[0][4]
            course_dict['End Time'] = data[0][5]
            course_dict['Weekdays'] = data[0][6] # creates list of days (by letter)
            course_dict['Semester'] = data[0][7]
            course_dict['Year'] = data[0][8]
            course_dict['Credits'] = data[0][9]
            full_schedule.append(course_dict) # add data to list
        
        print('COURSE SCHEDULE: \n\n')
        for course in full_schedule:
            for item in course.items():
                if isinstance(item[1], str): # Check to see if variable is type string
                    print(item[0] + ': ' + item[1])
                else:
                    print(item[0] + ': ' + str(item[1]))
            # Space between courses
            print('\n')



    def check_conflicts(self):
        '''Checks conflicts in scheduling between courses'''
        db = sqlite3.connect('assignment2.db')
        cursor = db.cursor()
        command = "SELECT COURSES FROM STUDENT WHERE ID = '" + str(self._id) + "';"
        cursor.execute(command)
        raw_courses = cursor.fetchall() # Contains hyphenated list of course ID's
        course_ids = raw_courses[0][0] # get data as single string
        id_lst = course_ids.split('-')

        course_day_time = [] # Will hold start time, end time, days of week, and course name
        for course in id_lst:
            command = "SELECT START_TIME, END_TIME, DAYS_OF_WEEK, TITLE FROM COURSE WHERE CRN = " + course + ";"
            cursor.execute(command)
            course_dict = {} # Holds all data seperated out from SQL returned data
            data = cursor.fetchall()
            # Seperate data
            course_dict['start_time'] = data[0][0]
            course_dict['end_time'] = data[0][1]
            course_dict['days'] = data[0][2].split()
            course_dict['name'] = data[0][3]
            course_day_time.append(course_dict) # add data to list

        for i in range(len(course_day_time)):
            compare_start = i + 1 # Starting point for comparison
            #for j in range(compare_start)
            for j in range(compare_start, len(course_day_time)):
                c1_days = course_day_time[i]['days']
                c2_days = course_day_time[j]['days']
                all_days = c1_days + c2_days
                if len(all_days) != len(set(all_days)): # There are conflicting days
                    # Check the start and end time 
                    c1_start_time = course_day_time[i]['start_time']
                    c1_end_time = course_day_time[i]['end_time']
                    c2_start_time = course_day_time[j]['start_time']
                    c2_end_time = course_day_time[j]['end_time']

                    # Check overlaps in time
                    overlap_flag = False
                    if c1_start_time >= c2_start_time and c1_start_time <= c2_end_time: # overlap detected
                        overlap_flag = True
                    
                    # Check other way 
                    if c2_start_time >= c1_start_time and c2_start_time <= c1_end_time: # overlap detected
                        overlap_flag = True

                    if overlap_flag == True:
                        print('There is an overlap between ', course_day_time[i]['name'], ' and ', course_day_time[j]['name'])  



# Testing

if __name__ == '__main__':
    isaac = Student()
    isaac.set_id(10001)
    isaac.print_schedule()
    
