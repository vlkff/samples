#
# This is set of examples and a playground for Python3 data structures
#
# Basic data structures are
# list[] - like ordered array, with numeric, automatically assigned indexes from 0 to n
# tuple() - same as list, but immutable
# dictionary{} - similar to keyed array in php
# set
#
from utils import print_list
#
# Lists
#
# Lists looks like just an indexed, ordered arrays.
#
my_list = ['one', 'two', 3, True]

# let's see what we can do with it
length = len(my_list)
my_list.append(4)
my_list.insert(1, 500)
del(my_list[0])

for item in my_list:
    print(item)

print_list(my_list)

#
# Tuples
#
# It looks like a list, but immutable.
#
my_tuple = ('One', 'Two', 'Three')
my_typle2 = 'One', 'Two', 'Three', my_tuple
print(my_typle2)
three_three = my_tuple[2][2]


#
# Dictionary
#
# It looks like an associative array in php.
#
my_dictionary = {'first': 'one', 'second': 'two', 3: 'three'}
print(my_dictionary)
# how to get in for access to few vars at a time?
for i, v in my_dictionary.items():
    print('index: {}, value: {}'.format(i, v))

# In a dictionary 'in' looking for an index, not for a value
lookup = 'one'
is_obj_present = lookup in my_dictionary
print('Is {} occur in a dictionary? {}'.format(lookup, is_obj_present))

lookup = 'first'
is_obj_present = lookup in my_dictionary
print('Is {} occur in a dictionary? {}'.format(lookup, is_obj_present))

#
# Sequences
# It looks line not a separate data structure but a way to operate with indexes in lists and tuples
#
my_list = ['One', 'Two', 'Three', 4, 5, 6]
# from index 1 to index 3
each_second = my_list[1:6:2]
print(each_second)

lookup = 'One'
is_obj_present = lookup in my_list
print('Is {} occur in a list? {}'.format(lookup, is_obj_present))

#
# Set
#
# It's a fourth data structure after list, tuple, dictionary
# Set looks like a special data structure when you need to operate on intersections
#
print('\n\n###   Sets   ###')

set1 = set(['one', 'two', 'three', 'three'])
set1.add('new')
print('Set1:')
print(set1)

set2 = set(['four', 'five', 'six'])
set2.add('new')
print('Set2:')
print(set2)

list1 = ['one', 'two', 'three', 'three']
print('list1:')
print(list1)

list2 = ['four', 'five', 'six']
list2.append('new')
print('list2:')
print(list2)

print('set1 & set2 result:')
print(set1 & set2)

print('list1 & list2 result:')
# it would cause an error
# print(list1 & list2)


