#Challenge 1
numbers: list = [n * 2 for n in range(1,5)]

#Challenge 2
names: list = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
upper_names: list = [name.upper() for name in names if len(name) > 5]
print(upper_names)

#Challenge 3
with open("file_1.txt") as list1:
    set1: list = list1.read().split()
    list1.close()
    
with open("file_2.txt") as list2:
    set2: list = list2.read().split()
    list2.close()
    
inters: list = [int(num) for num in set1 if num in set2]
print(inters)

#Dictionary Comprehension
import random


Student_names: list = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_scores: dict = {names: random.randint(1, 100) for names in Student_names}
#My method
# passed_students = {names: students_scores[names] for names in Student_names if students_scores[names] >= 60}

#Angela's Method
passed_students: list = {student:score for (student, score) in students_scores.items() if score >= 60}
print(students_scores)
print(passed_students)

#Challenge 4
all_words: list = input("Introduce a sentence:\n").split()

letters_in_words: dict = {word: len(word) for word in all_words}
print(letters_in_words)
