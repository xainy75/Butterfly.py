from turtle import *
from math import sin, cos, exp

tracer(1)
bgcolor('#1a0033')

for t in range(0, 628, 2):
    t_rad = t / 100
    x = sin(t_rad) * (exp(cos(t_rad)
    ) - 2*cos(4*t_rad) - sin(t_rad/12)**5)

    y = cos(t_rad) * (exp(cos(t_rad)
    ) - 2*cos(4*t_rad) - sin(t_rad/12)**5)

    red = abs(sin(t_rad * 2))
    green = abs(cos(t_rad * 3))
    blue = (1 + sin(t_rad * 5)) / 2
    s = 5
    up()
    goto(x * 85, y * 85)
    color(red, green, blue)
    dot(s)
done()
