from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")



# def turtle_creators(name,x_axis,y_axis):
#     name = Turtle()
#     name.shape("square")
#     name.color("white")
#     name.goto(x = x_axis,y = y_axis)


# turtle_creators("boss",0,0)
# turtle_creators("tiger",-20,0)
# turtle_creators("lion",-40,0)


start = [(0,0), (-20,0), (-40,0)]
screen.tracer(0)

segments = []

for pos in start:
    new_seg = Turtle("square")
    new_seg.color("white")
    new_seg.penup()
    new_seg.goto(pos)
    segments.append(new_seg)
    

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    for seg_num in range(len(segments)-1,0,-1 ):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments(seg_num).goto(new_x,new_y)
    segments[0].forward(20)
        









screen.exitonclick()