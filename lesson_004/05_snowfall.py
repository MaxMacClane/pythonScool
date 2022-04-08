# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = 1000, 600

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные


# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()05_snowfall.py
N = 10
x, y = 0, 0


# function return randon 'x'and 'y'
def random_start(condition=False):
    x = sd.random_number(0, 1000)
    y = sd.random_number(650, 660)
    if condition:
        return x
    else:
        return y


# function return dict wiht list
def snowf_value():
    length_list = []
    return {'length': length_list,
            'x': random_start(condition=True),
            'y': random_start(condition=False)
            }


snowf_lists = []
# loop adds dictionary to list
for _ in range(N):
    snowf_lists.append(snowf_value())
    for length in range(1, sd.random_number(8, 30), 4):
        # for length in range(sd.random_number(0, 600)):
        snowf_lists[_]['length'].append(length)
# infinite loop conditions
while True:
    sd.start_drawing()
    # sd.clear_screen()

    # the loop takes data from the list, draws a white snowflake and a blue circle
    for index, count in enumerate(snowf_lists):
        for snowf_list in snowf_lists[index]['length']:
            sd.snowflake(center=sd.get_point(snowf_lists[index]['x'], snowf_lists[index]['y']), length=snowf_list,
                         color=sd.COLOR_WHITE)
        sd.circle(center_position=sd.get_point(snowf_lists[index]['x'], snowf_lists[index]['y']), radius=30,
                  color=sd.background_color, width=0)

        snowf_lists[index]['x'] -= sd.random_number(-20, 20)
        snowf_lists[index]['y'] -= sd.random_number(10, 20)

    for index, count in enumerate(snowf_lists):
        for snowf_list in snowf_lists[index]['length']:
            sd.snowflake(center=sd.get_point(snowf_lists[index]['x'], snowf_lists[index]['y']), length=snowf_list,
                         color=sd.COLOR_WHITE)
        # list deletion condition
        if snowf_lists[index]['y'] < sd.random_number(15, 25):
            snowf_lists.remove(count)

    x += 1
    # condition for updating the list with data and continuing the snowfall
    if x % 2 == 0:
        for _ in range(5):
            snowf_lists.append(snowf_value())

        for _ in range(len(snowf_lists)):
            snowf_lists[_]['length'].clear()
            for length in range(1, sd.random_number(8, 30), 4):
                # for length in range(sd.random_number(0, 600)):
                snowf_lists[_]['length'].append(length)

    sd.finish_drawing()
    sd.sleep(0.2)
    if sd.user_want_exit():
        break

sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg
