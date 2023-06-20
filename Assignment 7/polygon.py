import turtle
polygon_coords = [(0, 0), (50, 50), (100, 0), (100, -100), (0, -100)]
turtle.setup(400,400)
turtle.penup()
turtle.goto(polygon_coords[0])
turtle.pendown()
for i in polygon_coords[1:]:
    turtle.goto(i)
turtle.goto(polygon_coords[0])
turtle.done()