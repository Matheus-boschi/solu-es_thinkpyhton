#EXERCICIOS AMOSTRAS
import turtle
bob = turtle.Turtle()
def square(t, length) : 
    for i in range (4) :    
        t.fd(length)
        t.lt(90)
# square(bob, 100)

# 3
bob = turtle.Turtle()
def polygon(t, n, length) :
    angle = 360 / n 
    polilyne(t, n, length, angle)
#4  

import math  
def circle(t, r) : 
    arc(t, r, 360)
 


#5
def arc(t, r, angle) :
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n 
    polilyne(t, n, step_length, step_angle)
    for i in range (n) : 
        t.fd(step_length)
        t.tl(step_angle)


def polilyne(t, n , length, angle) : 
    for i in range(n) : 
        t.fd(length)
        t.lt(angle)

circle()








    

