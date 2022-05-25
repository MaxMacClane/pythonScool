import termcolor as ter
import simple_draw as sd
from lesson_004 import _05_snowfall as snow

ter.cprint("  Seleck color snowflakes  ", 'blue', attrs=['reverse'])

color_list_select = {"1": "COLOR_WHITE ", "2": "COLOR_BLACK ", "3": "COLOR_RED   ",
                     "4": "COLOR_ORANGE", "5": "COLOR_YELLOW", "6": "COLOR_GREEN ",
                     "7": "COLOR_CYAN  ", "8": "COLOR_BLUE  ", "9": "COLOR_PURPLE",
                     "0": "MULTICOLOR"}

color_list_tuple = {"1": (255, 255, 255), "2": (0, 0, 0), "3": (255, 0, 0),
                    "4": (255, 127, 0), "5": (255, 255, 0), "6": (0, 255, 0),
                    "7": (0, 255, 255), "8": (0, 0, 255), "9": (255, 0, 255),
                    "0": "0"}

for i in color_list_select:
    ter.cprint(" {}:{} ".format(i, color_list_select[i]), 'yellow', attrs=['blink'])
color_list = 0
while color_list not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
    color_list = input()
    if color_list not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
        ter.cprint("Please enter a number from 1 to 9")

if color_list == "0":
    snow.snowfleaks_multicolor(amount=2)
else:
    snow.snowfleaks(color_list=color_list_tuple[color_list], amount=2)

print(color_list_tuple[color_list])

sd.pause()
