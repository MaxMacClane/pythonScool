# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (800, 600)


# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

# the function draws a vector three times with a change in angle by 120 degrees and a triangle is obtained
def triangle(point, angle, length, width):
    r = sd.get_vector(start_point=point, angle=angle, length=length, width=width)
    r.draw()
    r1 = sd.get_vector(start_point=r.end_point, angle=angle + 120, length=length, width=width)
    r1.draw()
    r2 = sd.get_vector(start_point=r1.end_point, angle=angle + 240, length=length, width=width)
    r2.draw()


point = sd.get_point(100, 50)
angle = 0
triangle(point=point, angle=angle, length=200, width=4)

# the function draws a vector four times with a 90 degree angle change and a square is obtained
def square(point, angle, length, width):
    r = sd.get_vector(start_point=point, angle=angle, length=length, width=width)
    r.draw()

    r1 = sd.get_vector(start_point=r.end_point, angle=angle + 90, length=length, width=width)
    r1.draw()

    r2 = sd.get_vector(start_point=r1.end_point, angle=angle + 180, length=length, width=width)
    r2.draw()

    r3 = sd.get_vector(start_point=r2.end_point, angle=angle + 270, length=length, width=width)
    r3.draw()


point = sd.get_point(400, 50)
angle = 0
square(point=point, angle=angle, length=200, width=4)

# function draw a pentagon
def pentagon(point, color, width):
    sd.polygon(point_list=point, color=color, width=width)


point = [sd.get_point(400, 300), sd.get_point(500, 300),
         sd.get_point(550, 400), sd.get_point(450, 500),
         sd.get_point(350, 400)]

pentagon(point=point, color=sd.COLOR_YELLOW, width=3)

# function draw a hexagon
def hexagon(point, color, width):
    sd.polygon(point_list=point, color=color, width=width)


point = [sd.get_point(100, 300), sd.get_point(250, 300),
         sd.get_point(300, 400), sd.get_point(250, 500),
         sd.get_point(100, 500), sd.get_point(50, 400)]

hexagon(point=point, color=sd.COLOR_YELLOW, width=3)





# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
