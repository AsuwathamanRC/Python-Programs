from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 12, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(0,280)
        self.hideturtle()
        self.score = 0
        with open("Turtle/SnakeGame/data.txt") as f:
            self.highScore = int(f.read())
        self.updateScoreboard()

    def updateScoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.highScore}", move=False, align=ALIGNMENT, font=FONT)

    def increaseScore(self):
        # self.clear()
        self.score += 1
        self.updateScoreboard()

    def reset(self):
        if self.score>self.highScore:
            self.highScore = self.score
            with open("Turtle/SnakeGame/data.txt","w") as f:
                f.write(str(self.score))

        self.score = 0
        self.updateScoreboard()

    # def gameOver(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)