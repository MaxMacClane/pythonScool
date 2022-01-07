#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь магазинов с распродажами

shops = {
    'ашан':
        [
            {'name': 'печенье', 'price': 10.99},
            {'name': 'конфеты', 'price': 34.99},
            {'name': 'карамель', 'price': 45.99},
            {'name': 'пирожное', 'price': 67.99}
        ],
    'пятерочка':
        [
            {'name': 'печенье', 'price': 9.99},
            {'name': 'конфеты', 'price': 32.99},
            {'name': 'карамель', 'price': 46.99},
            {'name': 'пирожное', 'price': 59.99}
        ],
    'магнит':
        [
            {'name': 'печенье', 'price': 11.99},
            {'name': 'конфеты', 'price': 30.99},
            {'name': 'карамель', 'price': 41.99},
            {'name': 'пирожное', 'price': 62.99}
        ],
}

# Создайте словарь цен на продкты следующего вида (писать прямо в коде)
sweets = {
    'печенье': [
        {'shop': 'пятёрочка', 'price': 9.99},
        {'shop': 'ашан', 'price': 10.99}
    ],
    'конфеты': [
        {'shop': 'магнит', 'price': 30.99},
        {'shop': 'пятёрочка', 'price': 32.99}
    ],
    'карамель': [
        {'shop': 'магнит', 'price': 41.99},
        {'shop': 'ашан', 'price': 32.99}
    ],
    'пирожное': [
        {'shop': 'пятёрочка', 'price': 59.99},
        {'shop': 'магнит', 'price': 62.99}
    ],
}
# compares the price in dict and chooses lowel
for r in sweets.keys():
    if r == 'печенье':
        if sweets['печенье'][0]['price'] > sweets['печенье'][1]['price']:
            cookies_prise = sweets['печенье'][1]['price']
            cookies_shop = str(sweets['печенье'][1]['shop'])
            print(*cookies_shop[0].upper(), *cookies_shop[1:], ' - ', cookies_prise, sep='')
        else:
            cookies_prise = sweets['печенье'][0]['price']
            cookies_shop = str(sweets['печенье'][0]['shop'])
            print(*cookies_shop[0].upper(), *cookies_shop[1:], ' - ', cookies_prise, sep='')

print("Карамель", sweets['карамель'][0]["shop"], sweets["карамель"][0]["price"])
print("Карамель", sweets['карамель'][1]["shop"], sweets['карамель'][1]["price"])
# Указать надо только по 2 магазина с минимальными ценами
