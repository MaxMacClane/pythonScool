# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
# initialize variables to draw a rectangle

x, y = 0, 0
x1, y1 = 0, 0



# solution with rectangle function
# loop that chenges the value of variables, 'y'changing will raise the rectangle drawing up
# 'x'changing draws a rectengle to the right and call function thet draw rectengle
# for y in range(0, 700, 50):
#     y1 = y + 50
#     r = (y / 50) % 2
#     if r == 1:
#         x, x1 = -50, 50
#     if r == 0:
#         x, x1 = 0, 100
#     for x in range(x, 700, 100):
#         left = sd.get_point(x, y)
#         right = sd.get_point(x1, y1)
#         x1 += 100
#         sd.rectangle(left, right, color=sd.COLOR_YELLOW, width=3)

# solution with lines function
# loop draws horizontal lines
for y in range(0, 650, 50):
    point = [sd.get_point(0, y), sd.get_point(700, y)]
    sd.lines(point, color=sd.COLOR_YELLOW, closed=False, width=3)

# loop draws vertical lines in even lines
for y in range(0, 650, 100):
    y1 += 100  
    if y == 0:
        y1 = 50
    x1 = 0
    for x in range(0, 700, 100):
        point = [sd.get_point(x, y), sd.get_point(x1, y1)]
        x1 += 100
        sd.lines(point, color=sd.COLOR_YELLOW, closed=False, width=3)

# loop draws vertical lines in odd lines
for y in range(50, 650, 100):
    y1 += 100
    if y == 50:
        y1 = 100
    x1 = -50
    for x in range(-50, 700, 100):
        point = [sd.get_point(x, y), sd.get_point(x1, y1)]           
        x1 += 100
        sd.lines(point, color=sd.COLOR_YELLOW, closed=False, width=3)



sd.pause()