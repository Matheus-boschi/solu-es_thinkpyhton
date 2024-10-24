import turtle

def draw_petal(t, length, angle):
    for _ in range(2):
        t.circle(length, angle)
        t.left(180 - angle)

def draw_flower(t, num_petals, length, angle):
    for _ in range(num_petals):
        draw_petal(t, length, angle)
        t.left(360 / num_petals)

def main():
    t = turtle.Turtle()
    screen = turtle.Screen()
    t.speed(10)
    
    num_petals = 6
    length = 50
    
    # Experimente diferentes ângulos aqui
    angles = [30, 45, 50, 60, 70, 90, 180]
    
    for angle in angles:
        t.penup()
        t.goto(0, 0)
        t.pendown()
        t.clear()
        draw_flower(t, num_petals, length, angle)
        screen.update()
    
    screen.mainloop()

if __name__ == "__main__":
    main()




