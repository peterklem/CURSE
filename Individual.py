import sqlite3

class Individual:
    '''Holds first name, last name, and ID'''

    # Variables
    _first_name = ""
    _last_name = ""
    _id = ""

    #   Methods
    def __init__(self):  # No arguments passed
        '''Initializes an individual'''



    def set_first_name(self):
        '''Sets first name of individual'''
        self._first_name = input("Enter first name: ")
        print("First name set as " + self._first_name)


    def set_last_name(self):
        '''Sets last name of individual'''
        self._last_name = input("Enter last name: ")
        print("Last name set as " + self._last_name)


    def set_id(self):
        '''Sets ID of individual'''
        id_flag = False     # True if the input ID is not a duplicate

        while id_flag == False:     # Loop until a valid ID is input

            input_id = input("Enter individual ID: ")
            
            # Check for matching ID, must be unique

            db = sqlite3.connect('database.db')
            cursor = db.cursor()
            cmd = 'SELECT ID FROM STUDENT WHERE ID = ' + input_id
            cursor.execute(cmd)
            matching_id = cursor.fetchall()

            if len(matching_id) == 0:   # Check ID flag
                self._id = input_id
                print("ID set.")  # Print confirmation
                id_flag = True

            else:
                print("That ID is already taken. Please choose another")
                id_flag = False


        db.close()
        self._id = id

    def print_name_id(self):
        '''Prints all three variables to the output'''
        print('First Name: ' + self._first_name)
        print("Last Name: " + self._last_name)
        print("ID: " + self._id)


    def login(self):
        class_type = "" # holds user type

        input_email = input("Enter user email (without '@wit.edu'): ")
        input_id = input("Enter user ID: ")
        
        print(type(self))

        if isinstance(class_type, Student.Student):
            class_type = 'STUDENT'

        elif type(self) == "<class 'Instructor.Instructor'>":
            class_type = 'INSTRUCTOR'

        elif type(self) == "<class 'Admin.Admin'>":
            class_type = 'ADMIN'

        else:
            print('You are not registered as a student, instructor, or admin. Please contact CURSE support for assistance.')
            return False

        # Query database
        db = sqlite3.connect('database.db')
        cursor = db.cursor()

        cmd = "SELECT EMAIL, ID FROM " + class_type + " WHERE EMAIL='" + input_email + "';"
        cursor.execute(cmd)
        data = cursor.fetchall()

        print(data)
        db.close()


    def logout(self):
        pass