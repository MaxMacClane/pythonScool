import simple_draw as sd
import village_house as vi

vi.ground()

st_point = sd.get_point(1600, 100)
_length = 175
_angle = 90
vi.draw_branches(s_point=st_point, length=_length, angle=_angle)

vi.rainbow()
vi.smale_mane()
vi.sun()
vi.wall()
vi.cloud()
vi.snowfall()

sd.pause()
