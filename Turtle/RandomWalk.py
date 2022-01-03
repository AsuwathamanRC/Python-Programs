import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

tim.pensize(5)
tim.speed("fastest")

########### Challenge 4 - Random Walk ########
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen","khaki", "green yellow", "blue", "orange red"]
direction = [0,90,180,270]

def randomColor():
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    return (red,green,blue)

for _ in range(250):
    tim.color(randomColor())
    tim.setheading(random.choice(direction))
    tim.forward(15)

t.exitonclick()