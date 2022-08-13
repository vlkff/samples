#
# This is a demo file for objects
#
#
from User import User
from Man import Man
from Woman import Woman

user_me = User('Vladyslav', 'Bogatyrov')
print(str(user_me))
user_he = User('Dima', 'Sidanchenko')
user_me.say_hi()
print('Total amount of users is:')
print(user_me.get_count())

vlad = Man('Vladyslav', 'Bogatyrov')
oleg = Man('Oleg', 'Someone')
ivanka = Woman('Ivanka', 'the scorpio')

vlad.blink_to(ivanka)

ivanka.print_blinked()
ivanka.respond(vlad)
ivanka.respond(oleg)
