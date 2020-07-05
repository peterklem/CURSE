import sqlite3

class Individual:
    '''Holds first name, last name, and ID'''

    # Variables
    __first_name = ""
    __last_name = ""
    __id = ""

    #   Methods
    def __init__(self):  # No arguments passed
        #print("A new individual has been created")  # Print confirmation
        pass


    def set_first_name(self, first_name):
        '''Sets first name of individual'''
        self.__first_name = first_name


    def set_last_name(self, last_name):
        '''Sets last name of individual'''
        self.__last_name = last_name


    def set_id(self, id):
        '''Sets ID of individual'''
        self.__id = id


    def print_name_id(self):
        '''Prints all three variables to the output'''
        print('First Name: ' + self.__first_name)
        print("Last Name: " + self.__last_name)
        print("ID: " + self.__id)


    def login(self, user_id, user_type):
        '''Starts an attempt at a login'''
        try:
            user_type_cap = user_type.upper()
        except:
            print("User type must be a string")
            return False
        
        # Check information from database 
        db = sqlite3.connect("assignment2.db")
        cursor = db.cursor()
        command = "SELECT ID, NAME, SURNAME FROM " + user_type_cap + " WHERE ID = " + user_id
        print(command)
        cursor.execute(command)
        query_return = cursor.fetchall() # Contains first name, last name, and ID if a matching student is found
        db.close()
        if len(query_return) == 1:  # If data is returned
            query_data_seperated = list(query_return[0])
            # Set data if login is successful
            self.set_id(query_data_seperated[0])
            self.set_first_name(query_data_seperated[1])
            self.set_last_name(query_data_seperated[2])
            print("Login successful.")
            print("Welcome " + query_data_seperated[1] + " " + query_data_seperated[2] + "!")
            return True

        else:                       # If data is not returned
            print("Login failed.")
            return False


                

    def logout(self):
        '''Confirms if the user wants to log out or not'''
        # Return value should be set equal to the login flag
        is_user_sure = input("Are you sure you want to log out? ('y' or 'n'): ")
        if is_user_sure == 'y' or is_user_sure == 'Y':
            print("Logout confirmed.")
            return False # User logs out.
        else:
            return True # User stays logged in.


    def course_search_id(self, course_id):
        db = sqlite3.connect('assignment2.db')
        cursor = db.cursor()
        cursor.execute("SELECT * FROM COURSE WHERE CRN = '" + course_id + "'")
        course_info = cursor.fetchall()

        if len(course_info) == 0:
            print("Course does not exist. ")
        
        elif len(course_info) > 1:
            print("There are multiple courses with that particular ID. Please report to admin.")

        else: # Data found for a single course
            print(course_info)
