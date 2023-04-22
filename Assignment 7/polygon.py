import turtle
turtle.setup(400, 400)
turtle.speed(2)
polygon_coords = [(0, 0), (50, 50), (100, 0), (100, -100), (0, -100)]
turtle.penup()
turtle.goto(polygon_coords[0])
turtle.pendown()
for coord in polygon_coords[1:]:
    turtle.goto(coord)
turtle.goto(polygon_coords[0])
turtle.done()
