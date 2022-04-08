import simple_draw as sd

N = 10
x, y = 0, 0


# function return randon 'x'and 'y'
def random_start(condition=False):
    x = sd.random_number(0, 450)
    y = sd.random_number(650, 660)
    if condition:
        return x
    else:
        return y


# function return dict wiht list
def snowf_value():
    length_list = []
    return {'length': length_list,
            'x': random_start(condition=True),
            'y': random_start(condition=False)
            }


snowf_lists = []
# loop adds dictionary to list
for _ in range(N):
    snowf_lists.append(snowf_value())
    for length in range(1, sd.random_number(8, 30), 4):
        # for length in range(sd.random_number(0, 600)):
        snowf_lists[_]['length'].append(length)


# infinite loop conditions
def cloud():
    for i in range(10, 505, 1):
        y = sd.random_number(650, 800)
        sd.snowflake(center=sd.get_point(i, y), length=sd.random_number(15, 25), color=sd.COLOR_WHITE)


def snowfall():
    x = 0
    while True:
        sd.start_drawing()
        # sd.clear_screen()

        # the loop takes data from the list, draws a white snowflake and a blue circle
        for index, count in enumerate(snowf_lists):
            for snowf_list in snowf_lists[index]['length']:
                sd.snowflake(center=sd.get_point(snowf_lists[index]['x'], snowf_lists[index]['y']), length=snowf_list,
                             color=sd.COLOR_WHITE)
            sd.circle(center_position=sd.get_point(snowf_lists[index]['x'], snowf_lists[index]['y']), radius=30,
                      color=sd.background_color, width=0)

            snowf_lists[index]['x'] -= sd.random_number(-20, 20)
            snowf_lists[index]['y'] -= sd.random_number(10, 20)

        for index, count in enumerate(snowf_lists):
            for snowf_list in snowf_lists[index]['length']:
                sd.snowflake(center=sd.get_point(snowf_lists[index]['x'], snowf_lists[index]['y']), length=snowf_list,
                             color=sd.COLOR_WHITE)
            # list deletion condition
            if snowf_lists[index]['y'] < sd.random_number(150, 160):
                snowf_lists.remove(count)

        x += 1
        # condition for updating the list with data and continuing the snowfall
        if x % 2 == 0:
            for _ in range(5):
                snowf_lists.append(snowf_value())

            for _ in range(len(snowf_lists)):
                snowf_lists[_]['length'].clear()
                for length in range(1, sd.random_number(8, 30), 4):
                    # for length in range(sd.random_number(0, 600)):
                    snowf_lists[_]['length'].append(length)

        sd.finish_drawing()
        sd.sleep(0.1)
        if sd.user_want_exit():
            break
