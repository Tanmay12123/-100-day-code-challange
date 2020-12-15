from turtle import Turtle,Screen
import random

automatrix = Turtle()

num = [0,1]


colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
def returner():
    for i in range(4):
        automatrix.color(random.choice(colours))
        automatrix.pensize(10)
        automatrix.left(90)
        automatrix.forward(150)


returner()
def door():
    automatrix.left(180)
    automatrix.forward(45)
    automatrix.right(90)
    automatrix.forward(60)
    automatrix.left(90)
    automatrix.forward(60)
    automatrix.left(90)
    automatrix.forward(60)
    automatrix.right(90)
door()



automatrix.forward(45)
automatrix.right(90)
automatrix.forward(150)
automatrix.right(90)
automatrix.forward(110)
automatrix.left(65)
automatrix.forward(80)
# for i in range(4):
#     automatrix.circle(10)
#     automatrix.forward(2)


automatrix.write("Automatrix")


















screen = Screen()
screen.exitonclick()