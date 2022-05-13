from mastermind_engine import set_number, check_number
from termcolor import cprint

represented_number = 0
reference = set_number()
move_count = 0
cprint("Try to guess the number puzzled by the computer", color='magenta')


def fix_represent():
    f = "0"
    while len(f) != str(len(reference)):
        f = input("Enter a four-digit number ")
        if len(f) < len(reference) or len(f) > len(reference):
            cprint("invalid input - Enter a four-digit number ", on_color='on_red')
        elif len(f) == len(reference):
            return f


while represented_number != reference:
    represented_number = fix_represent()
    print('*' * 44)
    move_count += 1
    f = check_number(represented_number=represented_number, reference=reference)
    cprint("bulls {}, cows {}".format(f[0], f[1]), color='red')
    if represented_number == reference:
        cprint(" You win! Guessed number is {}".format(reference), 'green', attrs=['underline'])
        cprint("Move count {}".format(move_count), 'green', attrs=['underline'])
        print()
        question = input("If you want to play more, enter yes, otherwise no ")
        if question == "yes" or question == "YES" or question == "Yes":
            reference = 0
        else:
            cprint("   GAME OVER   ", 'green', 'on_grey', ['reverse'])
