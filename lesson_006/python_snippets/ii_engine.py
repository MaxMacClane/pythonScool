from termcolor import cprint
from random import choice, randint, random
import mastermind_engine


def binary_search(referens):
    hidden_number = referens
    list_len = len(mastermind_engine.set_number(islist=True))
    list_numbers = mastermind_engine.set_number(islist=True)
    numbe_middle_list = " "
    steps_list = []
    point_srt = 0
    point_end = 5040
    count = 0
    while hidden_number != numbe_middle_list:
        numbe_middle_list = list_numbers[list_len // 2]
        steps_list.append(numbe_middle_list)
        list_len = len(list_numbers) // 2
        if numbe_middle_list > hidden_number:
            del list_numbers[list_numbers.index(numbe_middle_list): point_end]

        elif numbe_middle_list < hidden_number:
            del list_numbers[point_srt: list_numbers.index(numbe_middle_list)]

        elif len(list_numbers) == 2 and list_len == 1:
            list_numbers.remove(numbe_middle_list)
        count += 1
    for i in steps_list:
        yield i






