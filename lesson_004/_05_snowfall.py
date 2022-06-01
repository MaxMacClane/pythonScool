# -*- coding: utf-8 -*-
import simple_draw as sd
import random
sd.resolution = 1080, 600
# function return dict wiht ltis
def snowf_value(amount):# функция возвращает список со словарём в котором данные для снежинки
    N = amount      # количество снежинок
    snowf_lists = []
    color_list_tuple = [(255, 255, 255), (0, 0, 0), (255, 0, 0),# список разной цветовой палитры
                        (255, 127, 0), (255, 255, 0), (0, 255, 0),
                        (0, 255, 255), (0, 0, 255), (255, 0, 255),
                        ]
    for i in range(N):# цикл заполняет словарь с данными снежинки
        length_list = [x for x in range(4, 30, random.randint(3, 9))] # генерируем список случайных величин длинны
        f = {'length': length_list,
             'x': random.randint(0, 1000),# координата "х"
             'y': random.randint(650, 660),# координата "у"
             "color" : random.choice(color_list_tuple)# выбирает случайный цвет снежинки
             }
        snowf_lists.append(f)
    return snowf_lists

c = 0
def snowfleaks(color_list, amount, speed, quantity_snowflake=True):# рисуем многослойную снежинку передаём функции цвет, количество снежинок
    x, y = 0, 0                                                 # скорость отрисовки и условие при отсутствии которого получаем снегопад
    snowf_lists = snowf_value(amount=amount)# получаем данные для снежинки
    while True:
        sd.start_drawing()# функция simple-draw начинает рисовать в pygame
        # the loop takes data from the list, draws a white snowflake and a blue circle
        for index, count in enumerate(snowf_lists):# запускаем двумерный цикл первый проходит по словарю списка
            for snowf_list in snowf_lists[index]['length']:# второй проходит по списку длинны "length"
                sd.snowflake(center=sd.get_point(snowf_lists[index]['x'], snowf_lists[index]['y']), length=snowf_list,
                             color=color_list)  # рисуем многослойную снежинку
            sd.circle(center_position=sd.get_point(snowf_lists[index]['x'], snowf_lists[index]['y']), radius=40,
                      color=sd.background_color, width=0) # рисеум подложку цветом beckground
            snowf_lists[index]['x'] -= sd.random_number(-20, 20)    # меняем координаты
            snowf_lists[index]['y'] -= sd.random_number(10, 20)     # меняем координаты
        for index, count in enumerate(snowf_lists): # повторяем двумерный цикл для и рисуем снежинку со смещением
            for snowf_list in snowf_lists[index]['length']:# добиваемся эффекта красивого снегопада
                sd.snowflake(center=sd.get_point(snowf_lists[index]['x'], snowf_lists[index]['y']), length=snowf_list,
                             color=color_list)
            # list deletion condition
            if snowf_lists[index]['y'] < sd.random_number(5, 15): # условие выполнение которого собирает снежинки в сугроб
                snowf_lists.remove(count)
                if quantity_snowflake == True:# если выполняется это условие
                        snowf_lists.clear()# освобождаем список с данными снежинки
                        s = snowf_value(amount=amount)# получаем новые
                        snowf_lists += s  # добавляем в список получаем количество снежинок равное N
        x += 1
        # condition for updating the list with data and continuing the snowfall
        if quantity_snowflake == False: # если выполняется это условие получаем снегопад
            if x % 3 == 0: # каждый третий проход
                for _ in range(4): # добавляем в список количество снежинок (N * 4)
                    s = snowf_value(amount=amount)
                    snowf_lists += s
                for _ in range(len(snowf_lists)): # проходим по длине списка
                    snowf_lists[_]['length'].clear() # удаляем список с длинной "length"
                    for length in range(1, sd.random_number(8, 30), 4):# создаём новый список длины "length"
                        snowf_lists[_]['length'].append(length) # получаем эффект таяния снежинок на лету

        sd.finish_drawing()
        sd.sleep(speed)
        if sd.user_want_exit():
            break

def snowfleaks_multicolor( amount, speed, quantity_snowflake=True): # фукция рисует разноцветные снежинки
    x, y = 0, 0                                                 # разноцветный снегопад
    snowf_lists = snowf_value(amount=amount)                    # в остальном они одинаковые
    while True:
        sd.start_drawing()
        # sd.clear_screen()
        # the loop takes data from the list, draws a white snowflake and a blue circle
        for index, count in enumerate(snowf_lists):
            for snowf_list in snowf_lists[index]['length']:
                sd.snowflake(center=sd.get_point(snowf_lists[index]['x'], snowf_lists[index]['y']), length=snowf_list,
                             color=snowf_lists[index]['color']) # получаем разный цвет из словаря данных снежинки

            sd.circle(center_position=sd.get_point(snowf_lists[index]['x'], snowf_lists[index]['y']), radius=30,
                      color=sd.background_color, width=0)
            snowf_lists[index]['x'] -= sd.random_number(-20, 20)
            snowf_lists[index]['y'] -= sd.random_number(10, 20)
        for index, count in enumerate(snowf_lists):
            for snowf_list in snowf_lists[index]['length']:
                sd.snowflake(center=sd.get_point(snowf_lists[index]['x'], snowf_lists[index]['y']), length=snowf_list,
                             color=snowf_lists[index]['color'])
            # list deletion condition
            if snowf_lists[index]['y'] < sd.random_number(15, 25):
                snowf_lists.remove(count)
                if quantity_snowflake == True:
                        snowf_lists.clear()
                        s = snowf_value(amount=amount)
                        snowf_lists += s
        x += 1
        #condition for updating the list with data and continuing the snowfall
        if quantity_snowflake == False:
            if x % 3 == 0:
                for _ in range(2):
                    s = snowf_value(amount=amount)
                    snowf_lists += s

                for _ in range(len(snowf_lists)):
                    snowf_lists[_]['length'].clear()
                    for length in range(1, sd.random_number(8, 30), 4):
                        # for length in range(sd.random_number(0, 600)):
                        snowf_lists[_]['length'].append(length)

        sd.finish_drawing()
        sd.sleep(speed)
        if sd.user_want_exit():
            break

