#!/usr/bin/env python
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion,', 'kangaroo,', 'elephant,', 'monkey,', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
zoo.extend(['bear'])
zoo.insert(1, 'bear,')
del zoo[-1]
print(*zoo)

# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
#  и выведите список на консоль
zoo.extend(['rooster,', 'ostrich,', 'lark'])
print(*zoo)

# уберите слона
#  и выведите список на консоль
zoo.remove('elephant,')
print(*zoo)
# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.

print('Cage №1 live -', zoo[0], 'Cage №7 live -', zoo[6], '.')
