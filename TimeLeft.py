# print how many days, weeks and months left
# if you live till 90 years
# Hint : There are 365 days in a year, 52 weeks in a year and 12 months in a year.

age = int(input("Enter your age : "))

yearsLeft = 90 - age
daysLeft = yearsLeft * 365
monthsLeft = yearsLeft * 12
weeksLeft = yearsLeft * 52

print("You have "+str(daysLeft)+" days, "+str(weeksLeft)+ " weeks, "+str(monthsLeft)+" months left.")