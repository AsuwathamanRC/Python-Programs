import colorgram
import random
import turtle as t

tim = t.Turtle()
tim.speed("fastest")
t.colormode(255)

# Extract colors from an image
rgb_colors = []
# colors = colorgram.extract('Turtle\HirstPainting\image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     newColor = (r,g,b)
#     rgb_colors.append(newColor)
# print(rgb_colors)

colorList = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

tim.setpos(0,0)
tim.penup()
tim.hideturtle()

y = 0

for _ in range(10):
    tim.setpos(0,y)
    for _ in range(10):
        tim.dot(20,random.choice(colorList))
        tim.forward(50)
    y += 50


screen = t.Screen()
screen.exitonclick()
