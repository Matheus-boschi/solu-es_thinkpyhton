import turtle
"""Se n é diferente de 0, a tartaruga move-se para frente length * n unidades.

    Rotaciona 50 graus para a esquerda.

    Chama draw(t, length, n-1) recursivamente.

    Rotaciona 100 graus para a direita.

    Chama draw(t, length, n-1) novamente.

    Rotaciona 50 graus para a esquerda.

    Move-se para trás length * n unidades.
"""
def draw (t, lenght, n) : 
    if n == 0 :
        return
    angle = 50
    t.fd(lenght * n)
    t.lt(angle)
    draw(t, lenght, n-1)
    t.rt(2 * angle)
    draw(t, lenght, n - 1)
    t.lt(angle)
    t.bk(lenght * n)

t = turtle.Turtle()
screen = turtle.Screen
t.speed(1)

draw(t, 10, 5)

screen.mainloop()


