# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg
list_figures = ["Threeangle", "Square", "Pentagon", "Hexagon"]
user_color_list = []
def try_again():
    # loop iterates through the list_figures, prints a tooltip to the monitor, and writes the user's choice to
    # user_color_list
    for select_color in list_figures:
        print('\nSELECT COLOR:', select_color, '\n 0 : RED \n 1 : BLACK\n 2 : WHITE\n 3 : YELLOW\n 4 : PURPLE\n'
                  ' 5 : ORANGE\n 6 : BLUE\n 7 : CYAN\n 8 : GREEN\n 9 : DARK YELLOW \n')
        user_color = int( input('Inter namber '))

        while user_color > 9:
            print('Inpyt namber from 0 to 9. Start over)'.upper())
            print('\nSELECT COLOR:', select_color, '\n 0 : RED \n 1 : BLACK\n 2 : WHITE\n 3 : YELLOW\n 4 : PURPLE\n'
                                                   ' 5 : ORANGE\n 6 : BLUE\n 7 : CYAN\n 8 : GREEN\n 9 : DARK YELLOW \n')
            user_color = int(input('Inter namber '))
        user_color_list.append(user_color)
        if select_color == "Hexagon":
            break


try_again()

list_color = [sd.COLOR_RED, sd.COLOR_BLACK, sd.COLOR_WHITE, sd.COLOR_YELLOW, sd.COLOR_PURPLE, sd.COLOR_ORANGE,
              sd.COLOR_BLUE, sd.COLOR_CYAN, sd.COLOR_GREEN, sd.COLOR_DARK_YELLOW]


def simple_figures(start_p, angle, length, width):
    # the loop defines condihions and sets the parameters for changing the angle and start point for the vector func.
    # end end_point for the funchion line
    for r in range(4):
        if r == 0:
            step_angle = 120
            start_p = sd.get_point(x, y)
            end_point = start_p
            color = list_color[user_color_list[0]]
        if r == 1:
            step_angle = 90
            start_p = sd.get_point(x + 300, y)
            end_point = start_p
            color = list_color[user_color_list[1]]
        if r == 2:
            step_angle = 72
            start_p = sd.get_point(x + 300, y + 250)
            end_point = start_p
            color = list_color[user_color_list[2]]
        if r == 3:
            step_angle = 60
            start_p = sd.get_point(x, y + 250)
            end_point = start_p
            color = list_color[user_color_list[3]]
        for angle in range(0, 360 - step_angle, step_angle):
            vector = sd.get_vector(start_point=start_p, length=length, angle=angle, width=width)
            vector.draw(color=color)
            start_p = vector.end_point
        start = vector.end_point
        sd.line(start, end_point, width=width, color=color)


x, y = 100, 50
start_po = sd.get_point(x, y)
_angle = 1
simple_figures(start_p=start_po, angle=_angle, length=150, width=3)

sd.pause()
