student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.

student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇

for grades in student_scores:
    if student_scores[grades] <= 70:        
        student_grades[grades] = "Fail"        
    elif  student_scores[grades] > 70 and student_scores[grades] <= 80:        
        student_grades[grades] = "Acceptable"        
    elif  student_scores[grades] > 80 and student_scores[grades] <= 90:        
        student_grades[grades] = "Exceeds Expectations"        
    else:        
        student_grades[grades] = "Outstanding"        

# 🚨 Don't change the code below 👇
print(student_grades)

