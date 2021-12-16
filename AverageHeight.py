# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
# You should not use the sum() or len() functions

#Write your code below this row 👇
total_height = 0
count = 0
for height in student_heights:
    total_height += height
    count += 1

print("Total height: " + str(height) + "\nTotal student count: " + str(count))
print("Average height = " + str(round(total_height/count)))
