import simple_draw as sd


def wall():
    for y in range(100, 451, 50):
        y1 = y + 50
        r = (y / 50) % 2
        if r == 1:
            x, x1 = 650, 750
        elif r == 0:
            x, x1 = 700, 800
        for x in range(x, 1101, 100):
            left = sd.get_point(x, y)
            right = sd.get_point(x1, y1)
            x1 += 100
            sd.rectangle(left, right, color=sd.COLOR_DARK_RED, width=4)
    sd.rectangle(sd.get_point(650, 100), sd.get_point(1200, 500), color=sd.COLOR_YELLOW, width=5)

    lest_point = [sd.get_point(640, 520), sd.get_point(1210, 520), sd.get_point(935, 650)]
    sd.lines(point_list=lest_point, color=sd.COLOR_RED, closed=True, width=50)
    lest_point = [sd.get_point(740, 560), sd.get_point(1110, 560), sd.get_point(935, 620)]
    sd.lines(point_list=lest_point, color=sd.COLOR_RED, closed=True, width=60)
    sd.square(sd.get_point(800, 200), side=200, color=sd.background_color, width=0)
    sd.square(sd.get_point(800, 200), side=200, color=sd.COLOR_WHITE, width=11)
    sd.line(sd.get_point(900, 200), sd.get_point(900, 400), color=sd. COLOR_WHITE, width=5)
    sd.line(sd.get_point(900, 325), sd.get_point(1000, 325), color=sd. COLOR_WHITE, width=5)

wall()


sd.pause()