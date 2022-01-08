from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(x_pos,y_pos)

    def move_up(self):
        self.goto(self.xcor(),self.ycor()+20)
        
    def move_down(self):
        self.goto(self.xcor(),self.ycor()-20)