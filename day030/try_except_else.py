try:  # contains the code that supposedly may get an error
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["jey"])
    
except FileNotFoundError:  # execute code if there is an error. In this case if the file doesn't exist
    file = open("a_file.txt", "w")
    file.write("Something")
    
except KeyError as error_message: # execute this code if the requested key is not in a_dictionary
    print(f"The key {error_message} does not exist.")
    
else:  # If there wasn't errors in "try"
    content = file.read()
    
finally:  # code executed no matter what happens inside the blocks above
    file.close()
    print("File was closed")

# we can generate our own exceptions by using "raise" keyword
height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Height not valid. Human height is 3 meters high.")

bmi = weight / height**2
print(f"Body Mass Index: {round(bmi, 2)}")
