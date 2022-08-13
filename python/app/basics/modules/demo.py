#
# Python modules explained
#

# Modules may both be implemented on C or python, be built-in or external
import sys
# By default, python search requested modules in dirs listed in sys.path and current dir
print('\n\nThe PYTHONPATH is', sys.path, '\n')

# If the module is found, then the statements in the body of that module are run
# and the module is made available for you to use.
# Note that the initialization is done only the first time that we import a module.

# It is possible to pre-compile a module into .pyc-file, and it would be imported faster.

# Lets import a simple module sample_module defined an file located in same dir
import sample_module
sample_module.say_hi()
print(sample_module.some_variable)
print(sample_module.__doc__)

#print(vars(sys))

import dump_module
dump_module.dump_vars()

# example how to import a function right to the current space
from sample_module import say_hi
say_hi()
