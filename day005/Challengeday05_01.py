#input a Python list of students heights
student_heights = input().split()
total_height = 0
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
#Don0t change the code above
    total_height += student_heights[n]

#Write your code below this row
print(f"Total Height: {total_height}")
print(f"Number of Students: {len(student_heights)}")
print(f"Average height: {round(total_height/len(student_heights))}")