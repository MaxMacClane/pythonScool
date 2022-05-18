from mastermind_engine import set_number, check_number, fix_represent, bulls_n_cows, game_celechion
from termcolor import cprint
from ii_engine import binary_search

player_response = 0
reference = set_number(islist=False)
reference1 = set_number(islist=False)
move_count = 0
celect = game_celechion()

if celect in ["one", "One", "ONE", "001"]:
    cprint("Try to guess the number puzzled by the computer", color='magenta')
    while player_response != reference:
        player_response = fix_represent(reference=reference)
        move_count += 1
        f = bulls_n_cows(represented_number=player_response, hidden_numbe=reference)
        cprint("bulls {}, cows {}".format(f[0], f[1]), color='red')
        print('*' * 44)
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

elif celect in ["002", "two", "Two", "TWO"]:
    while player_response != reference or computer_response != reference1:
        for i in binary_search(referens=reference1):
            cprint(" Player is playing please enter your number ", color="blue")
            player_response = fix_represent(reference=reference)

            move_count += 1
            f = check_number(represented_number=player_response, hidden_numbe=reference)
            cprint(" bulls {}, cows {}".format(f[0], f[1]), color='red')

            cprint(" Сomputer is playing ", color="cyan")

            computer_response = i

            cprint("#### {}".format(computer_response), color= "cyan")
            f = bulls_n_cows(represented_number=reference1, hidden_numbe=computer_response)
            cprint(" bulls {}, cows {}".format(f[0], f[1]), color='red')
            print('*' * 44)
            if player_response == reference:
                cprint(" The player won for the {} moves, hidden number {} ".format(move_count, reference), on_color='on_blue')
                for i in range(3):
                    print()
                question = input("If you want to play more, enter yes, otherwise no ")

                if question == "yes" or question == "YES" or question == "Yes":
                    player_response = "0"
                else:
                    cprint("   GAME OVER   ", 'green', 'on_grey', ['reverse'])
            elif computer_response == reference1:
                cprint(" Компьютер выиграл за {} ходов, скрытое число игрока {} ".format(move_count, reference), on_color='on_cyan')
                for i in range(3):
                    print()
                question = input("If you want to play more, enter yes, otherwise no ")

                if question == "yes" or question == "YES" or question == "Yes":
                    player_response = "0"
                else:
                    cprint("   GAME OVER   ", 'green', 'on_grey', ['reverse'])



