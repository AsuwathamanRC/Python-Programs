# Body Mass Index Calculator

#BMI = weight/(height*height)

weight = input("Enter your weight (in kg) : ")
height = input("Enter you height (in m) : ")

BMI = float(weight)/float(height)**2

print("Your BMI is : " + str(BMI))