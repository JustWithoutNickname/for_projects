import turtle

SPEEd = 0
LENGTH = 400
COLOR = "red"
SIZE = 2

START_X = -200
START_Y = 0
COUNT_OF_LINES = 20
ANGLE = 162


turtle.speed(SPEEd)
turtle.penup()
turtle.goto(START_X, START_Y)
turtle.pendown()
turtle.pencolor(COLOR)
for i in range(COUNT_OF_LINES):
    turtle.forward(LENGTH)
    turtle.left(ANGLE)
turtle.done()