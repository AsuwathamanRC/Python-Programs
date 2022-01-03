import turtle as t
import random

tim = t.Turtle()
tim.color("red", "green")

########### Challenge 3 - Draw Shapes ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def drawShape(sides):
    for _ in range(sides):
        tim.forward(100)
        tim.right(360/sides)

for side in range(3,11):
    tim.color(random.choice(colours))
    drawShape(side)

t.exitonclick()