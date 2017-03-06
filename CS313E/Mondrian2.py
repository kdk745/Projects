#  File: Mondrian.py

#  Description: Program that creates a random drawing varying complexity based on user input and outputs it as a .eps image.

#  Student Name: Juanito Taveras

#  Student UT EID: jmt3686

#  Course Name: CS 313E

#  Unique Number: 51730

#  Date Created: 3/3/2015

#  Date Last Modified: 3/3/2015


import turtle, random    # import modules

# function that picks a random color
def color(color_list):                                             # input is list of colors
	return color_list[random.randint(0, len(color_list)-1)]    # output is random color


# function that outputs True or False using the probabily of the user entering 1 - 6
def is_random(rec):
	if 0 < rec <= 2:
		out = random.choice('xxxxxxxxyyxxxx')    # 0 - 2 is highest likelihood x will be chosen
	elif 3 <= rec <= 4:
		out = random.choice('xxxyyyyyyxxx')
	elif rec == 5:
		out = random.choice('xxyyyyyyyx')
	elif rec == 6:                                   # 6 is highest likelihood that y will be chosen
		out = random.choice('xyyyyyyyyyyy')
	if out == 'y':                                   # if y is chosen, return True
		return True
	else:                                            # else, return false
		return False

# function that makes a border and fills it with a color
def border(ttl, canvas_color):
	ttl.width(10)
	ttl.penup()
	ttl.goto(-395, -395)
	ttl.pendown()
	ttl.seth(0)
	ttl.fillcolor(canvas_color)
	ttl.begin_fill()
	for i in range(4):
		ttl.forward(790)
		ttl.left(90)
	ttl.end_fill()

# function that makes a recursively bigger circle, each time turning 15 degrees
def draw_circles(ttl, x, y, width, start, radius, seth, color_list):
	if start < radius:                                                                         # circles keep increasing in size, shifting 15 degrees from each other
		ttl.penup()							                   # until the reach size 'radius'
		ttl.goto(x, y)
		ttl.pendown()
		ttl.color(color(color_list))  # chooses random color from color list every time
		ttl.width(width)
		ttl.seth(seth)
		ttl.circle(start)
		draw_circles(ttl, x, y, width + 0.05, start + 2.5, radius, seth + 15, color_list)  # calls itself again with bigger circle, thinner pen, 15 degrees right


# function that makes recursively smaller triangles	
def draw_triangles(ttl, x, y, side, seth, color_list, width):
	if side > 0:
		ttl.penup()
		ttl.goto(x, y)
		ttl.pendown()
		ttl.color(color(color_list))
		ttl.seth(seth)
		for i in range(3):
			ttl.forward(side)
			ttl.left(120)
		draw_triangles(ttl, x + 5, y + 5, side - 10, seth, color_list, width - 0.1)  # calls itself again with shifted triangle, smaller, thinner pen
		



def main():

	# make a list of colors to randomly choose from
	color_list = ['red', 'green', 'blue', 'yellow', 'orange', 'brown', 'blue', 'purple', 'gray']



	turtle.title('Recursive Composition')        # title of drawing
	turtle.setup(800, 800, 0, 0)                 # create 800 x 800 screen
	ttl = turtle.Turtle()                        # create turtle
	ttl.speed(0)                                 # set turtle speed
	ttl.hideturtle()                             # hide turtle

	# print beautiful poem
	print ('Random Recursive Composition \n')
	print ('Recursion is but a fact of life')
	print ('Randomness as well')
	print ('Again and again occurs joy and strife')
	print ('As does rando - SOFT TACO SHELLS')
	
	# have user input level of recursion
	rec = int(input('Enter a level of recursion between 1 and 6: '))

	# make black canvas
	canvas_color = 'black'
	border(ttl, canvas_color)
	
	radius = rec * 50
	side = rec * 75
	

	# if user enters zero, return a blank screen
	if rec == 0:
		canvas_color = 'white'
		border(ttl, canvas_color)
		ts = turtle.getscreen()
		ts.getcanvas().postscript(file = 'Mondrian.eps')
		return

	# make main triangle
	ttl.width(2)
	draw_triangles(ttl, -350, -350, 700, 0, color_list, 5)

	# make random x and y variables
	x = random.randint(-400, 400)
	y = random.randint(-400, 400)

	# if True is randomly output based on user input, switch x and y
	if is_random(rec):
		x, y = y, x
		
	count = 0
	if is_random(rec) and count < 6:       # if True draw recursive circles as long as count is less than 6
		ttl.width(2)
		draw_circles(ttl, x, y, 0.5, 1, radius, 0, color_list)
		count += 1
	elif not is_random(rec) and count < 6:  # if False draw two recursive triangles of random size
		ttl.width(2)
		draw_triangles(ttl, x, y,  random.randint(0, 300), 0, color_list, 5)
		draw_triangles(ttl, y, x, random.randint(0, 300), 0, color_list, 5)
		count += 1



	# save as .eps
	ts = turtle.getscreen()
	ts.getcanvas().postscript(file = "Mondrian.eps")

main()


		
