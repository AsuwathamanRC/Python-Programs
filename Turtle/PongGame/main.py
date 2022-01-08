from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


rightPaddle = Paddle(350,0)
leftPaddle = Paddle(-350,0)
ball = Ball()
score = Scoreboard()


screen.listen()
screen.onkey(rightPaddle.move_up,"Up")
screen.onkey(rightPaddle.move_down,"Down")
screen.onkey(leftPaddle.move_up,"w")
screen.onkey(leftPaddle.move_down,"s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with right and left paddle
    x_pos = ball.xcor()
    if x_pos>=330 and ball.distance(rightPaddle)<=50 or x_pos<=-330 and ball.distance(leftPaddle)<=50:
        ball.x *= -1
        ball.move_speed *= 0.9

    # Detect if ball misses the paddle
    if x_pos>=380 or x_pos<=-380:
        if x_pos>=380:
            score.l_point()
        else:
            score.r_point()
        ball.resetBall()

    if score.lScore>=10 or score.rScore>=10:
        score.updateWinner()
        game_is_on = False


screen.exitonclick()