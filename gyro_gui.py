from graphics import *
from math import cos , sin ,radians

#Drawing x and y Lines
def drawXaxis( x , y ):
    line = Line(Point( width/2 - x ,width/2 - y),Point( width/2 + x , width/2 + y ))
    line.setOutline(color_rgb(160,32,240))
    line.setWidth(2)
    line.draw(win)
    time.sleep(0.01)
    for line in win.items[:]:
        line.undraw()
    win.update()

def drawYaxis( x1 , y1 , x2 , y2 ):
    line = Line(Point(x1,y1),Point(x2,y2))
    line.setOutline(color_rgb(255,0,255))
    line.setWidth(5)
    line.draw(win)

#Rotate lines
def rotateXaxis( degree ):
    drawXaxis((width/2)*sin(radians(degree+90)),(width/2)*cos(radians(degree+90)))

#Defining window size
width=400
degree = 0
# Creating window with x and y axis
win = GraphWin("Gyroscopic View",width,width)
win.setBackground(color_rgb(0,0,0))

def create_axis():
    xaxis = Line( Point(0,width/2),Point(width, width/2))
    xaxis.setOutline(color_rgb(0,0,255))
    yaxis = Line( Point(width/2,0),Point(width/2, width))
    yaxis.setOutline(color_rgb(0,0,255))
    xaxis.draw(win)
    yaxis.draw(win)

while True:
#    degree = input("Enter the angle of the line in degrees : ")
    if degree==800:
    #degree=='x':
        win.getMouse()
        win.close()
        break
    else:
        create_axis()
        rotateXaxis(int(degree))
        degree += 1
