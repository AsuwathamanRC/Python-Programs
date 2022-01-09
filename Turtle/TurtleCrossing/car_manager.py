from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

# Y_POSITIONS = [0,30,60,90,120,150,180,210,240,270,-30,-60,-90,-120,-150,-180,-210,-240,-270]


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.carSpeed = STARTING_MOVE_DISTANCE

    def createCar(self):
        randomChance = random.randint(1,6)
        if randomChance == 6:
            newCar = Turtle("square")
            newCar.penup()
            newCar.shapesize(stretch_wid=1,stretch_len=2)
            newCar.color(random.choice(COLORS))
            newCar.goto(x=300,y=random.randrange(-250,250,30))
            self.all_cars.append(newCar)

    def moveCars(self):
        for car in self.all_cars:
            car.backward(self.carSpeed)

    def levelUp(self):
        self.carSpeed += MOVE_INCREMENT