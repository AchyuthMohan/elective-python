import turtle
turtle.setup(400, 400)
turtle.speed(2)
hexagon_coords = [(0, 0), (50, 0), (75, 50), (50, 100), (0, 100), (-25, 50)]
turtle.penup()
turtle.goto(hexagon_coords[0])
turtle.pendown()
turtle.fillcolor("red")
turtle.begin_fill()
for coord in hexagon_coords[1:]:
    turtle.goto(coord)
turtle.goto(hexagon_coords[0])
turtle.end_fill()
turtle.done()
