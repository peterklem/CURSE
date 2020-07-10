from Individual import *
from Student import *
from Instructor import *
from Admin import *
import sqlite3

# This is a test for the login function for every individual type

if __name__ == '__main__':
    
    
    # Instantiate each of the invdividual type classes
    S = Student()
    I = Instructor()
    A = Admin()

    # Reset the text file
    outfile = open('login_test_output.txt', 'w')
    outfile.close()
    
    # Try with valid information
    S.login('10001', 'student', 'PhysicsFounder')
    I.login('20001', 'instructor', 'hummus')
    A.login('30001', 'admin', 'fourtyFourth')

    # Try with invalid passwords
    S.login('10001', 'student', 'Phys')
    I.login('20001', 'instructor', 'hmus')
    A.login('30001', 'admin', 'fourtyFourth')

    # Try with characters as the ID
    S.login('abd', 'student', 'PhysicsFounder')
    I.login('20001', 'instructor', 'hummus')
    A.login('30001', 'admin', 'fourtyFourth')