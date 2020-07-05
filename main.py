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
    user_type = ""          # Holds the type of user that is trying to log in
    user_pass = ""          # Holds user's entered password
    login_flag = False
    quit_flag = False
# Call login
    while quit_flag == False: # Go while the user does 

        while login_flag == False:
            user_type = input("Are you a student, instructor, or admin? ")
            user_input_id = input("Enter user ID: ")  
            user_input_id = input("Enter password: ")
            user_type = user_type.upper()

            if user_type == 'STUDENT':
                Student_obj = Student()
                login_flag = Student_obj.login(user_input_id, user_type, user_pass)
                if login_flag == False:
                    del Student_obj
            elif user_type == 'INSTRUCTOR':
                Instructor_obj = Instructor()
                login_flag = Instructor_obj.login(user_input_id, user_type, user_pass)
                if login_flag == False:
                    del Instructor_obj
            elif user_type == 'ADMIN':
                Admin_obj = Admin()
                login_flag = Admin_obj.login(user_input_id, user_type, user_pass)
                if login_flag == False:
                    del Admin_obj
            else:
                print("Invalid login information, please try again.")

        # Main menu
        while login_flag == True:
            # Everyone has the option to:
            #     Logout
            #     Search all courses
            #     Search course based on parameter

            # Students have the option to:
            #     Add or remove course from semester schedule

            # Instructors have the option to:
            #     Assemble course roster

            # Admins have the option to:
            #     Add course to system
            #     Remove course from system

            selection_input = 0     # Holds the user's selection once logged in

            print("To search course by ID, enter '1'.")
            print("To search for courses based on other parameters, enter '2'.")
            print("To log out, enter '3'.")
            if user_type == 'STUDENT':
                print("To add a course to your schedule, enter '4'.")
                print("To remove a course from your schedule, enter '5'.\n")

                selection_input = input()

                if selection_input == 1:
                    # Call student search course by ID
                    pass
                elif selection_input == 2:
                    #Call student search course by some other condition
                    pass
                elif selection_input == 3:
                    # Call student logout
                    login_flag = False
                    pass
                elif selection_input == 4:
                    # Call student add class to schedule
                    pass
                elif selection_input == 5:
                    # Call student remove class from schedule
                    pass

                else:
                    print("Invalid selection, please try again. \n")
                


            elif user_type == "INSTRUCTOR":
                print("To print the class roster for a certain course, enter '4'.\n")

                if selection_input == 1:
                    # Call instructor search course by ID
                    pass
                elif selection_input == 2:
                    #Call instructor search course by some other condition
                    pass
                elif selection_input == 3:
                    # Call instructor logout
                    login_flag = False
                    pass
                elif selection_input == 4:
                    # Call instructor assemble course roster
                    pass
                else:
                    print("Invalid selection, please try again. \n")
                
            elif user_type == "ADMIN":
                print("To add a course to the system, enter '4'.")
                print("To remove a course from the system, enter '5'.\n")

                if selection_input == 1:
                    # Call admin search course by ID
                    pass
                elif selection_input == 2:
                    #Call student search course by some other condition
                    pass
                elif selection_input == 3:
                    # Call admin logout
                    login_flag = False
                    pass
                elif selection_input == 4:
                    # Call admin add course to system
                    pass
                elif selection_input == 5:
                    # Call admin remove course from system
                    pass

                else:
                    print("Invalid selection, please try again. \n")

            else:
                raise Exception("The user type is not set.")

            

            