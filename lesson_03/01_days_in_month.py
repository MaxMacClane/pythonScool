# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
print('Вы ввели', month)
months_year = {'1': ['january', 31],
               '2': ['february', 28],
               '3': ['march', 31],
               '4': ['april', 30],
               '5': ['may', 31],
               '6': ['june', 30],
               '7': ['july', 31],
               '8': ['august', 31],
               '9': ['september', 30],
               '10': ['october', 31],
               '11': ['november', 30],
               '12': ['desember', 31],
               }
# loop chenges class of the key to int / unpacks the dictionary value
for _, r in months_year.items():
    _ = int(_)
    manth_name = r[0]
    day_in_mans = r[1], 'days'
    if _ == month:
        print(manth_name[0].upper() + manth_name[1:], *day_in_mans)
    elif month > 12:
        print('Only twelve months in year! Please inter valid value.')
        break


