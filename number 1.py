import turtle
turtle.setup(750,500)
turtle.bgcolor('pink')
turtle.pencolor('blue')
turtle.pensize(2)
turtle.speed(4)
turtle.right(45)
turtle.fillcolor("yellow")
turtle.begin_fill()
for i in range(3):
    turtle.forward(100)
    turtle.left(90)
turtle.forward(200)
#my_turtle.end_fill()
#my_turtle.begin_fill()
for i in range(3):
    turtle.right(90)
    turtle.forward(100)
turtle.end_fill()
turtle.done()
#my_turtle.getscreen()._root.mainloop()  # <-- run the Tkinter main loop

#print( "%.3f" %(34.99998))


