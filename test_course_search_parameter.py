from Individual import *
from Student import *
from Instructor import *
from Admin import *
import sqlite3

# This is a test for the login function for every individual type
def check_results(results):
    # Checks length of results (if there is a course found) and outputs data to a txt file
    outfile.write('Output: ')
    if isinstance(results, list):
        for item in results:
            outfile.write(item[0] + '\n')
    else:
        outfile.write("Nothing was output.\n")

if __name__ == '__main__':
    
    
    # Instantiate each of the invdividual type classes
    S = Student()
    I = Instructor()
    A = Admin()


    # Reset and open the text file
    outfile = open('course_parameter_search_test_output.txt', 'w')

    # Search by name (valid)
    outfile.write('Input: Search by name, name = "Computer Architecture".\n')
    outfile.write('EXPECTED OUTPUT: "Computer Architecture".\n')
    results = S.course_search_parameter(1, 'Computer Architecture')
    check_results(results)
    results = I.course_search_parameter(1, 'Computer Architecture')
    check_results(results)
    results = A.course_search_parameter(1, 'Computer Architecture')
    check_results(results)

    outfile.write('\n\n')

    # Search by name(invalid)
    outfile.write('Input: Search by name, name = "Hackathon".\n')
    outfile.write('EXPECTED OUTPUT: "Nothing was output."\n')
    results = S.course_search_parameter(1, 'Hackathon')
    check_results(results)
    results = I.course_search_parameter(1, 'Hackathon')
    check_results(results)
    results = A.course_search_parameter(1, 'Hackathon')
    check_results(results)
    outfile.write('\n\n')

    # Search by name(blank)
    outfile.write('Input: Search by name, name = "".\n')
    outfile.write('EXPECTED OUTPUT: All course names in the database should show up.\n')
    results = S.course_search_parameter(1, '')
    check_results(results)
    results = I.course_search_parameter(1, '')
    check_results(results)
    results = A.course_search_parameter(1, '')
    check_results(results)
    outfile.write('\n\n')

    # Search by department (valid)
    outfile.write('Input: Search by department, department name = "ELEC".\n')
    outfile.write('EXPECTED OUTPUT: All ELEC courses should show up (5 for each user type).\n')
    results = S.course_search_parameter(2, 'ELEC')
    check_results(results)
    results = I.course_search_parameter(2, 'ELEC')
    check_results(results)
    results = A.course_search_parameter(2, 'ELEC')
    check_results(results)
    outfile.write('\n\n')

    # Search by department(invalid)
    outfile.write('Input: Search by department, department name = "GANK".\n')
    outfile.write('EXPECTED OUTPUT: "Nothing was output".\n')
    results = S.course_search_parameter(2, 'GANK')
    check_results(results)
    results = I.course_search_parameter(2, 'GANK')
    check_results(results)
    results = A.course_search_parameter(2, 'GANK')
    check_results(results)
    outfile.write('\n\n')
    

    # Search by instructor (Last name only)
    outfile.write('Input: Search by instructor, instructor name = "Carpenter".\n')
    outfile.write('EXPECTED OUTPUT: All of Prof. Carpenter\'s courses (2 each user type).\n')
    results = S.course_search_parameter(3, 'Carpenter')
    check_results(results)
    results = I.course_search_parameter(3, 'Carpenter')
    check_results(results)
    results = A.course_search_parameter(3, 'Carpenter')
    check_results(results)
    outfile.write('\n\n')
    

    # Search by instructor (Part of a first name only)
    outfile.write('Input: Search by instructor, instructor name = "Pil".\n')
    outfile.write('EXPECTED OUTPUT: All of Prof. Pilin\'s courses (2 each user type).\n')
    results = S.course_search_parameter(3, 'Pil')
    check_results(results)
    results = I.course_search_parameter(3, 'Pil')
    check_results(results)
    results = A.course_search_parameter(3, 'Pil')
    check_results(results)
    outfile.write('\n\n')
    

    # Search by instructor (all lowercase)
    outfile.write('Input: Search by instructor, instructor name = "carpenter".\n')
    outfile.write('EXPECTED OUTPUT:All of Prof. Carpenter\'s courses (2 for each user type).\n')
    results = S.course_search_parameter(3, 'carpenter')
    check_results(results)
    results = I.course_search_parameter(3, 'carpenter')
    check_results(results)
    results = A.course_search_parameter(3, 'carpenter')
    check_results(results)
    outfile.write('\n\n')

    # Search by instructor (Invalid)
    outfile.write('Input: Search by instructor, instructor name = "Cort".\n')
    outfile.write('EXPECTED OUTPUT: "Nothing was output."\n')
    results = S.course_search_parameter(3, 'Cort')
    check_results(results)
    results = I.course_search_parameter(3, 'Cort')
    check_results(results)
    results = A.course_search_parameter(3, 'Cort')
    check_results(results)
    outfile.write('\n\n')

    # Search by semester (valid)
    outfile.write('Input: Search by semester, semester = "SUM".\n')
    outfile.write('EXPECTED OUTPUT: All summer course names (5 for each user type)\n')
    results = S.course_search_parameter(4, 'SUM')
    check_results(results)
    results = I.course_search_parameter(4, 'SUM')
    check_results(results)
    results = A.course_search_parameter(4, 'SUM')
    check_results(results)
    outfile.write('\n\n')

    # Search by semester (invalid)
    outfile.write('Input: Search by semester, semester = "MAY".\n')    
    outfile.write('EXPECTED OUTPUT: "Nothing was output."\n')
    results = S.course_search_parameter(4, 'MAY')
    check_results(results)
    results = I.course_search_parameter(4, 'MAY')
    check_results(results)
    results = A.course_search_parameter(4, 'MAY')
    check_results(results)
    outfile.write('\n\n')
    
    # Search by # of credits (valid)
    outfile.write('Input: Search by number of credits, credits = 4.\n')    
    outfile.write('EXPECTED OUTPUT: All summer course names (5 for each user type)\n')
    results = S.course_search_parameter(5, '4')
    check_results(results)
    results = I.course_search_parameter(5, '4')
    check_results(results)
    results = A.course_search_parameter(5, '4')
    check_results(results)
    outfile.write('\n\n')

    # Search by # of credits (letters)
    outfile.write('Input: Search by number of credits, credits = "nocredits".\n')    
    outfile.write('EXPECTED OUTPUT: "Nothing was output."\n')
    results = S.course_search_parameter(5, 'nocredits')
    check_results(results)
    results = I.course_search_parameter(5, 'nocredits')
    check_results(results)
    results = A.course_search_parameter(5, 'nocredits')
    check_results(results)
    outfile.write('\n\n')


    
    
    
    
    outfile.close()

