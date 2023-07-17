import turtle
r=0.8
g=0
b=0
turtle.setup(500,500)
turtle.pencolor(r,g,b)
turtle.fillcolor('yellow')
turtle.begin_fill()
for i in range(6):
    turtle.forward(100)
    turtle.right(60)
turtle.end_fill()
turtle.done()