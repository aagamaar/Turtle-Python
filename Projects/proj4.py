import turtle
import colorsys

def starburst_animation(segments=36, length=150, speed=0):
    turtle.speed(speed)
    turtle.bgcolor("black")
    h = 0

    for _ in range(360):
        color = colorsys.hsv_to_rgb(h, 1, 1)
        turtle.color(color)
        for _ in range(segments):
            turtle.forward(length)
            turtle.left(360 / segments)
        turtle.right(1)
        h += 0.003

    turtle.hideturtle()
    turtle.done()

starburst_animation(segments=6, length=100, speed=0)