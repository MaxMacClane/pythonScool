import termcolor as ter
import simple_draw as sd
from lesson_004 import _05_snowfall as snow

ter.cprint(" Seleck color snowflakes ", 'blue', attrs=['reverse'])

color_list_select = {"1": "COLOR_WHITE ", "2": "COLOR_BLACK ", "3": "COLOR_RED   ",
                     "4": "COLOR_ORANGE", "5": "COLOR_YELLOW", "6": "COLOR_GREEN ",
                     "7": "COLOR_CYAN  ", "8": "COLOR_BLUE  ", "9": "COLOR_PURPLE",
                     "0": "MULTICOLOR"}

color_list_tuple = {"1": (255, 255, 255), "2": (0, 0, 0), "3": (255, 0, 0),
                    "4": (255, 127, 0), "5": (255, 255, 0), "6": (0, 255, 0),
                    "7": (0, 255, 255), "8": (0, 0, 255), "9": (255, 0, 255),
                    "0": "0"}

for i in color_list_select:
    ter.cprint(" {}:{} ".format(i, color_list_select[i]), 'cyan', attrs=['blink'])
color_list = 0
while color_list not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
    color_list = input("#### ")
    if color_list not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
        ter.cprint(" Please enter a number from 1 to 9 ")

ter.cprint(" Seleck quantity snowflakes  ", 'blue', attrs=['reverse'])
ter.cprint("Enter a number from 1 to 100 or zero for snowfall  ", 'cyan')

quantity = 101
while 0 != quantity >= 100:
    quantity = input("#### ")
    if len(quantity) >= 4:
        ter.cprint(" Please enter a number from 1 to 100 ", on_color='on_red')
        quantity = 101
        continue
    quantity = int(quantity)
    if quantity > 100:
        ter.cprint(" Please enter a number from 1 to 100 ", on_color='on_red')

ter.cprint(" To change the speed of falling snowflakes, enter yes or no  ", 'blue', attrs=['reverse'])
answer = input("#### ")
speed = 0.1
if answer in ["Yes", "yes", "YES", "y", "Y"]:
    ter.cprint(" Please enter floating number from 0.1 to 0.9 ", 'blue', attrs=['reverse'])
    ter.cprint(" Default speed 0.1  ", 'blue', attrs=['reverse'])
    while speed not in ["0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9"]:
        speed = input("#### ")
        if speed not in ["0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9"]:
            ter.cprint(" please enter floating number from 0.1 to 0.9 ", on_color='on_red')

speed = float(speed)

ter.cprint("  Click escape to finish  ", on_color='on_green')

if color_list == "0" and quantity == 0:
    snow.snowfleaks_multicolor(amount=2, speed=speed, quantity_snowflake=False)
elif color_list == "0" and 1 <= quantity <= 100:
    snow.snowfleaks_multicolor(amount=quantity, speed=speed, quantity_snowflake=True)

elif quantity == 0:
    snow.snowfleaks(color_list=color_list_tuple[color_list], amount=2, speed=speed, quantity_snowflake=False)
elif 1 <= quantity <= 100:
    snow.snowfleaks(color_list=color_list_tuple[color_list], amount=quantity, speed=speed, quantity_snowflake=True)



sd.pause()
