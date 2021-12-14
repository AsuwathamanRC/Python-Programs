# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name = name1 + name2
name.lower()

first_digit = 0
first_digit += name.count("t")
first_digit += name.count("r")
first_digit += name.count("u")
first_digit += name.count("e")

second_digit = 0
second_digit += name.count("l")
second_digit += name.count("o")
second_digit += name.count("v")
second_digit += name.count("e")

score = int(str(first_digit)+str(second_digit))

if score<10 or score>90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score>40 and score<50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
