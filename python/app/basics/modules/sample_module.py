#
# Simple example module
#
__name__ = 'Custom name'
__version__ = '0.1'
__doc__ = \
"""
Documentation and usage explanation may be placed here
"""

print('The \'sample module\' module imported and it\'s machine name is {}'.format(__name__))

some_variable = 'Some value'


def say_hi():
    print('Hello from {}'.format(__name__))
    print('Module version is {}'.format(__version__))
# end of function



