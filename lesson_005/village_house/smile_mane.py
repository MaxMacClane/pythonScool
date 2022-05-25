import simple_draw as sd
sd.resolution= 600, 800


# draw a circle
def smale_mane():
    for _ in range(1):
        point = sd.get_point(460, 270)
        # point = sd.random_point()
        sd.circle(point, 60, color=sd.random_color(), width=8)
        # set the conditions, the first two draw the eyes, the next two draw the pupils
        for _ in range(2):
            r = (_ / 1) % 2
            if r == 0:
                point.x = point.x - 53
                point.y = point.y
                right = sd.get_point(point.x + 40, point.y + 25)
            elif r == 1:
                point.x = point.x + 50
                point.y = point.y
                right = sd.get_point(point.x + 40, point.y + 25)
            sd.ellipse(left_bottom=point, right_top=right, color=sd.COLOR_YELLOW, width=0)
            if r == 0:
                point.x = point.x + 15
                point.y = point.y
                right = sd.get_point(point.x + 10, point.y + 25)
            elif r == 1:
                point.x = point.x + 15
                point.y = point.y
                right = sd.get_point(point.x + 10, point.y + 25)
            sd.ellipse(point, right, color=sd.COLOR_BLACK, width=0)
        # set conditions and draw pink tears
        for _ in range(2):
            r = (_ / 1) % 2
            if r == 0:
                point.x = point.x - 62
                point.y = point.y - 3
                end_point = sd.get_point(point.x + 3, point.y)
                sd.line(point, end_point, color=sd.COLOR_PURPLE, width=10)
            elif r == 1:
                point.x = point.x + 65
                point.y = point.y
                end_point = sd.get_point(point.x + 3, point.y)
                sd.line(point, end_point, color=sd.COLOR_PURPLE, width=10)
        # draw eyebrows
        for _ in range(2):
            r = (_ / 1) % 2
            if r == 0:
                point.x = point.x - 30
                point.y = point.y + 25
                end_point = sd.get_point(point.x + 45, point.y + 10)
                sd.line(point, end_point, color=sd.COLOR_PURPLE, width=6)
            elif r == 1:
                point.x = point.x - 45
                point.y = point.y + 10
                end_point = sd.get_point(point.x + 45, point.y - 10)
                sd.line(point, end_point, color=sd.COLOR_PURPLE, width=6)
        # draw a nose
        point.x = point.x + 45
        point.y = point.y - 10
        end_point = sd.get_point(point.x, point.y - 40)
        sd.line(point, end_point, color=sd.COLOR_WHITE, width=10)
        # draw the lower lip
        for _ in range(2):
            r = (_ / 1) % 2
            if r == 0:
                point.x = point.x
                point.y = point.y - 65
                end_point = sd.get_point(point.x + 40, point.y + 15)
                sd.line(point, end_point, color=sd.COLOR_WHITE, width=7)
            elif r == 1:
                point.x = point.x - 40
                point.y = point.y + 15
                end_point = sd.get_point(point.x + 42, point.y - 15)
                sd.line(point, end_point, color=sd.COLOR_WHITE, width=7)
        # draw the upper lip
        point.x = point.x
        point.y = point.y
        end_point = sd.get_point(point.x + 80, point.y)
        sd.line(point, end_point, color=sd.COLOR_WHITE, width=7)
        # draw body
        point.x = point.x + 40
        point.y = point.y - 33
        end_point = sd.get_point(point.x, point.y - 80)
        sd.line(point, end_point, color=sd.random_color(), width=10)
        # draw hands
        color = sd.random_color()
        for _ in range(2):
            r = (_ / 1) % 2

            if r == 0:
                point.x = point.x
                point.y = point.y - 20
                end_point = sd.get_point(point.x + 70, point.y + 15)
                sd.line(point, end_point, color=color, width=6)
            elif r == 1:
                point.x = point.x - 70
                point.y = point.y + 15
                end_point = sd.get_point(point.x + 70, point.y - 15)
                sd.line(point, end_point, color=color, width=6)
        color = sd.random_color()
        for _ in range(2):
            r = (_ / 1) % 2

            if r == 0:
                point.x = point.x + 70
                point.y = point.y - 75
                end_point = sd.get_point(point.x + 60, point.y - 45)
                sd.line(point, end_point, color=color, width=6)
            elif r == 1:
                point.x = point.x - 60
                point.y = point.y - 45
                end_point = sd.get_point(point.x + 60, point.y + 45)
                sd.line(point, end_point, color=color, width=6)
smale_mane()

sd.pause()