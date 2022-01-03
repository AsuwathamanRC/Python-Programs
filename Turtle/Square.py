import turtle as t

######## Challenge 1 - Draw a Square ############
tim = t.Turtle()
tim.shape("turtle")
tim.color("red")

for _ in range(4):
    tim.forward(100)
    tim.right(90)

t.exitonclick()