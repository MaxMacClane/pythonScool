#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть значение радиуса круга

# Выведите на консоль значение прощади этого круга с точностю до 4-х знаков после запятой
# подсказки:
#       формулу можно подсмотреть в интернете,
#       пи возьмите равным 3.1415926
#       точность указывается в функции round()

radius = 42
# s = πR2

surface_area = 3.1415926 * (42 ** 2)

print('surface_circle = ', surface_area.__round__(4))


# Далее, пусть есть координаты точки
# где 23 - координата х, 34 - координата у

# Если точка point лежит внутри того самого круга (radius = 42), то выведите на консоль True,
# Или False, если точка лежит вовне круга.
# подсказки:
#       нужно определить расстояние от этой точки до начала координат (0, 0)
#       формула так же есть в интернете
#       квадратный корень - это возведение в степень 0.5
#       операции сравнения дают булевы константы True и False
point = (23, 34)
hypotenuse = ((23 ** 2) + (34 ** 2)) ** .5
print(hypotenuse)

if hypotenuse < radius:
    print(True)
else:
    print(False)
# Аналогично для другой точки
# Если точка point_2 лежит внутри круга (radius = 42), то выведите на консоль True,
# Или False, если точка лежит вовне круга.
point_2 = (30, 30)
hypotenuse_1 = ((30 ** 2) + (30 ** 2)) ** .5
print(hypotenuse_1)

if hypotenuse_1 < radius:
    print(True)
else:
    print(False)
# Пример вывода на консоль:
#
# 77777.7777
# False
# False


