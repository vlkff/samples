#
# Sample User class.
#
# Class names starts from Capital letter
#
class User:
    """
    Sample User class

    A docblock for the class
    """

    first_name = ''
    last_name = ''

    # example of private class variable, analog to static in php
    __count = 0

    # python like a php have a 'magic' methods
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

        # act with a class-var
        self.__class__.__count += 1

    # I assume that 'magic' method returns an obj string representation
    def __str__(self):
        return 'A string representation of User {} {} '\
            .format(self.first_name, self.last_name)

    # A method declaration
    def say_hi(self):
        print('My name is {} {}'.format(self.first_name, self.last_name))

    def get_count(self):
        """Example of working with private vars"""
        return self.__count

    def getName(self):
        return self.first_name + ' ' + self.last_name