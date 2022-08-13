#
# Helps get info about modules.
#

__name__ = 'Module dumper'
__version__ = '0.1'
__doc__ = \
'''
Helps get info about modules.
'''


def dump_vars(module='sys'):
    """
    Print names of all attributes from sys module
    :return: Null
    """

    import sys

    # Just print a names
    names = dir(module)
    print('\'sys\' module attributes returned by dir():')
    for name in names:
        print(name)
    print()

    variables = vars(sys)
    print('\'sys\' module vars returner by vars():')
    for name in variables:
        print(name)
        #print(value)
    print()
    #print(variables)


    # not sure yet how to get an attribute value by using attr name as a var
    # https://stackoverflow.com/questions/5036700/how-can-you-dynamically-create-variables

    # values = {}
    # for name in names:
    #     # maybe use try..catch here ?
    #     values[name] = getattr(sys, name)



    # for name, value in values:
    #     print('Value of {name} is:'.format(name=name))
    #     print(value)
    #     print('--------------')
# end of function
