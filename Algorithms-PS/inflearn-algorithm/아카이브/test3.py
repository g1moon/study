import turtle as t

information = [120,56,201,120,88,75,90,130,157,254,221,130]  

a = t.Screen()            
a.setworldcoordinates(-5, -5, 800, 400)

t.color("blue")
t.fillcolor("red")
t.pensize(3)

for height in information:
    
    t.begin_fill()              
    t.left(90)
    t.forward(height)
    t.write(str(height),  font = ("맑은고딕", 18, "bold"))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    
    t.right(90)
    t.forward(40)
    t.right(180)
    t.forward(40)
    
    t.end_fill()
        
    t.forward(10)

