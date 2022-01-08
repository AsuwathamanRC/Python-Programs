from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 60, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(0,280)
        self.hideturtle()
        self.lScore = 0
        self.rScore = 0
        self.updateScoreboard()

    def updateScoreboard(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.lScore, move=False, align=ALIGNMENT, font=FONT)
        self.goto(100,200)
        self.write(self.rScore, move=False, align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.lScore += 1
        self.updateScoreboard()

    def r_point(self):
        self.rScore += 1
        self.updateScoreboard()

    def updateWinner(self):
        self.goto(0,0)
        self.write("* * * GAME ENDS * * *", move=False, align=ALIGNMENT, font=('Arial', 40, 'normal'))