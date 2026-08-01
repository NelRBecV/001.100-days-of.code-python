# input a Python list of students heights

student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

# Don't change the code above
# Write your code below this row
total_height: int = 0

for h in range(len(student_heights)):
    total_height += student_heights[h]

print(f"Total Height: {total_height}")
print(f"Number of Students: {len(student_heights)}")
print(f"Average height: {round(total_height/len(student_heights))}")
