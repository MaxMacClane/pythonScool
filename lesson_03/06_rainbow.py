# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
x, y = 50, 50
x1, y1 = 350, 450
# loop thet sort out rainbow_colors, call def.line from simple_drow and changes start & end point 'x'
for i in range(len(rainbow_colors)):
    start_point = sd.get_point(x, y)
    x += 30
    end_point = sd.get_point(x1, y1)
    x1 += 30
    sd.line(start_point, end_point, color=rainbow_colors[i], width=20)

for i in range(len(rainbow_colors)):
    def start_point(x=50):
        x += i * 30
        return x

    def end_point(x1=350):
        x1 += i * 30
        return x1

    sd.line(sd.get_point(start_point(), 450), sd.get_point(end_point(), 50), color=rainbow_colors[i], width=20)

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код

sd.pause()
