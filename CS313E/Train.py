#  File: Train.py

#  Description: Draws a train with turtle graphics

#  Student Name: Kayne Khoury

#  Student UT EID: kdk745 class id:76

#  Course Name: CS 313E

#  Unique Number: 51730

#  Date Created:2/17/2015

#  Date Last Modified:2/18/2015

import turtle

import math

# draw a square of a given side 
# starting at uuper left corner (x, y)
def drawSquare (ttl, x, y, side):
  ttl.penup()
  ttl.goto(x, y)
  ttl.setheading(0)	# set the pen in the +ve x direction
  ttl.pendown()
  ttl.begin_fill()
  ttl.color('gray')
  for iter in range (4):
    ttl.forward(side)
    ttl.right(90)
  ttl.end_fill()
  ttl.penup()

def drawSquare2 (ttl, x, y, side):
  ttl.penup()
  ttl.goto(x, y)
  ttl.setheading(0)	# set the pen in the +ve x direction
  ttl.pendown()
  for iter in range (4):
    ttl.forward(side)
    ttl.right(90)
  ttl.penup()


  # draw a line from (x1, y1) to (x2, y2)
def drawLine (ttl, x1, y1, x2, y2):
  ttl.penup()
  ttl.goto (x1, y1)
  ttl.pendown()
  ttl.goto (x2, y2)
  ttl.penup()

def drawPolygon (ttl, x, y, num_side, radius):
  sideLen = 2 * radius * math.sin (math.pi / num_side)
  angle = 360 / num_side
  ttl.penup()
  ttl.goto (x, y)
  ttl.pendown()
  for iter in range (num_side):
    ttl.forward (sideLen)
    ttl.left (angle)

def main():

    turtle.setup ( 800, 800, 0, 0)

    ttl = turtle.Turtle()

    ttl.color('blue')

    ttl.pensize(2)

    # draw top rectangle

    drawLine(ttl,-200*1.5,0,-100*1.5,0)

    drawLine(ttl,-100*1.5,0,-100*1.5,-5*1.5)

    drawLine(ttl,-100*1.5,-5*1.5,-200*1.5,-5*1.5)

    drawLine(ttl,-200*1.5,-5*1.5,-200*1.5,0)

    # draw lines for engineer's room

    drawLine(ttl,-190*1.5,-5*1.5,-190*1.5,-105*1.5)

    drawLine(ttl,-110*1.5,-5*1.5,-110*1.5,-105*1.5)

    # draw engineer windows

    drawSquare(ttl,-180*1.5,-15*1.5,25*1.5)

    drawSquare(ttl,-145*1.5,-15*1.5,25*1.5)

    ttl.color('blue')

    drawSquare2(ttl,-180*1.5,-15*1.5,25*1.5)

    drawSquare2(ttl,-145*1.5,-15*1.5,25*1.5)

    # draw body of train

    drawLine(ttl,-110*1.5,-20*1.5,70*1.5,-20*1.5)

    drawLine(ttl,70*1.5,-20*1.5,70*1.5,-115*1.5)

    # draw front of train

    drawLine(ttl,70*1.5,-90*1.5,80*1.5,-90*1.5)

    drawLine(ttl,80*1.5,-90*1.5,80*1.5,-30*1.5)

    drawLine(ttl,80*1.5,-30*1.5,70*1.5,-30*1.5)

    drawLine(ttl,80*1.5,-80*1.5,85*1.5,-80*1.5)

    drawLine(ttl,85*1.5,-80*1.5,85*1.5,-40*1.5)

    drawLine(ttl,85*1.5,-40*1.5,80*1.5,-40*1.5)

    drawLine(ttl,70*1.5,-95*1.5,90*1.5,-95*1.5)

    drawLine(ttl,90*1.5,-95*1.5,100*1.5,-115*1.5)

    drawLine(ttl,100*1.5,-115*1.5,70*1.5,-115*1.5)

    # draw top part of train

    drawLine(ttl,30*1.5,-20*1.5,35*1.5,5*1.5)

    drawLine(ttl,35*1.5,5*1.5,10*1.5,5*1.5)

    drawLine(ttl,10*1.5,5*1.5,15*1.5,-20*1.5)

    drawLine(ttl,35*1.5,5*1.5,30*1.5,20*1.5)

    drawLine(ttl,30*1.5,20*1.5,15*1.5,20*1.5)

    drawLine(ttl,15*1.5,20*1.5,10*1.5,5*1.5)

    drawLine(ttl,-25*1.5,-20*1.5,-25*1.5,-10*1.5)

    drawLine(ttl,-25*1.5,-10*1.5,-55*1.5,-10*1.5)

    drawLine(ttl,-55*1.5,-10*1.5,-55*1.5,-20*1.5)

    drawLine(ttl,-30*1.5,-10*1.5,-30*1.5,-5*1.5)

    drawLine(ttl,-30*1.5,-5*1.5,-50*1.5,-5*1.5)

    drawLine(ttl,-50*1.5,-5*1.5,-50*1.5,-10*1.5)

    # draw dots and detail on train body

    for i in range(-164,105,5):

        ttl.goto(i,-61*1.5)

        ttl.dot(2*1.5,'black')

    for j in range(-86,-31,5):

        ttl.goto(21*1.5,j)

        ttl.dot(2*1.5,'black')

        ttl.goto(-60*1.5,j)

        ttl.dot(2*1.5,'black')

    drawLine(ttl,-110*1.5,-59*1.5,70*1.5,-59*1.5)

    drawLine(ttl,-110*1.5,-63*1.5,70*1.5,-63*1.5)

    drawLine(ttl,23*1.5,-59*1.5,23*1.5,-20*1.5)

    drawLine(ttl,19*1.5,-59*1.5,19*1.5,-20*1.5)

    drawLine(ttl,-58*1.5,-59*1.5,-58*1.5,-20*1.5)

    drawLine(ttl,-63*1.5,-59*1.5,-63*1.5,-20*1.5)

    # draw wheel wells

    drawLine(ttl,-190*1.5,-105*1.5,-180*1.5,-105*1.5)

    drawLine(ttl,-110*1.5,-105*1.5,-120*1.5,-105*1.5)

    ttl.goto(-150*1.5,-135*1.5)

    ttl.circle(30*1.5,90)

    ttl.pendown()

    ttl.circle(30*1.5,180)

    ttl.penup()

    ttl.goto(-90*1.5,-105*1.5)

    ttl.circle(30*1.5,180)

    ttl.pendown()

    ttl.circle(30*1.5,180)

    drawLine(ttl,-110*1.5,-105*1.5,-90*1.5,-105*1.5)

    ttl.penup()

    ttl.goto(-11*1.5,-105*1.5)

    ttl.circle(30*1.5,180)

    ttl.pendown()

    ttl.circle(30*1.5,180)

    drawLine(ttl,-11*1.5,-105*1.5,-30*1.5,-105*1.5)

    drawLine(ttl,50*1.5,-105*1.5,70*1.5,-105*1.5)

    ttl.penup()

    ttl.color('black')

    #draw tracks

    drawLine(ttl,-200*1.5,-135*1.5,120*1.5,-135*1.5)

    drawLine(ttl,-200*1.5,-140*1.5,120*1.5,-140*1.5)

    for i in range(-293,180,28):

        drawLine(ttl,i,-140*1.5,i,-142*1.5)

        drawLine(ttl,i,-142*1.5,i+10*1.5,-142*1.5)

        drawLine(ttl,i+10*1.5,-142*1.5,i+10*1.5,-140*1.5)

    # draw wheels

    ttl.color('red')

    # first wheel

    ttl.goto(-175*1.5,-110*1.5)

    ttl.pendown()

    ttl.circle(25*1.5)

    ttl.penup()

    ttl.goto(-170*1.5,-110*1.5)

    ttl.pendown()

    ttl.circle(20*1.5)

    ttl.penup()

    ttl.goto(-155*1.5,-110*1.5)

    ttl.pendown()

    ttl.circle(5*1.5)

    ttl.penup()

    drawLine(ttl,-168*1.5,-112*1.5,-155*1.5,-110*1.5)

    drawLine(ttl,-168*1.5,-108*1.5,-155*1.5,-110*1.5)

    drawLine(ttl,-198.5,-168,-218,-165)

    drawLine(ttl,-198.5,-162,-218,-165)

    drawLine(ttl,-228,-138.5,-225,-158)

    drawLine(ttl,-222,-138.5,-225,-158)

    drawLine(ttl,-228,-191.5,-225,-172)

    drawLine(ttl,-222,-191.5,-225,-172)

    drawLine(ttl,-203,-145,-219.7,-160.2)

    drawLine(ttl,-206,-140,-219.7,-160.2)

    drawLine(ttl,-244,-140,-230.3, -160.2)

    drawLine(ttl,-247,-145,-230.3,-160.2)

    drawLine(ttl,-244,-183,-230.3,-170.8)

    drawLine(ttl,-247,-178,-230.3,-170.8)

    drawLine(ttl,-203,-178,-219.7,-170.8)

    drawLine(ttl,-206,-183,-219.7,-170.8)

    # second wheel

    ttl.goto(-175*1.5+135,-110*1.5)

    ttl.pendown()

    ttl.circle(25*1.5)

    ttl.penup()

    ttl.goto(-170*1.5+135,-110*1.5)

    ttl.pendown()

    ttl.circle(20*1.5)

    ttl.penup()

    ttl.goto(-155*1.5+135,-110*1.5)

    ttl.pendown()

    ttl.circle(5*1.5)

    ttl.penup()

    drawLine(ttl,-168*1.5+135,-112*1.5,-155*1.5+135,-110*1.5)

    drawLine(ttl,-168*1.5+135,-108*1.5,-155*1.5+135,-110*1.5)

    drawLine(ttl,-198.5+135,-168,-218+135,-165)

    drawLine(ttl,-198.5+135,-162,-218+135,-165)

    drawLine(ttl,-228+135,-138.5,-225+135,-158)

    drawLine(ttl,-222+135,-138.5,-225+135,-158)

    drawLine(ttl,-228+135,-191.5,-225+135,-172)

    drawLine(ttl,-222+135,-191.5,-225+135,-172)

    drawLine(ttl,-203+135,-145,-219.7+135,-160.2)

    drawLine(ttl,-206+135,-140,-219.7+135,-160.2)

    drawLine(ttl,-244+135,-140,-230.3+135, -160.2)

    drawLine(ttl,-247+135,-145,-230.3+135,-160.2)

    drawLine(ttl,-244+135,-183,-230.3+135,-170.8)

    drawLine(ttl,-247+135,-178,-230.3+135,-170.8)

    drawLine(ttl,-203+135,-178,-219.7+135,-170.8)

    drawLine(ttl,-206+135,-183,-219.7+135,-170.8)

    # third wheel

    
    ttl.goto(-175*1.5+253,-110*1.5)

    ttl.pendown()

    ttl.circle(25*1.5)

    ttl.penup()

    ttl.goto(-170*1.5+253,-110*1.5)

    ttl.pendown()

    ttl.circle(20*1.5)

    ttl.penup()

    ttl.goto(-155*1.5+253,-110*1.5)

    ttl.pendown()

    ttl.circle(5*1.5)

    ttl.penup()

    drawLine(ttl,-168*1.5+253,-112*1.5,-155*1.5+253,-110*1.5)

    drawLine(ttl,-168*1.5+253,-108*1.5,-155*1.5+253,-110*1.5)

    drawLine(ttl,-198.5+253,-168,-218+253,-165)

    drawLine(ttl,-198.5+253,-162,-218+253,-165)

    drawLine(ttl,-228+253,-138.5,-225+253,-158)

    drawLine(ttl,-222+253,-138.5,-225+253,-158)

    drawLine(ttl,-228+253,-191.5,-225+253,-172)

    drawLine(ttl,-222+253,-191.5,-225+253,-172)

    drawLine(ttl,-203+253,-145,-219.7+253,-160.2)

    drawLine(ttl,-206+253,-140,-219.7+253,-160.2)

    drawLine(ttl,-244+253,-140,-230.3+253, -160.2)

    drawLine(ttl,-247+253,-145,-230.3+253,-160.2)

    drawLine(ttl,-244+253,-183,-230.3+253,-170.8)

    drawLine(ttl,-247+253,-178,-230.3+253,-170.8)

    drawLine(ttl,-203+253,-178,-219.7+253,-170.8)

    drawLine(ttl,-206+253,-183,-219.7+253,-170.8)

    ttl.ht()


    turtle.done()

    

main()

    
