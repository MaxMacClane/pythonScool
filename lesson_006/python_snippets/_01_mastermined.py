from mastermind_engine import set_number, check_number
from termcolor import cprint
represented_number = 0
reference = set_number()
move_count = 0
cprint("Try to guess the number puzzled by the computer", color='magenta')
while represented_number != reference:
    represented_number = input("Enter a four-digit number ")
    print('*' * 44)
    move_count += 1
    check_number(represented_number=represented_number, reference=reference)
    if represented_number == reference:
        cprint(" You win! Guessed number is {}".format(reference), 'green', attrs=['underline'])
        cprint("Move count {}".format(move_count), 'green', attrs=['underline'])
        print()
        question = input("If you want to play more, enter yes, otherwise no ")
        if question == "yes" or question == "YES" or question == "Yes":
            reference = 0
        else:
            cprint("   GAME OVER   ", 'green', 'on_grey', ['reverse'])
