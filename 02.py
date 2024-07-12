import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_curve(order, size=200):
    window = turtle.Screen()
    window.bgcolor("white")


    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()
    
    for _ in range(3):
        t.right(120)
        koch_curve(t, order, size)

    window.mainloop()


level_of_recursion = int(input ("Input level of recursion: "))
draw_koch_curve(level_of_recursion)