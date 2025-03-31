import turtle
import colorsys
import random

def enhanced_spiral(turns=120, size=2, speed=0, segments=4):
    turtle.speed(speed)
    turtle.bgcolor("black")
    turtle.pensize(2)
    h = 0

    for i in range(turns):
        for j in range(segments):
            color = colorsys.hsv_to_rgb(h, 1, 1)
            turtle.color(color)

            # Add some random variations:
            radius = size * (40 + j * 5) + random.randint(-10, 10) #random radius
            angle = 90 + random.randint(-15, 15) #random angle
            forward_distance = 250 + random.randint(-50, 50) #random forward distance

            turtle.circle(radius, angle)
            turtle.forward(forward_distance)
            turtle.left(90)

            h += 0.003 + random.uniform(-0.001, 0.001) #random hue change.

        turtle.right(10)
        
        # Add a pulsating effect:
        if i % 10 == 0:
            turtle.pensize(3)
        else:
            turtle.pensize(2)

    turtle.hideturtle()
    turtle.done()

enhanced_spiral(turns=150, size=2, speed=0, segments=5) #example call.