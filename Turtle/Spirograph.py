import turtle as t
import random

tim = t.Turtle()
tim.speed("fastest")
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

########### Challenge 5 - Spirograph ########
def drawSpirograph(gap):
    for _ in range(int(360/gap)):
        tim.color(random_color())
        tim.setheading(tim.heading() + gap)
        tim.circle(100)

drawSpirograph(5)
t.exitonclick()