import turtle
import random

def fractal_tree(branch_len, t):
    if branch_len > 5:
        t.color(random.choice(["green", "brown", "lightgreen"]))
        t.forward(branch_len)
        t.right(20)
        fractal_tree(branch_len - 15, t)
        t.left(40)
        fractal_tree(branch_len - 15, t)
        t.right(20)
        t.backward(branch_len)

def main():
    t = turtle.Turtle()
    window = turtle.Screen()
    t.left(90)
    t.penup()
    t.backward(100)
    t.pendown()
    fractal_tree(100, t)
    window.exitonclick()

main()