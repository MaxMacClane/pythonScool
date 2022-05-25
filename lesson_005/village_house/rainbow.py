import simple_draw as sd
sd.resolution=800, 800

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

def rainbow():
    radius = 400
    point = sd.get_point(400, 400)
    # loop thet sort out rainbow_colors reduces radius and calla function  to draw circles
    for i in rainbow_colors:
        radius -= 31
        sd.circle(point, radius, color=i, width=30)


rainbow()

sd.pause()