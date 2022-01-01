from random import choice, randint
from art import logo, vs
from game_data import data

print(logo)
game_over = False
score = 0
a = randint(0,len(data)-1)

while not game_over:
    
    print("Compare A: "+data[a]["name"]+", a "+data[a]["description"]+", from "+data[a]["country"])

    print(vs)

    b = randint(0,len(data)-1)
    while b==a:
        b = randint(0,len(data)-1) #To make sure 'a' and 'b' values are not equal

    print("Against B: "+data[b]["name"]+", a "+data[b]["description"]+", from "+data[b]["country"])

    choice = input("Who has more followers? Type 'a' or 'b': ")

    if choice=='a' and data[a]["follower_count"]>=data[b]["follower_count"]:
        score += 1
        print(f"You're right! Current score: {score}")
        a = b
    elif choice=='b' and data[b]["follower_count"]>=data[a]["follower_count"]:
        score += 1
        print(f"You're right! Current score: {score}")
        a = b
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_over = True
