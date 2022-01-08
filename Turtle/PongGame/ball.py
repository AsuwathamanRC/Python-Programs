from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x = 10
        self.y = 10
        self.move_speed = 0.1

    def move(self):
        self.goto(self.xcor()+self.x,self.ycor()+self.y)
        self.bounce()

    # Detect Top and Bottom walls and bounce
    def bounce(self):
        y_pos = self.ycor()
        if y_pos>=290 or y_pos<=-290:
            self.y *= -1

    # Reset ball if anyone paddle misses the ball
    def resetBall(self):
        # Reset move speed
        self.move_speed = 0.1
        # Change direction
        self.x *= -1
        self.y *= -1
        self.goto(0,0)