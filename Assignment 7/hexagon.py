import turtle
turtle.setup(400, 400)
turtle.speed(2)
turtle.penup()
turtle.goto(-50, 50)
turtle.pendown()
turtle.color("red", "yellow") 
turtle.begin_fill()  
for i in range(6):
    turtle.forward(100)
    turtle.right(60)
turtle.end_fill()
turtle.done()
