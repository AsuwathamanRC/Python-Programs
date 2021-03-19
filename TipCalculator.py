#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

amount = float(input("What was the total bill? "))
percentage = float(input("What percentage would you like to give? "))
people = int(input("How many people to split the bil? "))

tip = round((( amount*(percentage/100) )+amount)/people,2)

print("Each person should pay: " + str(tip))