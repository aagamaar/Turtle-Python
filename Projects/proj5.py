import turtle
import colorsys

def hypnotic_circles(radius=10, num_circles=50, speed=0):
    turtle.speed(speed)
    turtle.bgcolor("black")
    h = 0

    for _ in range(num_circles):
        color = colorsys.hsv_to_rgb(h, 1, 1)
        turtle.color(color)
        turtle.circle(radius)
        radius += 5
        h += 0.01

    turtle.hideturtle()
    turtle.done()

hypnotic_circles(radius=5, num_circles=100, speed=0)