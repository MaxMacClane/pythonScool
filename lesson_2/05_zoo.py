#!/usr/bin/env python
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion,', 'kangaroo,', 'elephant,', 'monkey,', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
zoo.extend(['bear'])
zoo.insert(1, 'bear,')
del zoo[-1]
print(zoo[0], zoo[1], zoo[2], zoo[3], zoo[4])

# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
#  и выведите список на консоль
zoo.extend(['rooster,', 'ostrich,', 'lark.'])
print(zoo[0], zoo[1], zoo[2], zoo[3], zoo[4], zoo[5], zoo[6], zoo[7])

# уберите слона
#  и выведите список на консоль
zoo.remove('elephant,')
print(zoo[0], zoo[1], zoo[2], zoo[3], zoo[4], zoo[5], zoo[6])
# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.

zoo[0] = 'lion cage №1,'
zoo[6] = 'lark cage №7.'
print(zoo[0], zoo[6])


