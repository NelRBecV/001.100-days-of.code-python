print("Welcome to the tip Calcualtor!")
total_bill= float(input("What was the total bill? $"))
tip_percent = float(input("How much tip would you like to give? 10, 12, 15? "))
people_sharing = int(input("How many people to split the bill? "))

tip_bill = (total_bill * (tip_percent / 100)) + total_bill
bill_split = round(tip_bill / people_sharing,2)

print(f"Each person should pay: ${bill_split}" + "     Normal double float")
print(f"Each person should pay: $" + "{:.2f}".format(bill_split) + "    Precise double float")
#"{:.2f}".format(variable) es codigo para resolver el problema de doble núemro flotante preciso
#como el se se usa para manejar cifras relacionadas con monedas (Centavos y céntimos)