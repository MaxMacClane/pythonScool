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
# def triangle(point, angle, length, width):
#     r = sd.get_vector(start_point=point, angle=angle, length=length, width=width)
#     r.draw()
#     r1 = sd.get_vector(start_point=r.end_point, angle=angle + 120, length=length, width=width)
#     r1.draw()
#     r2 = sd.get_vector(start_point=r1.end_point, angle=angle + 240, length=length, width=width)
#     r2.draw()
#
#
# point = sd.get_point(100, 50)
# angle = 0
# triangle(point=point, angle=angle, length=200, width=3)
#
#
# # the function draws a vector four times with a 90 degree angle change and a square is obtained
# def square(point, angle, length, width):
#     r = sd.get_vector(start_point=point, angle=angle, length=length, width=width)
#     r.draw()
#     r1 = sd.get_vector(start_point=r.end_point, angle=angle + 90, length=length, width=width)
#     r1.draw()
#     r2 = sd.get_vector(start_point=r1.end_point, angle=angle + 180, length=length, width=width)
#     r2.draw()
#     r3 = sd.get_vector(start_point=r2.end_point, angle=angle + 270, length=length, width=width)
#     r3.draw()
#
#
# point = sd.get_point(400, 50)
# angle = 0
# square(point=point, angle=angle, length=200, width=3)
#
#
# # function draw a pentagon
# def pentagon(point, color, width):
#     sd.polygon(point_list=point, color=color, width=width)
#
#
# point = [sd.get_point(400, 300), sd.get_point(500, 300),
#          sd.get_point(550, 400), sd.get_point(450, 500),
#          sd.get_point(350, 400)]
#
# pentagon(point=point, color=sd.COLOR_YELLOW, width=3)
#
#
# # function draw a hexagon
# def hexagon(point, color, width):
#     sd.polygon(point_list=point, color=color, width=width)
#
#
# point = [sd.get_point(100, 300), sd.get_point(250, 300),
#          sd.get_point(300, 400), sd.get_point(250, 500),
#          sd.get_point(100, 500), sd.get_point(50, 400)]
#
# hexagon(point=point, color=sd.COLOR_YELLOW, width=3)

# funchion draws triangle, square, pentagon, hexagon
# the sides of the figures are drawn by the vector funchoin
# except for the closing side are drawn by the line funchion
def simple_figures(start_p, angle, length, width):
    # the loop defines condihions and sets the parameters for changing the angle and start point for the vector func.
    # end end_point for the line funchion 
    for r in range(4):
        if r == 0:
            step_angle = 120
            start_p = sd.get_point(x, y)
            end_point = start_p
        if r == 1:
            step_angle = 90
            start_p = sd.get_point(x + 300, y)
            end_point = start_p
        if r == 2:
            step_angle = 72
            start_p = sd.get_point(x + 300, y + 250)
            end_point = start_p
        if r == 3:
            step_angle = 60
            start_p = sd.get_point(x, y + 250)
            end_point = start_p               
        for angle in range(0, 360 - step_angle, step_angle):
            vector = sd.get_vector(start_point=start_p, length=length, angle=angle,  width=width)
            vector.draw()
            start_p = vector.end_point
        start = vector.end_point
        sd.line(start, end_point, width=width)


x, y = 100, 50
start_po = sd.get_point(x, y)
_angle = 1
simple_figures(start_p=start_po, angle=_angle, length=150, width=3)
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
