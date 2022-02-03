# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = 600, 600

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()
x, y = 220, 500


def random_valeu(point, namber, condition=False):
    if condition:
        point_x = sd.random_number(point, namber)
        return point_x


quantity = 0
point = sd.get_point(random_valeu(0, 600), y)
while True:
    sd.clear_screen()
    point.x += sd.random_number(-30, 30)
    point.y -= sd.random_number(0, 30)

    for length in range(3, sd.random_number(10, 30), sd.random_number(2, 5)):
    # for length in range(sd.random_number(0, 600)):
        sd.snowflake(center=point, length=length, color=sd.COLOR_WHITE)
    if point.y < 10:
        point.y = 600 - sd.random_number(0, 30)
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
