class Individual:
    '''Holds first name, last name, and ID'''

    # Variables
    __first_name = ""
    __last_name = ""
    __id = ""

    #   Methods
    def __init__(self):  # No arguments passed
        print("A new individual has been created")  # Print confirmation

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