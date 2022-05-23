# -*- coding: utf-8 -*-
import simple_draw as sd
import random
random.seed(120)
sd.resolution = 1000, 600
# import lesson_006.users_module as use
# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные


# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()_05_snowfall.py




# function return dict wiht list
def snowf_value():
    N = 2
    snowf_lists = []
    for i in range(N):
        length_list = [x for x in range(4, 30, random.randint(3, 9))]
        f = {'length': length_list,
             'x': random.randint(0, 1000),
             'y': random.randint(650, 660)
             }
        snowf_lists.append(f)
    return snowf_lists





# infinite loop conditions
def snowfleaks(color_list):
    x, y = 0, 0
    snowf_lists = snowf_value()
    while True:
        sd.start_drawing()
        # sd.clear_screen()
        # the loop takes data from the list, draws a white snowflake and a blue circle
        for index, count in enumerate(snowf_lists):
            for snowf_list in snowf_lists[index]['length']:
                sd.snowflake(center=sd.get_point(snowf_lists[index]['x'], snowf_lists[index]['y']), length=snowf_list,
                             color=color_list)
            sd.circle(center_position=sd.get_point(snowf_lists[index]['x'], snowf_lists[index]['y']), radius=30,
                      color=sd.background_color, width=0)
            snowf_lists[index]['x'] -= sd.random_number(-20, 20)
            snowf_lists[index]['y'] -= sd.random_number(10, 20)
        for index, count in enumerate(snowf_lists):
            for snowf_list in snowf_lists[index]['length']:
                sd.snowflake(center=sd.get_point(snowf_lists[index]['x'], snowf_lists[index]['y']), length=snowf_list,
                             color=color_list)
            # list deletion condition
            if snowf_lists[index]['y'] < sd.random_number(15, 25):
                snowf_lists.remove(count)
                # del snowf_lists[index +1]
                # del snowf_lists[index +2]

        x += 1
        # condition for updating the list with data and continuing the snowfall
        if x % 2 == 0:
            for _ in range(1):
                s = snowf_value()
                snowf_lists += s

            for _ in range(len(snowf_lists)):
                snowf_lists[_]['length'].clear()
                for length in range(1, sd.random_number(8, 30), 4):
                    # for length in range(sd.random_number(0, 600)):
                    snowf_lists[_]['length'].append(length)

        sd.finish_drawing()
        sd.sleep(0.1)
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
