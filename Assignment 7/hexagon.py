# colored hexagon
import turtle
turtle.setup(500,500)
turtle.pencolor('red')
turtle.fillcolor('yellow')
turtle.begin_fill()
for i in range(6):
    turtle.forward(100)
    turtle.left(60)
turtle.end_fill()
turtle.done()