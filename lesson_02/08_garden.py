#!/usr/bin/env python
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза',)

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка',)

# создайте множество цветов, произрастающих в саду и на лугу
garden_set = set(garden)
meadow_set = set(meadow)
print(type(garden_set), type(meadow_set))

flowers = list(garden_set | meadow_set)
# выведите на консоль все виды цветов
print(flowers[0].capitalize(), *flowers[1:], sep=', ', end='.\n')

# выведите на консоль те, которые растут и там и там
everywhere = list(garden_set & meadow_set)
print(everywhere[0].capitalize(), *everywhere[1:], sep=', ', end='.\n')

# выведите на консоль те, которые растут в саду, но не растут на лугу
only_garden = list(garden_set - meadow_set)
print(only_garden[0].capitalize(), *only_garden[1:], sep=', ', end='.\n')

# выведите на консоль те, которые растут на лугу, но не растут в саду
only_meadow = list(meadow_set - garden_set)
print(only_meadow[0].capitalize(), *only_meadow[1:], sep=', ', end='.\n')
