from random import choice
from itertools import product
from termcolor import cprint


def set_number(islist=True):
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
            elif ip == ir and indexp != indexr:
                cows += 1
    cows_end = cows - bulls
    f = bulls, cows_end
    return f


def bulls_n_cows(represented_number, hidden_numbe):

    # assert represented_number in everything and hidden_numbe in everything, " number must be unique digits, try again "
    bulls = sum(1 for x, y in zip(represented_number, hidden_numbe) if x == y)
    cows = len(set(represented_number) & set(hidden_numbe)) - bulls
    return bulls, cows


def fix_represent(reference):
    f = "0"
    while len(f) != len(reference):
        f = input("#### ")
        if len(f) < len(reference) or len(f) > len(reference):
            cprint("invalid input - Enter a four-digit number ", on_color='on_red')
        elif len(f) == len(reference):
            return f


def game_celechion():
    cprint(" Single player – enter one or 1. Game with computer – enter two or 2. ", 'green', attrs=['reverse'])
    answer = " "
    answer_list = ("one", "One", "ONE", "1", "2", "two", "Two", "TWO")
    while len(answer) != len('one'):
        answer = input("#### ")
        if answer not in answer_list:
            answer = " "
            cprint(" Please enter the correct answer ", 'green', attrs=['reverse'])
        elif answer == "1" or answer == "2":
            answer = "00" + answer
    return answer



