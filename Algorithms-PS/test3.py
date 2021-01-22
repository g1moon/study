
import turtle
import random
turtle.bgcolor('black')
colors=["red","purple","blue","green","yellow","orange"]
turtle.speed(15)
for a in range(30):
    turtle.goto(random.randint(-350,350), random.randint(-350,350))
    turtle.pendown()
    l = random.randint(50,300)
    turtle.color('black', colors[random.randint(0,5)])
    turtle.begin_fill()
    t = 5
    while t > 0: 
        turtle.forward(l)
        turtle.right(360 / 5 * 2)
        t = t -1
    turtle.end_fill()
    turtle.penup()


