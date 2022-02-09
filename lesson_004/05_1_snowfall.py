import simple_draw as sd

width = 1000
height = 600
sd.resolution = (width, height)

N = 5


# def start_point():
#     x = height + 100
#     y = sd.randint(10, width - 10)
#     print(y, x)
#     return sd.get_point(x, y)




def snowflake_gen():
    return {'length': sd.random_number(8, 24),
            'x': sd.randint(10, width - 10),
            'y': height + sd.randint(10, 50),
            'factor_a': sd.random_number(4, 7) / 10,
            'factor_b': sd.random_number(4, 7) / 10,
            'factor_c': sd.random_number(45, 60)
            }


snowflakes = []

for _ in range(N):
    snowflakes.append(snowflake_gen())


# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

i = 0

sd.start_drawing()
while True:
    # sd.clear_screen()
    # sd.draw_background()

    for snowflake in snowflakes:
        point = sd.get_point(snowflake['x'], snowflake['y'])
        sd.snowflake(
            point, snowflake['length'],
            sd.background_color,
            snowflake['factor_a'],
            snowflake['factor_b'],
            snowflake['factor_c'])

        snowflake['x'] -= sd.randint(-10, 10)
        snowflake['y'] -= sd.randint(10, 25)

        point = sd.get_point(snowflake['x'], snowflake['y'])
        sd.snowflake(
            point, snowflake['length'],
            sd.COLOR_WHITE,
            snowflake['factor_a'],
            snowflake['factor_b'],
            snowflake['factor_c'])
        if snowflake['y'] < sd.randint(15, 30):

            snowflakes.remove(snowflake)
        #     print(snowflake)
    i += 1
    if i % 2 == 0:
        # new_snowflake = snowflake_gen()
        # print(new_snowflake)
        snowflakes.append(snowflake_gen())
        print('\n', snowflakes)

    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
