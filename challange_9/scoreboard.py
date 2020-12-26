from turtle import Turtle
import time
FONT = ("Courier", 15, "normal")

# time = time()
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-250,270)
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f" Level:{self.level}", align = "center", font = FONT)
    
    def increase_level(self):
        self.level += 1
        self.goto(0,0)
        self.write(" Level Up!", align = "center", font =("Courier", 20, "normal"))
        time.sleep(0.4)
        self.clear()
        self.goto(-250,270)
        self.update_scoreboard()
        
    def game_over(self):
        self.goto(0,0)
        self.write(" GAME OVER", align = "center", font =("Courier", 25, "normal"))