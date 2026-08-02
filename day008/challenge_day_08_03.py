# Write your code below this line
def paint_calc(height, width, cover):
    painting_calculation = round((width * height) / cover)
    print(f"You'll need {painting_calculation} cans of paint")
  
# Write your code above this line
# Define the function paint_calc() so the code below work
# Don't change the code above


test_h = int(input())  # test of height
test_v = int(input())  # test of weight

coverage = 5
paint_calc(height=test_h, width=test_v, cover=coverage)
