user_answer = turtle.textinput(title="Guessed the State",prompt="Name another state")
for place in states:
    if user_answer ==place:
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state = data[data.state == user_answer]
        t.goto(int(state.x), int(state.y))
        t.write(user_answer)
