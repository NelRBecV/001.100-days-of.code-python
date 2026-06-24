import os

with open("/input/invited_names.txt") as names:
    name_list = names.readlines()#Reada every single line in a txt file
    name_list
    names.close()

with open("/input/starting_letter.txt") as letter:
    letter_content = letter.read()#Read all the content in a txt file
    letter.close()
    
if not os.path.exists("ReadyToSend"):#Checks if the directory exists
    os.mkdir("./ReadyToSend")

for inv_name in name_list:
    invitation = letter_content.replace("[name]", f"{inv_name[0:len(inv_name)-1]}")
    guest = open(f"./ReadyToSend/letter_for_{inv_name[0:len(inv_name)-1]}.txt","w")
    #{inv_name[0:len(inv_name)-1]} allows to print the string without taking New Line symbol (\n)
    guest.write(invitation)
    guest.close()
