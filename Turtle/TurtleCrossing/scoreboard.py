from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.color("black")
        self.goto(-280,250)
        self.hideturtle()
        self.updateScoreboard()

    def updateScoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}",align="Left",font=FONT)

    def updateLevel(self):
        self.level += 1
        self.updateScoreboard()

    def gameOver(self):
        self.goto(0,0)
        self.write(f"* * Game Over * *",align="Center",font=FONT)