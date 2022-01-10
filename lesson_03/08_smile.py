# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

sd.resolution = (1200, 800)
# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

# draw a circle
for _ in range(10):
    point = sd.random_point()
    sd.circle(point, 60, color=sd.random_color(), width=3)
    # set the conditions, the first two draw the eyes, the next two draw the pupils
    for _ in range(2):
        r = (_ / 1) % 2
        if r == 0:
            point.x = point.x - 53
            point.y = point.y
            right = sd.get_point(point.x + 40, point.y + 25)
        if r == 1:
            point.x = point.x + 50
            point.y = point.y
            right = sd.get_point(point.x + 40, point.y + 25)
        sd.ellipse(point, right, color=sd.COLOR_YELLOW, width=0)
        if r == 0:
            point.x = point.x + 15
            point.y = point.y
            right = sd.get_point(point.x + 10, point.y + 25)
        if r == 1:
            point.x = point.x + 15
            point.y = point.y
            right = sd.get_point(point.x + 10, point.y + 25)
        sd.ellipse(point, right, color=sd.COLOR_BLACK, width=0)
    # set conditions and draw pink tears
    for _ in range(2):
        r = (_ / 1) % 2
        if r == 0:
            point.x = point.x - 62
            point.y = point.y - 3
            end_point = sd.get_point(point.x + 3, point.y)
            sd.line(point, end_point, color=sd.COLOR_PURPLE, width=10)
        if r == 1:
            point.x = point.x + 65
            point.y = point.y
            end_point = sd.get_point(point.x + 3, point.y)
            sd.line(point, end_point, color=sd.COLOR_PURPLE, width=10)
    # draw eyebrows
    for _ in range(2):
        r = (_ / 1) % 2
        if r == 0:
            point.x = point.x - 30
            point.y = point.y + 25
            end_point = sd.get_point(point.x + 45, point.y + 10)
            sd.line(point, end_point, color=sd.COLOR_PURPLE, width=6)
        if r == 1:
            point.x = point.x - 45
            point.y = point.y + 10
            end_point = sd.get_point(point.x + 45, point.y - 10)
            sd.line(point, end_point, color=sd.COLOR_PURPLE, width=6)
    # draw a nose
    point.x = point.x + 45
    point.y = point.y - 10
    end_point = sd.get_point(point.x, point.y - 40)
    sd.line(point, end_point, color=sd.COLOR_RED, width=10)
    # draw the lower lip
    for _ in range(2):
        r = (_ / 1) % 2
        if r == 0:
            point.x = point.x
            point.y = point.y - 65
            end_point = sd.get_point(point.x + 40, point.y + 15)
            sd.line(point, end_point, color=sd.COLOR_RED, width=7)
        if r == 1:
            point.x = point.x - 40
            point.y = point.y + 15
            end_point = sd.get_point(point.x + 42, point.y - 15)
            sd.line(point, end_point, color=sd.COLOR_RED, width=7)
    # draw the upper lip
    point.x = point.x
    point.y = point.y
    end_point = sd.get_point(point.x + 80, point.y)
    sd.line(point, end_point, color=sd.COLOR_RED, width=7)

sd.pause()
