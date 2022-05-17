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


def check_number(represented_number, hidden_numbe):
    bulls = 0
    cows = 0
    for indexp, ip in enumerate(represented_number):
        for indexr, ir in enumerate(hidden_numbe):
            if ip == ir and indexp == indexr:
                bulls += 1
                break
            elif ip == ir and ip != hidden_numbe[indexp]:
                cows += 1
    f = bulls, cows
    return f


def hidden_number():
    f = set_number(islist=False)
    return f


def bulls_n_cows(a, b):
    set_number(islist=True)
    assert a in everything and b in everything
    bulls = sum(1 for x, y in zip(a, b) if x == y)
    cows = len(set(a) & set(b)) - bulls
    return bulls, cows


def fix_represent(reference):

    f = "0"
    while len(f) != str(len(reference)):
        f = input("#### ")
        if len(f) < len(reference) or len(f) > len(reference):
            cprint("invalid input - Enter a four-digit number ", on_color='on_red')
        elif len(f) == len(reference):
            return f