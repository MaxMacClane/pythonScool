import simple_draw as sd


radius = 100
point = sd.get_point(300, 1000)

sd.start_drawing()

def sun():

    sd.circle(center_position=point, radius=radius, color=sd.COLOR_YELLOW, width=0)
    angle = 45

    for _ in range(12):
        sd.vector(point, angle=angle, length=270, color=sd.COLOR_YELLOW, width=7)
        angle += 30
    # for _ in range(12):
    #     sd.circle(center_position=point, radius=200, color=sd.background_color, width=10)


sun()
sd.finish_drawing()
sd.sleep(0.1)
# sd.pause()
