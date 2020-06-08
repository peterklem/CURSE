from Individual import *

class Student(Individual):
    '''Contains functions that pertain to students'''

    def __init__(self):
        self._schedule = []  # Student schedule
        print('A new student has been created')

    def search_course(self, course_name):
        '''Searches courses by name'''
        results = []
        # Search SQL database for matches, add to results
        return results

    def add_course(self, course_id):
        '''Adds this student to a course specified by course ID'''
        # Need SQL database
        None

    def drop_course(self, course_id):
        '''Removes this student to a course specified by course ID'''
        # Needs SQL
        None

    def print_schedule(self):
        '''Prints out student's schedule'''
        for i in self._schedule:
            print(i)
