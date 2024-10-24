import turtle

def triangle(t, length) : 
    for _ in range(3) :
        t.forward(length)
        t.left(120)

def pentagono(t, length) :
    for _ in range(7) :
        triangle(t, length)
        t.forward(length)
        t.left(60)

    

t = turtle.Turtle()
t.speed(2)

pentagono(t, 50)
t.fd(50)

turtle.done()


    





