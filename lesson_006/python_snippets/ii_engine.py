from termcolor import cprint
from random import choice, randint, random
import mastermind_engine

hidden_number = mastermind_engine.set_number(islist=False)



def fix_represent():
    global hidden_number
    list_len = len(mastermind_engine.set_number(islist=True))
    list_numbers = mastermind_engine.set_number(islist=True)
    d = " "
    steps_list = []
    point_srt = 0
    point_end = 5040
    count = 0
    while hidden_number != d:
        d = list_numbers[list_len // 2]
        steps_list.append(d)
        list_len = len(list_numbers) // 2
        if d > hidden_number:
            del list_numbers[list_numbers.index(d) : point_end]

        elif d < hidden_number:
            del list_numbers[point_srt: list_numbers.index(d)]

        if len(list_numbers) == 2 and list_len == 1:
            list_numbers.remove(d)
        count += 1
    return steps_list

def fix_import():
    represented_number = fix_represent()
    f = mastermind_engine.check_number(represented_number=represented_number, hidden_number=hidden_number)
    cprint("bulls {}, cows {}".format(f[0], f[1]), color='red')
    return f


# while hidden_number != fix_import():

for i in fix_represent():
    print(i)
