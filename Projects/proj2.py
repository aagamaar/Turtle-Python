import turtle
import colorsys

def kaleidoscopic_spiral(turns=100, size=5, speed=0):
    turtle.speed(speed)
    turtle.bgcolor("black")
    h = 0

    for i in range(turns):
        color = colorsys.hsv_to_rgb(h, 1, 1)
        turtle.color(color)
        turtle.circle(size + i, 90)
        turtle.left(120)
        h += 0.005

    turtle.hideturtle()
    turtle.done()

kaleidoscopic_spiral(turns=200, size=2, speed=0)