#
# Define a Man class
#

from User import User
# @todo: how to reference to Woman class which reference to Man class to escape a loop error?
#from Woman import Woman


class Man(User):
    """
    Man.py can blink to any woman and know if she responds.
    """
    __gender = 'male'

    __blinked_to = []

    def __init__(self, first_name: str, last_name: str):
        # print('Man constructor')
        # print(first_name)
        # print(last_name)
        User.__init__(self, first_name, last_name)

    def blink_to(self, woman):
        # @todo: add woman type declaration or validation
        print('{} send a blink to {}'.format(self.getName(), woman.getName()))
        self.__add_blink(woman)
        woman.got_blink(self)

    def __add_blink(self, woman):
        self.__blinked_to.append(woman)

    # override a base class method
    def say_hi(self):
        prefix = 'mr.' if not self.__gender == 'female' else 'mss'
        print('My name is {} {} {}'.format(prefix, self.first_name, self.last_name))

    def get_response(self, woman):
        print(self.getName() + ' get a response from ' + woman.getName())

