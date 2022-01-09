from turtle import Turtle, position

STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.body = []
        self.createSnake()
        self.head = self.body[0]

    def createSnake(self):        
        for position in STARTING_POSITION:
            self.addBody(position)
        
    def addBody(self,position):
        new_body = Turtle("square")
        new_body.penup()
        new_body.color("white")
        new_body.goto(position)
        self.body.append(new_body)

    def reset(self):

        for b in self.body:
            b.goto(1000,1000)

        self.body.clear()
        self.createSnake()
        self.head = self.body[0]

    def extend(self):
        self.addBody(self.body[-1].position())
    
    def move(self):
        for body_num in range(len(self.body)-1,0,-1):
            x_pos = self.body[body_num-1].xcor()
            y_pos = self.body[body_num-1].ycor()
            self.body[body_num].goto(x_pos,y_pos)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)