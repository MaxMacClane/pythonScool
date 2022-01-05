#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов
from pprint import pprint

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = dict()

moscow = sites['Moscow']
london = sites['London']
paris = sites['Paris']

moscow_london = ((moscow[0] - london[0]) ** 2 + (moscow[1] - london[1]) ** 2) ** .5
moscow_paris = ((moscow[0] - paris[0]) ** 2 + (moscow[1] - paris[1]) ** 2) ** .5
london_paris = ((london[0] - paris[0]) ** 2 + (london[1] - paris[1]) ** 2) ** .5


distances['Moscow'] = {}
distances['London'] = {}
distances['Paris'] = {}

distances['Moscow']['London'] = moscow_london.__round__(3)
distances['Moscow']['Paris'] = moscow_paris.__round__(3)
distances['London']['Moscow'] = moscow_london.__round__(3)
distances['London']['Paris'] = london_paris.__round__(3)
distances['Paris']['Moscow'] = moscow_paris.__round__(3)
distances['Paris']['London'] = london_paris.__round__(3)


pprint(distances)
