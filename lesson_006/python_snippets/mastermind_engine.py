from random import randint, random, choice
from itertools import product, count

from termcolor import cprint

_guess_number = 0

everything = " "


def set_number(islist=True):
    global everything
    everything = ["".join(x) for x in product('0123456789', repeat=4)
                  if len(set(x)) == len(x)]
    if islist:
        return everything
    else:
        return choice(everything)


def check_number(represented_number, hidden_number):
    bulls = 0
    cows = 0
    for indexp, ip in enumerate(represented_number):
        for indexr, ir in enumerate(hidden_number):
            if ip == ir and indexp == indexr:
                bulls += 1
                break
            elif ip == ir and ip != hidden_number[indexp]:
                cows += 1
    f = bulls, cows
    return f


def bulls_n_cows(a, b):
    assert a in everything and b in everything
    bulls = sum(1 for x, y in zip(a, b) if x == y)
    cows = len(set(a) & set(b)) - bulls
    return bulls, cows
