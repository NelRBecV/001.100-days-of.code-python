student_scores = {"Harry": 81,
                  "Ron": 78,
                  "Hermione": 99,
                  "Draco": 74,
                  "Neville": 65
}
#Don't change the code above
#TODO-1 Create an empty dictionary called student_grades

#TODO-2 Write your code below and add the grades to the student_grades
student_grades = {}
print(student_scores)

for key in student_scores:
    if student_scores[key] > 90:
        student_grades[key]="Oustanding"
    elif student_scores[key] > 80:
        student_grades[key] = "Exceeds expectations"
    elif student_scores[key] > 70:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

print(student_grades)
#Don't change the code above
