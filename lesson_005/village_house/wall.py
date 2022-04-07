import simple_draw as sd


def wall():
    for y in range(100, 451, 50):
        y1 = y + 50
        r = (y / 50) % 2
        if r == 1:
            x, x1 = 450, 550
        elif r == 0:
            x, x1 = 500, 600
        for x in range(x, 901, 100):
            left = sd.get_point(x, y)
            right = sd.get_point(x1, y1)
            x1 += 100
            sd.rectangle(left, right, color=sd.COLOR_YELLOW, width=3)
    sd.rectangle(sd.get_point(450, 100), sd.get_point(1000, 500), color=sd.COLOR_YELLOW, width=3)

    lest_point = [sd.get_point(440, 520), sd.get_point(1010, 520), sd.get_point(735, 650)]
    sd.lines(point_list=lest_point, color=sd.COLOR_RED, closed=True, width=50)
    lest_point = [sd.get_point(540, 560), sd.get_point(910, 560), sd.get_point(735, 620)]
    sd.lines(point_list=lest_point, color=sd.COLOR_RED, closed=True, width=60)

