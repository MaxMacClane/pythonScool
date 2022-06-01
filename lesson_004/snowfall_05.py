import simple_draw as sd
sd.resolution=1080, 600
N = 20 # количество снежинок

def snowflake_gen():# функция создаёт словарь с данными для снежинки
    return {'length': sd.random_number(8, 24), # рандомная длина лучей
            'x': sd.randint(10, 1100),   # рандомная точка "х"
            'y': 850 + sd.randint(10, 50),# рандомная точка "у"
            'factor_a': sd.random_number(4, 7) / 10,# рандомный фактор
            'factor_b': sd.random_number(4, 7) / 10,# рандомный фактор
            'factor_c': sd.random_number(45, 60)# рандомный фактор
            }

snowflakes = []

for _ in range(N):# добавляем в список столько словарей сколько снежинок нужно нарисовать
    snowflakes.append(snowflake_gen())

sd.start_drawing() # функция simple-draw начинающая отрисовку pygame
def snowfall_again():
    i = 0
    while True:
        for snowflake in snowflakes: # запускаем  цикл проходящий по списку, забираем данные из словаря
            point = sd.get_point(snowflake['x'], snowflake['y'])# для отрисовки снежинки цветом background
            sd.snowflake(
                point, snowflake['length'],
                sd.background_color,
                snowflake['factor_a'],
                snowflake['factor_b'],
                snowflake['factor_c'])

            snowflake['x'] -= sd.randint(-10, 10)# изменяем координаты
            snowflake['y'] -= sd.randint(10, 25)# изменяем координаты

            point = sd.get_point(snowflake['x'], snowflake['y'])
            sd.snowflake(                           # рисуем снежинки белым цветом
                point, snowflake['length'],
                sd.COLOR_WHITE,
                snowflake['factor_a'],
                snowflake['factor_b'],
                snowflake['factor_c'])
            if len(snowflakes) > 60: # удаляем излишние данные из списка
                snowflakes.remove(snowflake)
            if snowflake['y'] < sd.randint(15, 30):
                snowflakes.remove(snowflake) # удаляем лишние данные из списка
        i += 1
        if i % 2 == 0: # добавляем в список новые снежинки каждую нечётную итерацию
            snowflakes.append(snowflake_gen())


        sd.finish_drawing() # функция simple-draw завершающая отрисовку pygame
        sd.sleep(0.1)  # функция simple-draw отвечающая за скорость отрисовки. 0.1 самая высокая, 0.9 самая медленная
        if sd.user_want_exit():
            break


snowfall_again()

sd.pause()
