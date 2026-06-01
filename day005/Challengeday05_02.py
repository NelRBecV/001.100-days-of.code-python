#input a lis of students scores
student_scores = input().split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
#Don't change the code above
high_score = 0
low_score = 100
for n in range(0, len(student_scores)):
    if high_score < student_scores[n]:
        high_score = student_scores[n]
    if low_score > student_scores[n]:
         low_score = student_scores[n]

lowest_score = str(low_score)
if  low_score < 10:
    lowest_score = "0" + str(low_score)
print(f"The Highest score in this class is: {high_score} and the lowest is: {lowest_score}")
#Write your code below this row