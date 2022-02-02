# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = 800, 800
import random


# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения
# recursion function draws two vectors from the same point with different direction
def draw_branches(s_point, length, angle):
    if length < 4:
        return
    s_point = sd.vector(start=s_point, angle=angle, length=length, width=3, color=sd.random_color())
    _length = length * .75
    angle_ = angle - 30
    draw_branches(s_point, length=_length, angle=angle_)
    angle_ = angle + 30
    draw_branches(s_point, length=_length, angle=angle_)


st_point = sd.get_point(390, 50)
_length = 150
_width = 3
_angle = 90

draw_branches(s_point=st_point, length=_length, angle=_angle)

# 4) Усложненное задание (делать по желанию)


# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
sd.random_number()

sd.pause()
