# Body Mass Index Calculator 2.0

#BMI = weight/(height*height)

weight = input("Enter your weight (in kg) : ")
height = input("Enter you height (in m) : ")

BMI = float(weight)/float(height)**2

BMI = round(BMI,2)

if BMI < 18.5:
    print("Your BMI is : " + str(BMI) + ", you are underweight.")
elif BMI < 25:
    print("Your BMI is : " + str(BMI) + ", you have a normal weight.")
elif BMI < 30:
    print("Your BMI is : " + str(BMI) + ", you are slightly overweight.")
elif BMI < 35:
    print("Your BMI is : " + str(BMI) + ", you are obese.")
else:
    print("Your BMI is : " + str(BMI) + ", you are clinically obese.")