def format_name(f_name, l_name):
    """gives format to a string and turn it into a capittalized or titled text"""
    w_name=""
    w_name = f_name.capitalize() + " "
    w_name += l_name.capitalize() + "."    
    return w_name

first_name=input("What's your first name?")
last_name=input("And, what's your last name?")

print(f"Your whole name is {format_name(first_name, last_name)}")
