# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = 600, 600

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные


# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()
N = 5
x, y = 0, 0


def random_start(condition=False):
    x = sd.random_number(0, 600)
    y = sd.random_number(550, 600)
    if condition:
        return x
    else:
        return y


def snowf_value():
    length_list = []
    return {'length': length_list,
            'x': random_start(condition=True),
            'y': random_start(condition=False)
            }


snowf_lists = []

for _ in range(N):
    snowf_lists.append(snowf_value())
    for length in range(1, sd.random_number(20, 30), sd.random_number(2, 30)):
        # for length in range(sd.random_number(0, 600)):
        snowf_lists[_]['length'].append(length)

    print(snowf_lists)

while True:
    sd.clear_screen()

    for flake in snowf_lists:
        x = snowf_lists[0]['x']
        y = snowf_lists[0]['y']
        # for length in snowf_lists[0]['length'][4]
        length = snowf_lists[0]['length'][1]
        sd.snowflake(center=sd.get_point(x, y), length=length, color=sd.COLOR_WHITE)
        print(sd.get_point(x,y))

    sd.sleep(0.6)

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
