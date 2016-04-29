import math
import turtle
from datetime import datetime
from PIL import Image

DEGREES_IN_CIRCLE = 360

def drawCircle(x, y, r):
    turtle.up()
    turtle.setpos(x+r,y)
    turtle.down()
    for i in range(0, DEGREES_IN_CIRCLE):
        a = math.radians(i+1)
        turtle.setpos(x+r*math.cos(a), y+r*math.sin(a))



def drawSpiro( R, r, l):
    turtle.up()
    turtle.setpos(R-(r*(1-l)),0)
    turtle.down()
    k = r/R
    rotations = int(r/math.gcd(r,R))
    for i in range(0,rotations*DEGREES_IN_CIRCLE):
        t = math.radians(i+1)
        x = R*((1-k)*math.cos(t)+l*k*math.cos(t*(1-k)/k))
        y = R*((1-k)*math.sin(t)+l*k*math.sin(t*(1-k)/k))
        turtle.setpos(x, y)
    turtle.hideturtle()

def saveSpiro():
    dateStr = (datetime.now()).strftime("%d%b%Y-%H%M%S")
    fileName = "spiro" + dateStr 
    canvas=turtle.getcanvas()
    canvas.postscript(file = fileName + ".eps")
    img = Image.open(fileName + ".eps")
    img.save(fileName+".png", "png")
    print(fileName, "saved")
    


# drawCircle(210, 70, 0.7)

drawSpiro(190, 45, 0.6)
saveSpiro()
turtle.mainloop()