import turtle
import pandas

screen = turtle.Screen()
screen.screensize(400,400)
screen.title("States Game")
image = "C:/Users/home/Desktop/Tanmay The Entirety/Python Stuff/#100 day code challange/challange_11/us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#TODO: Get the answer from the user and use it to run through the .csv file through for loop

data = pandas.read_csv("C:/Users/home/Desktop/Tanmay The Entirety/Python Stuff/#100 day code challange/challange_11/us-states-game-start/50_states.csv")
states = data.state.to_list()
us = data.state
not_guessed = []
states_guessed=[]

while len(states_guessed) != 50:
    user_answer = turtle.textinput(title=f"Guessed States {len(states_guessed)}/50",prompt="Name another state").title()
    
    if user_answer == "Exit":
        for state in us:
            if state not in states_guessed:
                not_guessed.append(state)
        print(not_guessed)
        new_data = pandas.DataFrame(not_guessed)
        new_data.to_csv("states_to_learrn.csv")
        break
        
    for place in states:
        if user_answer ==place:
            states_guessed.append(user_answer)
            t = turtle.Turtle()
            t.penup()
            t.hideturtle()
            state = data[data.state == user_answer]
            t.goto(int(state.x), int(state.y))
            t.write(user_answer)
            




# for places in us:
#     pass
#     for guss in states_guessed:
#         if places == guss:
#             pass
#         elif guss != places:
#             not_guessed.append(places)
            
# print(not_guessed)




screen.exitonclick()

