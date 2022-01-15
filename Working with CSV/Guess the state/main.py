from os import stat
from turtle import Turtle, Screen
import turtle
import pandas as p

IMAGE_PATH = r"Working with CSV\Guess the state\blank_states_img.gif"
CSV_PATH = r"Working with CSV\Guess the state\50_states.csv"

screen = Screen()
screen.title("U.S. States Game")
screen.addshape(IMAGE_PATH)
turtle.shape(IMAGE_PATH)

statePosition = Turtle()
statePosition.penup()
statePosition.hideturtle()

data = p.read_csv(CSV_PATH)
stateList = data.state.to_list()
answer_list = []

# xList = data.x.to_list()
# yList = data.y.to_list()

# To get the state coordinates
# def getMouseClickCoor(x,y):
#     print(x,y)
# turtle.onscreenclick(getMouseClickCoor)
# turtle.mainloop()

score = 0

game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f"Guess the state({score+1}/50)", prompt="What's another state name?").title()
    
    if answer_state.lower()=="exit":
        # learning_list = []
        # for state in stateList:
        #     if state not in answer_list:
        #         learning_list.append(state)

        # Using list comprehension
        learning_list = [state for state in stateList if state not in answer_list]
        newData = p.DataFrame(learning_list)
        newData.to_csv(r"Working with CSV\Guess the state\states_to_learn.csv")
        break            
    
    if answer_state in stateList:
        # pos = stateList.index(answer_state)
        # x_pos = xList[pos]
        # y_pos = yList[pos]
        # statePosition.goto(x_pos,y_pos)
        state_data = data[data.state == answer_state]
        statePosition.goto(int(state_data.x),int(state_data.y))
        statePosition.write(answer_state.title() , move=False, align="center", font=('Arial', 10, 'normal'))
        score += 1
        answer_list.append(answer_state)

    if score==50:
        game_is_on = False

screen.exitonclick()