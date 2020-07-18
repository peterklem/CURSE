from Individual import *
from Student import *
from Instructor import *
from Admin import *
import sqlite3

# This is a test for the logout function for every individual type

if __name__ == '__main__':

    # Instantiate each of the invdividual type classes and a flag for the output
    S = Student()
    I = Instructor()
    A = Admin()

    # Reset and open the text file
    outfile = open('logout_test_output.txt', 'w')

    outfile.write('Should return false: \n')
    # Test logout with user entering Y
    outfile.write(str(S.logout(confirm="y")) + ', ')
    outfile.write(str(I.logout(confirm='y')) + ', ')
    outfile.write(str(A.logout(confirm='y')) + '.\n\n')

    
    outfile.write("Should return true: \n")
    
    # User enters n
    outfile.write(str(S.logout(confirm='n')) + ', ')
    outfile.write(str(I.logout(confirm='n')) + ', ')
    outfile.write(str(A.logout(confirm='n'))  + '.\n\n') 

    # User enters a number 
    outfile.write("Should return true: \n")
    outfile.write(str(S.logout(confirm='1')) + ', ')
    outfile.write(str(I.logout(confirm='2')) + ', ')
    outfile.write(str(A.logout(confirm='3'))  + '.\n\n') 
    
    # User enters nothing
    outfile.write("Should return true: \n")
    outfile.write(str(S.logout(confirm='')) + ', ')
    outfile.write(str(I.logout(confirm='')) + ', ')
    outfile.write(str(A.logout(confirm=''))  + '.\n\n') 

    outfile.close()