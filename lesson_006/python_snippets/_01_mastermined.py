from mastermind_engine import set_number, check_number, fix_represent, bulls_n_cows
from termcolor import cprint
from ii_engine import binary_search

player_response = 0
reference = set_number(islist=False)
reference1 = set_number(islist=False)
move_count = 0


cprint(" Single player – enter one. Game with computer – enter two. ", on_color='on_green')
game_selection = input("#### ")

if game_selection == "one" or game_selection == "ONE" or game_selection == "One":
    cprint("Try to guess the number puzzled by the computer", color='magenta')
    while player_response != reference:
        player_response = fix_represent(reference=reference)
        print('*' * 44)
        move_count += 1
        f = check_number(represented_number=player_response, hidden_number=reference)
        cprint("bulls {}, cows {}".format(f[0], f[1]), color='red')
        if player_response == reference:
            cprint(" You win! Guessed number is {}".format(reference), 'green', attrs=['underline'])
            cprint("Move count {}".format(move_count), 'green', attrs=['underline'])
            print()
            question = input("If you want to play more, enter yes, otherwise no ")
            if question == "yes" or question == "YES" or question == "Yes":
                player_response = "0"
                reference = set_number(islist=False)
            else:
                cprint("   GAME OVER   ", 'green', 'on_grey', ['reverse'])

elif game_selection == "two" or game_selection == "TWO" or game_selection == "Two":
    while player_response != reference or computer_response != reference1:
        for i in binary_search(referens=reference1):
            cprint(" Player is playing please enter your number ", color="blue")
            player_response = fix_represent(reference=reference)

            move_count += 1
            f = check_number(represented_number=player_response, hidden_numbe=reference)
            cprint(" bulls {}, cows {}".format(f[0], f[1]), color='red')
            print('*' * 44)
            cprint(" Сomputer is playing ", color="cyan")

            computer_response = i

            cprint("#### {}".format(computer_response), color= "cyan")
            f = bulls_n_cows(reference1, computer_response)
            cprint(" bulls {}, cows {}".format(f[0], f[1]), color='red')
            if player_response == reference:
                cprint(" The player won the hidden number {} ".format(reference), on_color='on_blue')
                question = input("If you want to play more, enter yes, otherwise no ")
                if question == "yes" or question == "YES" or question == "Yes":
                    player_response = "0"
                else:
                    cprint("   GAME OVER   ", 'green', 'on_grey', ['reverse'])
            elif computer_response == reference1:
                cprint(" The computer won the guessed number of the player ".format(reference), on_color='on_cyan')
                if question == "yes" or question == "YES" or question == "Yes":
                    player_response = "0"
                else:
                    cprint("   GAME OVER   ", 'green', 'on_grey', ['reverse'])



