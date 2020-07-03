from Individual import *
from Student import *
from Instructor import *
from Admin import *
import sqlite3
#--------------------------------------------------------------------
#   This is the "main" file in the CURSE program. It is mainly the
#   user interface and determines when each of the functions is 
#   called.
#--------------------------------------------------------------------

if __name__ == '__main__':
#Variables
    user_input_id = ""      # Temporarily holds user's id during login
    user_type = ""
# Call login
    while len(user_input_id) == 0:
        user_login = input("Enter user ID: ")
        if user_login == "":
            print("Please enter a valid ID.")
        else: # User entered something
            
            user_type = input("Are you a student, instructor, or admin? ")
            user_type.capitalize()

            if user_type == 'STUDENT':

                # Search student table for ID matches
                db = sqlite3.connect("assignment2.db")
                cursor = db.cursor()
                command = "SELECT ID FROM STUDENT WHERE ID = " + user_input_id
                cursor.execute(command)
                id_lst = cursor.fetchall() # Contains list of matching student ID's as what was input

                if len(id_lst) == 0:
                    # No matching ID's
                    print("There is no student with that ID. Please retry.")
                else:
                    Student_obj = Student() # instantiate a new student
                    
                db.close()

        