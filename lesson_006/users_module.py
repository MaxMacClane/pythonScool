import termcolor as ter
import simple_draw

ter.cprint("  Seleck color snowflakes  ", 'blue', attrs=['reverse'])
color_list_select = {1: "COLOR_WHITE ", 2: "COLOR_BLACK ", 3: "COLOR_RED   ", 4: "COLOR_ORANGE", 5: "COLOR_YELLOW",
                     6: "COLOR_GREEN ", 7: "COLOR_CYAN  ", 8: "COLOR_BLUE  ", 9: "COLOR_PURPLE", }
color_list_tuple = {1: (255, 255, 255), 2: (0, 0, 0), 3: (255, 0, 0), 4: (255, 127, 0), 5: (255, 255, 0),
                    6: (0, 255, 0), 7: (0, 255, 255), 8: (0, 0, 255), 9: (255, 0, 255), }

for i in color_list_select:
    ter.cprint(" {}:{} ".format(i, color_list_select[i]), 'yellow', attrs=['blink'])
color_list = int(input())
from lesson_004._05_snowfall import snowfleaks

snowfleaks(color_list=color_list_tuple[color_list])