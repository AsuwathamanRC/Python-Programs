student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

# Scores 91 - 100: Grade = "Outstanding"
# Scores 81 - 90: Grade = "Exceeds Expectations"
# Scores 71 - 80: Grade = "Acceptable"
# Scores 70 or lower: Grade = "Fail"

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
    if student_scores[student]>90:
        grade = "Outstanding"
    elif 80<student_scores[student]<91:
        grade = "Exceeds Expectations"
    elif 70<student_scores[student]<81:
        grade = "Acceptable"
    else:
        grade = "Fail"
    
    student_grades[student] = grade
    

# 🚨 Don't change the code below 👇
print(student_grades)