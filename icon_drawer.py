import turtle

f = 4
h = 400

turtle.penup()
turtle.pensize(70)
turtle.pencolor((0, 0, 0))
turtle.shape(name=None)
turtle.bgcolor("#ECBAFC")

turtle.pencolor("#CF00FF")
turtle.setpos(0,0+h)
turtle.pendown()
turtle.setpos(150*f,-50*f+h)
turtle.setpos(0,-100*f+h)
turtle.setpos(150*f,-150*f+h)
turtle.setpos(0,-200*f+h)
turtle.penup()

turtle.setpos(100*f,0+h)
turtle.pendown()

turtle.pencolor("#A85BBA")
turtle.setpos(200*f,0+h)
turtle.setpos(200*f,-100*f+h)
turtle.setpos(100*f,-100*f+h)
turtle.setpos(200*f,-100*f+h)
turtle.setpos(200*f,-200*f+h)

a = input()
