#
# Define a Woman class
#

from User import User
#from Man import Man


class Woman(User):
    """
    Woman can get a blink from a man and response on not.
    """

    __gender = 'female'

    __who_blinked = []

    def __init__(self, first_name: str, last_name: str):
        User.__init__(self, first_name, last_name)

    def got_blink(self, man):
        print('{} got a blink from {}'.format(self.getName(), man.getName()))
        self.__add_blink_from(man)


    # override a base class method
    def say_hi(self):
        prefix = 'mr.' if not self.__gender == 'female' else 'mss'
        print('My name is {} {} {}'.format(prefix, self.first_name, self.last_name))

    def __add_blink_from(self, man):
        self.__who_blinked.append(man)

    def print_blinked(self):
        print('Who blinked to {}:'.format(self.getName()))
        for person in self.__who_blinked:
            print('-' + person.getName())

    def __is_blinked(self, man):
        for blinked in self.__who_blinked:
            if blinked.getName() == man.getName():
                return True
        return False

    def respond(self, man):
        if self.__is_blinked(man):
            man.get_response(self)
        else:
            print('{woman} can\'t response to {man} as he not blinked her (yet :=) )'
                  .format(woman=self.getName(), man=man.getName()))

