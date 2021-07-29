from turtle import Turtle, Screen
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)


tim. speed(0)
tim.shape("turtle")
# tim.width(width = 100)
# tim.pensize(width = 20)

def draw_circle(size_of_gap):
    for x in range(int(360 / size_of_gap)):
        choice = random_color()
        tim.pencolor(choice)
        tim.circle(80)
        tim.setheading(tim.heading() + size_of_gap)

for x in range(5,10
               ):
    draw_circle(x)


screen = Screen()
screen.exitonclick()