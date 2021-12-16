import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

l = len(names)

i = random.randint(0,l-1)

print(names[i] + " is going to buy the meal today!" + str(l))