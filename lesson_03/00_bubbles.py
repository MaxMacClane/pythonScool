# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1000, 1000)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# define the radius and points to be passed to the circle function
radius = 70
point = sd.random_point()
color = sd.random_color()
# loop changeds the radius and calls a function that draws circle
for _ in range(3):
    radius += 20
    sd.circle(point, radius, color=sd.random_color(), width=20)


# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
# funchion with four parameters thet calls funchion circle and draws circle
def circle(point, color, radius, width):
    sd.circle(point, color, radius, width)


point = sd.random_point()
circle(point, 70, color, 40)

# Нарисовать 10 пузырьков в ряд
# loop thet run ten timse changed 'x' and draw ten circles per line
for x in range(30, 600, 60):
    point.x = x
    point.y = 50
    color = sd.random_color()
    circle(point, 50, color, 20)

# Нарисовать три ряда по 10 пузырьков
# loop witch run three timse changed 'y' and raises line with circles
for y in range(400, 550, 50):
    point.y = y
    for x in range(30, 600, 60):
        point.x = x
        color = sd.random_color()
        circle(point, 30, color, 20)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# loop thet draws one hundred circles in random place
for _ in range(100):
    point = sd.random_point()
    color = sd.random_color()
    circle(point, 30, color, 20)

sd.pause()
