import simple_draw as sd


rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

def rainbow():
    radius = 1400
    point = sd.get_point(800, 100)
    # loop thet sort out rainbow_colors reduces radius and calla function  to draw circles
    for i in range(len(rainbow_colors)):
        radius -= 31
        sd.circle(point, radius, color=rainbow_colors[i], width=30)