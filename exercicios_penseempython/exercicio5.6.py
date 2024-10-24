import turtle

def koch(t, length):
    if length < 3:
        t.forward(length)
    else:
        length /= 3
        koch(t, length)
        t.left(60)
        koch(t, length)
        t.right(120)
        koch(t, length)
        t.left(60)
        koch(t, length)

def snowflake(t, lenght) : 
    for _ in range(3) :
        koch(t, lenght)
        t.right(120)

t = turtle.Turtle()
t.speed(0)

snowflake(t, 100)

turtle.done()





    
    