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

    flag = False

    # Reset and open the text file
    outfile = open('login_test_output.txt', 'w')
 
    # Try with valid information
    outfile.write('EXPECTED RESULT: True\n')
    outfile.write(str(S.login('10001', 'student', 'PhysicsFounder')) + ',')
    outfile.write(str(I.login('20001', 'instructor', 'hummus')) + ',')
    outfile.write(str(A.login('30001', 'admin', 'fourtyFourth')) + '\n\n')

    # Try with invalid passwords
    outfile.write ('EXPECTED RESULT: False.\n')
    outfile.write(str(S.login('10001', 'student', 'Phys')) + ',')
    outfile.write(str(I.login('20001', 'instructor', 'hmus')) + ',')
    outfile.write(str(A.login('30001', 'admin', 'fourtyFourth')) + '\n\n')

    # Try with characters as the ID
    outfile.write('EXPECTED RESULT: False\n')
    outfile.write(str(S.login('abd', 'student', 'PhysicsFounder')) + ',')
    outfile.write(str(I.login('asdfdashb', 'instructor', 'hummus')) + ',')
    outfile.write(str(A.login('arwea', 'admin', 'fourtyFourth')))

    # Try with nothing entered for individual type
    outfile.write ('\n\nEXPECTED RESULT: False.\n')
    outfile.write(str(S.login('10001', '', 'PhysicsFounder')) + ',')
    outfile.write(str(I.login('20001', '', 'hummus')) + ',')
    outfile.write(str(A.login('30001', '', 'fourtyFourth')) + '\n\n')

    outfile.close()