import turtle

screen = turtle.Screen()
t = turtle.Turtle()

screen.onkeypress(lambda: t.forward(10), "w")
screen.onkeypress(lambda: t.backward(10), "s")
screen.onkeypress(lambda: t.left(90), "a")
screen.onkeypress(lambda: t.right(90), "d")

def toggle_pen():
    if t.isdown():
        t.penup()
    else:
        t.pendown()

screen.onkeypress(toggle_pen, "space")

screen.listen()
screen.mainloop()