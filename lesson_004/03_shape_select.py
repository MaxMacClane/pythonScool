# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

list_figures = ["Threeangle", "Square", "Pentagon", "Hexagon"]

list_color = [sd.COLOR_RED, sd.COLOR_BLACK, sd.COLOR_WHITE, sd.COLOR_YELLOW, sd.COLOR_PURPLE, sd.COLOR_ORANGE,
              sd.COLOR_BLUE, sd.COLOR_CYAN, sd.COLOR_GREEN, sd.COLOR_DARK_YELLOW]


#function asks to select a shape and its color
# draws a shape according to the selection
def simple_figures(start_p, length, width):
    print('\nSELECT FIGUR: \n 0 : Threeangle \n 1 : Square \n 2 : Pentagon \n 3 : Hexagon')
    user_figur = int(input('Inter namber '))

    while user_figur > 3:
        print('\nInput namber from 0 to 3. Start over'.upper())
        print('\nSELECT FIGUR: \n 0 : Threeangle \n 1 : Square \n 2 : Pentagon \n 3 : Hexagon')
        user_figur = int(input('Inter namber '))

    print('\nSELECT COLOR:', list_figures[user_figur], '\n 0 : RED \n 1 : BLACK\n 2 : WHITE\n 3 : YELLOW\n 4 : PURPLE\n'
                                                       ' 5 : ORANGE\n 6 : BLUE\n 7 : CYAN\n 8 : GREEN\n 9 : DARK YELLOW \n')
    user_color = int(input('Inter namber '))

    while user_color > 9:
        print('\nInpyt namber from 0 to 9. Start over)'.upper())
        print('\nSELECT COLOR:', list_figures[user_figur],
              '\n 0 : RED \n 1 : BLACK\n 2 : WHITE\n 3 : YELLOW\n 4 : PURPLE\n'
              ' 5 : ORANGE\n 6 : BLUE\n 7 : CYAN\n 8 : GREEN\n 9 : DARK YELLOW \n')
        user_color = int(input('Inter namber '))

    if user_figur == 0:
        step_angle = 120
        start_p = sd.get_point(x, y)
        end_point = start_p
        color = list_color[user_color]

    if user_figur == 1:
        step_angle = 90
        start_p = sd.get_point(x, y)
        end_point = start_p
        color = list_color[user_color]

    if user_figur == 2:
        step_angle = 72
        start_p = sd.get_point(x, y)
        end_point = start_p
        color = list_color[user_color]

    if user_figur == 3:
        step_angle = 60
        start_p = sd.get_point(x, y)
        end_point = start_p
        color = list_color[user_color]

    for angle in range(0, 360 - step_angle, step_angle):
        vector = sd.get_vector(start_point=start_p, length=length, angle=angle, width=width)
        vector.draw(color=color)
        start_p = vector.end_point
    start = vector.end_point
    sd.line(start, end_point, width=width, color=color)


x, y = 200, 250
start_po = sd.get_point(x, y)

simple_figures(start_p=start_po, length=150, width=3)

sd.pause()
