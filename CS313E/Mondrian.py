#  File: Mondrian.py

#  Description: Draws a scenic background, random trees with fruits, and then writes poetry

#  Student Name: Kayne Khoury

#  Class ID number: 76

#  Student UT EID: kdk745

#  Course Name: CS 313E

#  Unique Number: 51730

#  Date Created: 3/5/2015

#  Date Last Modified: 3/7/2015

import turtle, random


            
def draw_leaf(ttl):

      ttl.color('green')

      ttl.begin_fill()

      ttl.circle(10,steps=3)

      ttl.color('dark green')

      ttl.circle(5,steps=3)

      ttl.end_fill()

      

def drawTree (ttl,n, length,size,dot):

      if length > 5 and dot < 2:

          ttl.pensize(size)

          color(ttl,n)

          

      
          ttl.forward (length)

          draw_leaf(ttl)

          color(ttl,n)

          
          
          ttl.right (20)
          ttl.pensize(size)
         
          drawTree (ttl,n-1, length - random.randint(5,15),size-0.5,dot-1)
          ttl.left (40)
         
          drawTree (ttl,n-1, length - random.randint(5,15),size,dot-1)
          ttl.right (20)
          ttl.backward (length)

      if length > 5 and dot >=2:

          ttl.pensize(size)
          

      
          ttl.forward(length)
          ttl.right (20)
          ttl.pensize(size)
         
          drawTree (ttl,n-1, length - random.randint(5,15),size-0.5,dot-1)
          ttl.left (40)
         
          drawTree (ttl,n-1, length - random.randint(5,15),size,dot-1)
          ttl.right (20)
          ttl.backward (length)

def gotos(ttl,x,y,n,dot):

      if n == 0:

            return

      else:

        ttl.goto(x,y)

        ttl.pendown()

        drawTree(ttl,n,random.randint(50,75),6,dot)

        ttl.penup()

        gotos(ttl,x-random.randint(50,100),y-random.randint(0,30),n-1,dot)

def color(ttl,x):

    x = random.randint(0,100)

    if 0 < x <=25:

        ttl.color('dark red')

    if 25 < x <=50:

        ttl.color('red')

    if 50 < x <=75:

        ttl.color('yellow')

    if 75 < x <=100:

        ttl.color('orange')

def draw_fruit(ttl,color,n,x_2,y_2):



      if n > 0:

            ttl.goto(x_2,y_2)

            ttl.right(45)

            ttl.color('purple')

            ttl.begin_fill()

            ttl.circle(20,steps = 9)

            ttl.end_fill()

            ttl.goto(x_2,y_2+2)

            ttl.color('green')

            ttl.begin_fill()

            ttl.circle(5,steps=3)

            ttl.right(45)

            ttl.circle(5,steps=3)      

            ttl.end_fill()

            draw_fruit(ttl,color,n-1,x_2-random.randint(50,100),y_2-random.randint(0,50))


def main():

    x = random.randint(0,200)

    x_2 = x - 5

    y = random.randint(-200,0)

    y_2 = y - 5

    n = int(input("Enter a level of recursion between 1 and 6: "))

    dot = n -2

    turtle.setup(800,800,0,0)

    

    ttl = turtle.Turtle()

    ttl.speed(0)

    # create background
    

    ttl.left(90)

    ttl.penup()

    ttl.goto(-400,0)

    # create sky

    ttl.color('orange')

    ttl.begin_fill()

    ttl.pendown()

    ttl.goto(400,0)

    ttl.goto(400,400)

    ttl.goto(-400,400)

    ttl.goto(-400,0)

    ttl.end_fill()

    ttl.penup()

    ttl.goto(0,0)

    # create sun


    ttl.color('red','yellow')

    ttl.begin_fill()

    while True:

          ttl.forward(100)

          ttl.left(70)

          if abs(ttl.pos()) < 1:

                break

    ttl.end_fill()

    ttl.goto(-400,50)

    # create sea

    ttl.color('navy')

    ttl.begin_fill()

    ttl.goto(-400,0)

    ttl.goto(400,0)

    ttl.goto(400,50)

    ttl.goto(-400,50)

    ttl.end_fill()

    ttl.penup()

    ttl.goto(-400,50)

    ttl.color('brown')

    ttl.begin_fill()

    ttl.goto(-357,100)

    ttl.goto(-325,60)

    ttl.goto(-320,89)

    ttl.goto(-313,75)

    ttl.goto(-309,80)

    ttl.goto(-300,55)

    ttl.goto(-285,135)

    ttl.goto(-280,128)

    ttl.goto(-270,145)

    ttl.goto(-266,95)

    ttl.goto(-230,63)

    ttl.goto(-200,52)

    ttl.goto(-179,90)

    ttl.goto(-150,75)

    ttl.goto(-145,80)

    ttl.goto(-140,65)

    ttl.goto(-133,70)

    ttl.goto(-127,55)

    ttl.goto(-120,50)
    

    ttl.goto(-400,50)

    ttl.end_fill()

    

    

    # create ground/shore

    ttl.color('brown')

    ttl.goto(-400,0)

    ttl.pendown()

    ttl.begin_fill()

    ttl.goto(-400,-400)

    ttl.goto(400,-400)

    ttl.goto(400,0)

    ttl.goto(-400,0)

    ttl.end_fill()

    ttl.penup()

    ttl.pensize(2)

    # begin random, recursive part of code

    gotos(ttl,x,y,n,dot)

    draw_fruit(ttl,'purple',n,x_2,y_2)

    ttl.penup()

    # write poetry

    ttl.goto(-350,325)

    ttl.color('white')

    ttl.write("The fruit of the random tree, hath fallen in entropy",font=("Times new Roman",18,"normal"))

    ttl.ht()

    turtle.done()

main()


                  

    
