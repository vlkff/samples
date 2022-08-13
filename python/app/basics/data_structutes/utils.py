#
# Some functions just for fun
#

def print_list(list_to_print):
    print('_ _ _ _ _ _ _ _ _')
    index = 0
    while index < len(list_to_print):
        if index == len(list_to_print) - 1:
            print_end = ''
        else:
            print_end = ', '
        print(list_to_print[index], end=print_end)
        index = index + 1
    print('\n- - - - - - - - -')

