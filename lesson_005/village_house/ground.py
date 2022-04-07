import simple_draw as sd
heigth = 800
width = 1600
sd.resolution = width, heigth

def ground():
    start = sd.get_point(0, 0)
    end = sd.get_point(2000, 0)
    width = 200
    sd.line(start_point=start, end_point=end, color=sd.COLOR_GROUND, width=width)


ground()

# sd.pause()
