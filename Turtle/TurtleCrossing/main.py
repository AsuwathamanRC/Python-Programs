import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
carManager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up,"Up")
screen.onkey(player.move_down,"Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    carManager.createCar()
    carManager.moveCars()

    # Detect collision with cars
    for car in carManager.all_cars:
        if car.distance(player)<20:
            game_is_on = False
            scoreboard.gameOver()

    # Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        carManager.levelUp()
        scoreboard.updateLevel()

screen.exitonclick()