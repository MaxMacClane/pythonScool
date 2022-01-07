#!/usr/bin/env python
# -*- coding: utf-8 -*-


goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

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
# iterating over the keys in the dictionary.goods
for _ in goods.keys():
    # in the store dictionary take the value quantity and the price, calculate total cost for each keys
    # displaying value quantity, price and total cost
    if _ == 'Лампа':
        number_lamps = store[goods[_]][0]['quantity'], 'pcs'
        cost_lamp = store[goods[_]][0]['price'], '$'
        total_cost_lamps = number_lamps[0] * cost_lamp[0], '$'
        print(_, '-', *number_lamps, 'for -', *cost_lamp)
        print('Total cost lamps -', *total_cost_lamps)
    if _ == 'Стол':
        number_tables = store[goods[_]][0]['quantity'], 'pcs'
        number_tables_one = store[goods[_]][1]['quantity'], 'pcs'
        total_number_tables = number_tables[0] + number_tables_one[0], 'pcs'
        cost_table = store[goods[_]][0]['price'], '$'
        cost_table_one = store[goods[_]][1]['price'], '$'
        total_cost_tables = (number_tables[0] * cost_table[0]) + (number_tables_one[0] * cost_table_one[0]), '$'
        print(_, '-', *number_tables, 'for -', *cost_table, 'and', *number_tables_one, 'for', *cost_table_one)
        print('Total cost tables -', *total_cost_tables)
    if _ == 'Диван':
        number_sofas = store[goods[_]][0]['quantity'], 'pcs'
        number_sofas_one = store[goods[_]][1]['quantity'], 'pcs'
        total_number_sofas = number_sofas[0] + number_sofas_one[0], 'pcs'
        cost_sofa = store[goods[_]][0]['price'], '$'
        cost_sofa_one = store[goods[_]][1]['price'], '$'
        total_cost_sofas = (number_sofas[0] * cost_sofa[0]) + (number_sofas_one[0] * cost_sofa_one[0]), '$'
        print(_, '-', *number_sofas, 'for -', *cost_sofa, 'and', *number_sofas_one, 'for', *cost_sofa_one)
        print('Total cost sofas -', *total_cost_sofas)
    if _ == 'Стул':
        number_chairs = store[goods[_]][0]['quantity'], 'pcs'
        number_chairs_one = store[goods[_]][1]['quantity'], 'pcs'
        number_chairs_two = store[goods[_]][2]['quantity'], 'pcs'
        total_number_chairs = number_chairs[0] + number_chairs_one[0], 'pcs'
        cost_chair = store[goods[_]][0]['price'], '$'
        cost_chair_one = store[goods[_]][1]['price'], '$'
        cost_chair_two = store[goods[_]][2]['price'], '$'
        total_cost_chairs = (number_chairs[0] * cost_chair[0]) + (number_chairs_one[0] * cost_chair_one[0]) + \
                            (number_chairs_two[0] * cost_chair_two[0]), '$'
        print(_, '-', *number_chairs, 'for -', *cost_chair, 'and', *number_chairs_one, 'for', *cost_chair_one,
              'and', *number_chairs_two, 'for', *cost_chair_two)
        print('Total cost chairs -', *total_cost_chairs)





