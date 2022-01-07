#!/usr/bin/env python
# -*- coding: utf-8 -*-

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
print('Лампа -', store['12345'][0]['quantity'], 'шт, цена -', store['12345'][0]['price'], 'руб. общая стоимость', lamps_cost, 'рублей.')
# или проще (/сложнее ?)
table_cost = store[goods['Стол']][0]['quantity'] * store[goods['Стол']][0]['price']
table_cost1 = store[goods['Стол']][1]['quantity'] * store[goods['Стол']][1]['price']
tables_fo_510 = store[goods['Стол']][0]['quantity']
tables_fo_520 = store[goods['Стол']][1]['quantity']
number_table = store[goods['Стол']][0]['quantity'] + store[goods['Стол']][1]['quantity']
# table_cost = table_cost2 + table_cost1
print('Стол -', tables_fo_510, 'шт, цена', store[goods['Стол']][0]['price'], 'руб. общая стоимость', table_cost, 'рублей.')

sofa_cost = store[goods['Диван']][0]['quantity'] * store[goods['Диван']][0]['price'] + \
            store[goods['Диван']][1]['quantity'] * store[goods['Диван']][1]['price']
number_sofa = store[goods['Диван']][0]['quantity'] + store[goods['Диван']][1]['quantity']
print('Диван -', number_sofa, 'шт, стоимость', sofa_cost, 'рублей.')

chair_item = store['45678'][0]
chair_quantity = chair_item['quantity']
chair_price = chair_item['price']
chair_cost = chair_quantity * chair_price
print('Стул -', chair_quantity, 'шт, общая стоимость', chair_cost, 'руб.', 'цена -', chair_price, 'за шт.')
chair_item = store['45678'][1]
chair_quantity = chair_item['quantity']
chair_price = chair_item['price']
chair_cost = chair_quantity * chair_price
print('Стул -', chair_quantity, 'шт, общая стоимость', chair_cost, 'руб.', 'цена -', chair_price, 'за шт.')
chair_item = store['45678'][2]
chair_quantity = chair_item['quantity']
chair_price = chair_item['price']
chair_cost = chair_quantity * chair_price
print('Стул -', chair_quantity, 'шт, общая стоимость', chair_cost, 'руб.', 'цена -', chair_price, 'за шт.')
chair_total_quantity = store['45678'][0]['quantity'] + store['45678'][1]['quantity'] + store['45678'][2]['quantity']
chair_total_cost = (store['45678'][0]['quantity'] * store['45678'][0]['price']) + (store['45678'][1]['quantity']
                       * store['45678'][1]['price']) + (store['45678'][2]['quantity'] * store['45678'][2]['price'])
print('Всего стульев -', chair_total_quantity, 'шт,', 'общая стоимость', chair_total_cost, "рублей.")
# Вывести стоимость каждого товара на складе: один раз распечать сколько всего столов, стульев и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще житьs.



##########################################################################################
# ВНИМАНИЕ! После того как __ВСЯ__ домашняя работа сделана и запушена на сервер,         #
# нужно зайти в ЛМС (LMS - Learning Management System ) по адресу http://go.skillbox.ru  #
# и оформить попытку сдачи ДЗ! Без этого ДЗ не будет проверяться!                        #
# Как оформить попытку сдачи смотрите видео - https://youtu.be/qVpN0L-C3LU               #
##########################################################################################
