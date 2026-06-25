import turtle
import pandas

states_count = 0
us_map = turtle.Screen()
us_map.title("US States Game")
# us_map.bgpic("blank_states_img.gif") It also works but isn't the way for this challenge
us_img = "blank_states_img.gif"
us_map.addshape(us_img)
us_map.setup(730,500)
map=turtle.Turtle()
map.shape(us_img)

play = True

states = pandas.read_csv("50_states.csv")
remaining_states = states["state"].tolist()

while states_count != 50:
    ca = us_map.textinput(f"{states_count}/50 correct answers", "Name a US state: ").title()
    state_chosen = states[states.state == ca]
  
    if ca != 'Exit':
        if not state_chosen.empty:
            remaining_states.remove(ca)
            x= state_chosen.x.iloc[0]
            y= state_chosen.y.iloc[0]
            states_count += 1
            s_name = turtle.Turtle()
            s_name.penup()
            s_name.hideturtle()
            s_name.goto(x, y)
            s_name.write(f"{ca}", False, "center", ("Arial", 10, "bold"))
    else:
        ms = pandas.DataFrame({"missing states": remaining_states})
        ms.to_csv("missing_states.cvs")
        break






