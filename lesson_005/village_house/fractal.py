# -*- coding: utf-8 -*-

import simple_draw as sd




# the function calculates a random number within the specified percentages for the angle and length
def random_value(value, volum, condition=False):
    if condition == False:
        ran_val = sd.random_number(0, volum) / 1000
    else:
        ran_val = sd.random_number(-volum, volum) / 1000
    return value * ran_val
# # recursion function draws two vectors from the same point with different direction
def draw_branches(s_point, length, angle):
    if length < 3:
        return
    color = sd.COLOR_TREES
    if length < 20:
        color = sd.COLOR_GREEN
    s_point = sd.vector(start=s_point, angle=angle, length=length, width=5, color=color)
    no_know = int(30 + random_value(30, 400))
    # length *= (.75 + random_value(.75, 200, condition=True))
    length *= .7
    angle_ = angle - no_know
    draw_branches(s_point, length=length, angle=angle_)
    angle_ = angle + no_know
    draw_branches(s_point, length=length, angle=angle_)



# sd.pause()
