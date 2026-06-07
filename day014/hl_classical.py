from hl_logo import vs_logo, first_c, second_c


def play_classical_mode(person1, person2):
    fans_person1 = person1['Fans']
    fans_person2 = person2['Fans']
    first_c()
    
    print(f"This is {person1['Name']}. He/she is {person1['Occupation']} who is born in {person1['Country']}")
    print(f"and got {fans_person1} fans in his/her instagram account")
    
    vs_logo()
    second_c()
    
    print(f"This is {person2['Name']}. He/She is {person2['Occupation']} who is born in {person2['Country']}")
    print(f"{person2['Name']}'s fans amount is higher or lower than {person1['Name']}")
    
    user_choice = input("Type 'h' for higher, or 'l' for lower: ").lower()
    
    print(fans_person1)
    print(fans_person2)
    
    if user_choice[0].lower() == "h":
        return fans_person2 > fans_person1
    elif user_choice[0].lower() == "l":
        return fans_person2 < fans_person1
    

