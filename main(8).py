import turtle as t

def r(horizontal, vertical, color):
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.begin_fill()
    for counter in range(1, 3):
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)
    t.end_fill()
    t.penup()
    t.speed('slow')
    t.bgcolor('Dodger blue')

t.penup()
t.goto(-100, -150)
r(50, 20, 'blue')
t.goto(-30, -150)
r(50, 20, 'blue')

t.goto(-25, -50)
r(15, 100, 'grey')
t.goto(-55, -50)
r(-15, 100, 'grey')

t.goto(-90, 100)
r(100, 150, 'red')

t.goto(-150, 70)
r(60, 15, 'grey')
t.goto(-150, 110)
r(15, 40, 'grey')

t.goto(10, 70)
r(60, 15, 'grey')
t.goto(55, 110)
r(15, 40, 'grey')

t.goto(-50, 120)
r(15, 20, 'grey')

t.goto(-85, 170)
r(80, 50, 'red')

t.goto(-60, 160)
r(30, 10, 'white')
t.goto(-55, 155)
r(5, 5, 'black')
t.goto(-40, 155)
r(5, 5, 'black')

t.goto(-65, 135)
r(40, 5, 'black')

t.goto(-155, 130)
r(25, 25, 'green')
t.goto(-147, 130)
r(10, 15, t.bgcolor())
t.goto(50, 130)
r(25, 25, 'green')
t.goto(58, 130)
r(10, 15, t.bgcolor())

t.hideturtle()




