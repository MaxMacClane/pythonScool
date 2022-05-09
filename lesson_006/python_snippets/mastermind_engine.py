from random import randint, random
from termcolor import cprint
_guess_number = 0


def set_number():
    global _guess_number
    _guess_number = str(randint(1000, 9000))
    return _guess_number


def check_number(represented_number, reference):
    bulls = 0
    cows = 0
    for indexp, ip in enumerate(represented_number):
        for indexr, ir in enumerate(reference):
            if ip == ir and indexp == indexr:
                bulls += 1
                break
            elif ip == ir and ip != reference[indexp]:
                cows += 1
    return  cprint("bulls {}, cows {}".format(bulls, cows,), color='red')


