from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("arrow")
        self.penup()
        self.left(90)
        self.goto(STARTING_POSITION)
    
    def starter(self):
        self.forward(10)
        
    def go_to_start(self):
        self.goto(STARTING_POSITION)