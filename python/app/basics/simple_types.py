#                                       ### NUMBERS ###
# this is an integer
integer_var = 5

# this is a float
float_var = 10.5
float_var = 10E5

#                                       ### STRINGS ###
single_quote = 'strings are immutable'
double_quote = "same as single"

# and these looks similar to nowdoc in php but looks better

'''
and this is also a string
a multiline string
'''

"""
that also works
with
double quotes
"""

# formatting strings

formatted_str = '{0} age is {1}'.format('vlad`s', 35)
print(formatted_str)

print('#1: Why is {} playing with that {}?'.format('vlad', 'python'))

name = 'vlad'
pet = 'python'
print('#2: Why is {name} playing with that {pet}?'.format(name=name, pet='python'))
print('#3: Why is {name} playing with that {pet}?'.format(pet='python', name=name))

# concatenation
name = 'vlad\'s'
age = 35
# python not allow to make hidden types transitions
formatted_str = name + ' age is ' + str(age)
print(formatted_str)

# printing
print('a')
print('b')
print('a', end='')
print('b', end='')
print()

# new lines
strvar = "This is the first sentence. \
This is the second sentence."
print(strvar)

# raw lines
simple_line = "Newlines are indicated by \n\n\n symbols"
raw_line = r"Newlines are indicated by \n\n\n symbols"

print(simple_line)
print(raw_line)

# Type chenging
print('Type change testing')
i = 5
i = 'b'

# Code formatting
print \
    ('very interesting trick')

print \
    ('{} interesting {} trick'
        .format(
            'an',
            'another'
        )
    )

# Operators
bool_res = 5 & False
print(bool_res)

# Flow control

# If
# also elif: and else: may be chained
if True == False:
    print('True is True')

# While
# A simple and effective, work until the statement is True
# A fancy thing that 'else' may be chained
# may be used 'break'
i = 0
while i < 8:
    print('While i is: {}'.format(i))
    i = i+1
else:
    print('The while loop is over.')

# For
# it is interesting as it iterate through a data structure
for i in range(1, 5):
    print('For i is: {}'.format(i))

# also may be used
# 'else:'
# 'brake'
# 'continue'


# # # # # # # # # # # # # # # # # # # # # # # # # Functions # # # # # # # # # # # # # # # # # # # # # # # # #

def default_and_named_args_demo(first, second='Two', third='Three'):
    print('funcA call:')
    print('First arg is {}'.format(first))
    print('Second arg is {}'.format(second))
    print('Third arg is {}'.format(third))
# end of function


default_and_named_args_demo('111')
default_and_named_args_demo(second='222', third=333, first=111)


def infinite_args_demo(a=5, *numbers, **named):
    print('a:', a)

    # iterate through all the items in tuple
    for single_item in numbers:
        print('noname argument single_item:', single_item)

    for single_item in named:
        print('named argument single_item:', single_item)
# end of function


infinite_args_demo(5, 6, 7, 8, '9', named1='one', named2='Two')


# Docstring demo
def some_documented_function():
    """
    Demo for dock string usage.

    The function print a hello message and do nothing.
    No any special things at all.
    No arguments.
    No named arguments.
    Not working with global.
    It just does exist.
    Living in a file as few lines of code
    their function live.

    :return: Null
    """
    print('some_documented_function been called', end='')
    print('And it have the follow dock block', end='')
    print(some_documented_function.__doc__)


# end of function


some_documented_function()


#
# Test passing values by references 'binding'
#

# test simple var - value not changed
var1 = 6
var2 = var1
var1 = 12
print(var2)

# strings also not change
var1 = '6'
var2 = var1
var1 = '12'
print(var2)

# list not change
var1 = [6, '6']
var2 = var1
var1 = [12, '12']
print(var2)

# dictionary not change
var1 = {'1': 6 ,'2': 6}
var2 = var1
var1 = {'1': 12 ,'2': 12}
print(var2)