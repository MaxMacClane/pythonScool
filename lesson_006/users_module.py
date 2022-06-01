import termcolor as ter
import simple_draw as sd
from lesson_004 import _05_snowfall as snow

ter.cprint(" Seleckt color snowflakes ",'blue',attrs=['reverse'])  # предлогаем выбрать цвет снежинок

color_list_select={"1":"COLOR_WHITE ","2":"COLOR_BLACK ","3":"COLOR_RED   ",  # словарь для вабора цвета снежинок
                   "4":"COLOR_ORANGE","5":"COLOR_YELLOW","6":"COLOR_GREEN ",
                   "7":"COLOR_CYAN  ","8":"COLOR_BLUE  ","9":"COLOR_PURPLE",
                   "0":"MULTICOLOR"}
color_list_tuple={"1":(255,255,255),"2":(0,0,0),"3":(255,0,0),  # словарь соответствия цвета выбору пользователя
                  "4":(255,127,0),"5":(255,255,0),"6":(0,255,0),
                  "7":(0,255,255),"8":(0,0,255),"9":(255,0,255),
                  "0":"0"}
for i in color_list_select:  # цикл выводит таблицу выбора цвета снежинки
    ter.cprint(" {}:{} ".format(i,color_list_select[i]),'cyan',attrs=['blink'])
color_list=0
while color_list not in ["1","2","3","4","5","6","7","8","9","0"]:  # отлавливаем ошибки ввода выбора цвета
    color_list=input("#### ")
    if color_list not in ["1","2","3","4","5","6","7","8","9","0"]:
        ter.cprint(" Please enter a number from 1 to 9 ")

ter.cprint(" Seleck quantity snowflakes  ",'blue',attrs=['reverse'])  # предлагаем выбрать количество снежинок
ter.cprint("Enter a number from 1 to 100 or zero for snowfall  ",'cyan')  # Надпись с подсказкой

quantity=101
f=["0","1","2","3","4","5","6","7","8","9"]
while 0 != quantity > 100:
    quantity=input("#### ")
    if len(quantity) >= 4:
        ter.cprint(" Please enter a number from 1 to 100 ",on_color='on_red')
        quantity=101
        continue
    elif 0 < len(quantity) < 4:
        for i in quantity:
            if i not in f:
                ter.cprint(" Please enter a number from 1 to 100 ",on_color='on_red')
                quantity=101
                continue
    quantity=int(quantity)
    if quantity > 100:
        ter.cprint(" Please enter a number from 1 to 100 ",on_color='on_red')
ter.cprint(" To change the speed of falling snowflakes, enter yes or no  ",'blue',
           attrs=['reverse'])  # предлагаем изменить скорость отрисовки
answer=input("#### ")
speed=0.1
if answer in ["Yes","yes","YES","y","Y"]:
    ter.cprint(" Please enter floating number from 0.1 to 0.9 ",'blue',attrs=['reverse'])
    ter.cprint(" Default speed 0.1  ",'blue',attrs=['reverse'])
    while speed not in ["0.1","0.2","0.3","0.4","0.5","0.6","0.7","0.8","0.9"]:
        speed=input("#### ")
        if speed not in ["0.1","0.2","0.3","0.4","0.5","0.6","0.7","0.8","0.9"]:
            ter.cprint(" please enter floating number from 0.1 to 0.9 ",on_color='on_red')
speed=float(speed)

ter.cprint("  Click escape to finish  ",on_color='on_green')  # сообщаем условия прекращения pygame отрисовки снегопада

if color_list == "0" and quantity == 0:  # условия вызова разноцветного снегопада
    snow.snowfleaks_multicolor(amount=2,speed=speed,quantity_snowflake=False)
elif color_list == "0" and 1 <= quantity <= 100:  # условие отрисовки разноцветных снежинок заданного количества
    snow.snowfleaks_multicolor(amount=quantity,speed=speed,quantity_snowflake=True)
elif quantity == 0:  # условие отрисовки снегопада заданного цвета
    snow.snowfleaks(color_list=color_list_tuple[color_list],amount=2,speed=speed,quantity_snowflake=False)
elif 1 <= quantity <= 100:  # условия отрисовки снежинок выбранного цвета и количества
    snow.snowfleaks(color_list=color_list_tuple[color_list],amount=quantity,speed=speed,quantity_snowflake=True)

sd.pause()

