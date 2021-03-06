# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1000, 1000)
x, y = 0, 0


"""defined the radius and start points to be passed to the circle function
loop changeds the radius and calls a function that draws color circle"""
def three_color_circles():
    radius = 70
    point = sd.random_point()
    for _ in range(3):
        radius += 20
        color = sd.random_color()
        sd.circle(point, radius, color, width=20)


three_color_circles()


"""funchion with four parameters thet calls funchion circle and draws circle"""
def circle(point, color, radius, width):
    sd.circle(point, radius, color, width)


circle(sd.random_point(), radius=70, color=sd.random_color(), width=20)


"""functin with loop thet ten timse changed 'x' and draw ten circles per line"""
def ten_color_circles(point, radius, color, width):
    for x in range(30, 600, 60):
        point.x = x
        color = sd.random_color()
        sd.circle(point, radius, color, width)

ten_color_circles(sd.get_point(x, 50), radius=35, color=sd.random_color(), width=10)


"""function that three times, changing 'y' and three time draw ten circles in line"""
def three_time_tencircles(point, radius, color, width):
    for y in range(250, 550, 100):
        point.y = y
        for x in range(30, 600, 60):
            point.x = x
            color = sd.random_color()
            sd.circle(point, radius, color, width)


three_time_tencircles(sd.get_point(x, y), radius=30, color=sd.random_color(), width=20)

"""functin thet draws hundred circles in random place"""
def hundred_circles(point, radius, color, width):
    for _ in range(100):
        point = sd.random_point()
        color = sd.random_color()
        sd.circle(point, radius, color, width)


hundred_circles(sd.get_point(x, y), radius=20, color=sd.random_color(), width=20)


sd.pause()
