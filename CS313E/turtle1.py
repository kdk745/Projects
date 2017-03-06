import turtle

def main():

  turtle.setup(800,800,0,0)


  ttl = turtle.Turtle()

  ttl.penup()

  ttl.goto(-200,-50)

  ttl.pendown()

  ttl.circle(100,steps = 3)

  turtle.done()

main()
