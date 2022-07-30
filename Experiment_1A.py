import turtle
t=turtle.Screen()
t.bgcolor("green")
t.title("Samuel Joseph")
pen=turtle.Turtle()
pen.color("orange")

for i in range(2):
    for i in range(4):
        pen.forward(100);
        pen.left(90);

    pen.goto(50,50)
    for i in range(4):
        pen.forward(100);
        pen.left(90);

    pen.goto(150,50)
    pen.goto(100,0)

    pen.goto(100,100)
    pen.goto(150,150)

    pen.goto(50,150)
    pen.goto(0,100)
    pen.goto(0,0)
    pen.color("blue")
    t.bgcolor("white")

turtle.done()
