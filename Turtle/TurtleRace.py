from turtle import Turtle, Screen
import random

screen_width = 500
screen_height = 500
x_pos = ((screen_width/2)-20) * -1
y_pos = -225

screen = Screen()
# Set screen width and height
screen.setup(width=screen_width,height=screen_height)

is_race_on = False
# Ask the user to place a bet
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color:\n(red, orange, yellow, green, blue, indigo, violet)")

colors_list = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
turtle_list = []

if user_bet:
    is_race_on = True

# Create turtle object and assign starting position and color
for i in range(0,len(colors_list)):
    new_turlte = Turtle(shape="turtle")
    new_turlte.color(colors_list[i])
    new_turlte.penup()
    new_turlte.goto(x=x_pos,y=y_pos)
    turtle_list.append(new_turlte)
    y_pos += 75


while is_race_on:
    for player in turtle_list:
        player.forward(random.randint(0, 10))
        
        # Check if a turtle reaches the end point
        if player.xcor()>=230:
            is_race_on = False
            winning_color = player.pencolor()
            if winning_color.lower() == user_bet.lower():
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")


screen.exitonclick()