import turtle
coords=[(-100,-100),(0,0),(100,-100)]
line_cords=[(-50,-50),(50,-50)]
turtle.setup(400,400)
turtle.penup()
turtle.goto(coords[0])
turtle.pendown()
for i in coords[1:]:
    turtle.goto(i)
turtle.penup()
turtle.goto(line_cords[0])
turtle.pendown()
turtle.goto(line_cords[1])
turtle.done()