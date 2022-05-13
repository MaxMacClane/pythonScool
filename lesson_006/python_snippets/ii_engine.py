from termcolor import cprint
import mastermind_engine
reference = mastermind_engine.set_number()

def fix_represent():
    f = "0"
    while len(f) != str(len(reference)):
        f = input("Enter a four-digit number ")
        if len(f) < len(reference) or len(f) > len(reference):
            cprint("invalid input - Enter a four-digit number ", on_color='on_red')
        return f


def fix_import():
    represented_number = fix_represent()
    f = mastermind_engine.check_number(represented_number=represented_number, reference=reference)
    cprint("bulls {}, cows {}".format(f[0], f[1]), color='red')
    return f


while fix_import()[0] < 4:
    print("#" * 45)





