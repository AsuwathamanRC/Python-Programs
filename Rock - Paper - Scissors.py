import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

gestures = [rock, paper, scissors]

computer_choice = random.randint(0,2)

print("User choice:\n" + gestures[user_choice])
print("\nComputer choice:\n" + gestures[computer_choice])

if (user_choice<0 or user_choice>2):
    print("You typed an invalid number, you lose!") 
elif (user_choice==0 and computer_choice==1) or (user_choice==1  and computer_choice==2) or (user_choice==2  and computer_choice==0):
    print("Computer wins!")
elif user_choice==computer_choice:
    print("Draw!")
else:
    print("User wins!")