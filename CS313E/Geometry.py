#  File: Geometry.py

#  Description: Basic Geometry

#  Student Name: Juanito Taveras

#  Student UT EID: jmt3686

# Class ID: 150

#  Partner Name: Kayne Khoury

#  Partner UT EID: kdk745

# Class ID: 76

#  Course Name: CS 313E

#  Unique Number: 51730

#  Date Created: 2/10/2015

#  Date Last Modified: 2/14/2015

import math

def readCoord(inFile):         # function that reads the coordinates and outputs them as floats
  line1 = inFile.readline()    # reads line
  line1 = line1.strip()        # strips white space
  line1 = line1[:10]           # slices string to remove comments
  line1 = line1.strip()        # re-strips white space
  line1 = line1.split(" ")     # splits coordinates and puts them into a list
  coor1 = float(line1[0])      # makes x-coordinate
  coor2 = float(line1[-1])     # makes y-coordinate
  return (coor1, coor2)        # returns x and y coordinates

def readCoord_circle(inFile):  # function that reads radius and coordinates and outputs them as floats
  line = inFile.readline()     # reads line
  line = line.strip()          # strips white space
  line = line[:12]
  line = line.strip()
  line = line.split(" ")
  radius = float(line[0])
  x = float(line[1])
  y = float(line[2])
  return (radius, x, y)


class Point (object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get distance to another Point object
  def dist (self, other):
    return math.hypot (self.x - other.x, self.y - other.y)

  # create a string representation of a Point (x, y)
  def __str__ (self):
    return '(' + str(self.x) + ', ' + str(self.y) + ')'

  # test for equality between two points
  def __eq__ (self, other):
    tol = 1.0e-18
    return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))


class Line (object):
  # constructor assign default values if user defined points are the same
  def __init__ (self, p1_x = 0, p1_y = 0, p2_x = 1, p2_y = 1):
    tol = 1.0e-18
    if (abs(p1_x - p2_x) < tol) and (abs(p1_y - p2_y)< tol):
      self.p1 = Point (0, 0)
      self.p2 = Point (1, 1)
    else:
      self.p1 = Point (p1_x, p1_y)
      self.p2 = Point (p2_x, p2_y)

  # determine if line is parallel to x axis
  def is_parallel_x (self):
    tol = 1.0e-18
    return (abs(self.p1.y - self.p2.y)) < tol

  # determine if line is parallel to y axis
  def is_parallel_y (self):
    tol = 1.0e-18
    return (abs(self.p1.x - self.p2.x)) < tol

  # determine slope for the line
  # return float ('inf') if line is parallel to the y-axis
  def slope (self):
    if self.is_parallel_y():
      return float('inf')
    else:
      return (self.p1.y - self.p2.y) / (self.p1.x - self.p2.x)

  # determine the y-intercept of the line
  def y_intercept (self):
    return self.p1.y - (self.slope() * self.p1.x)

  # determine the x-intercept of the line
  def x_intercept (self):
    return -1.0 * self.y_intercept() / self.slope()


  # determine if two lines are parallel
  def is_parallel (self, other):
    tol = 1.0e-18
    return abs(self.slope() - other.slope()) < tol

  # determine if two lines are perpendicular to each other
  def is_perpendicular (self, other):
    tol = 1.0e-18
    return abs(self.slope() - ((-1)/other.slope())) < tol

  # determine if a point is on the line or on an extension of it
  def is_on_line (self, p):
    tol = 1.0e-18
    return abs((p1.y) - self.slope() * self.p1.x + self.y_intercept()) < tol

  # determine the perpendicular distance of a point to the line
  def perp_dist (self, p):

    test_line = Line()

    test_line.p1.x = p.x

    test_line.p1.y = p.y

    if ((p.x > self.p2.x or p.x < self.p2.x) and p.x < self.p1.x):

      test_line.p2.x = self.p1.x

      test_line.p2.y = ((-1/self.slope()) * self.p1.x) + (p.y - ((-1/self.slope()) * p.x))

      

    if ((p.x > self.p1.x or p.x < self.p1.x) and p.x < self.p2.x):

      test_line.p2.x = self.p2.x

      test_line.p2.y = ((-1/self.slope()) * self.p2.x) + (p.y - ((-1/self.slope()) * p.x))



    x_int = (self.y_intercept() - test_line.y_intercept())/((-1/self.slope()) - self.slope())
    y_int = self.slope() * x_int + self.y_intercept()

    dist = math.hypot (x_int - p.x, y_int - p.y)

    return round(dist)
  

  # determine the intersection point of two lines if not parallel
  def intersection_point (self, other):
    x_int = (self.y_intercept() - other.y_intercept())/(other.slope() - self.slope())
    y_int = self.slope() * x_int + self.y_intercept()
    return (x_int, y_int)

  # determine if two points are on the same side of the line
  # return False if one or both points are on the line

  def on_same_side (self, p1, p2):

    return (p1.y > self.slope() * p1.x + self.y_intercept() \
            and p2.y > self.slope() * p2.x + self.y_intercept()) \
            or (p1.y < self.slope() * p1.x + self.y_intercept() and p2.y < self.slope() + p2.x + self.y_intercept())
    

  # string representation of the line - one of three cases
  # y = c
  # x = c
  # y = m * x + b
  def __str__ (self):
    m = self.slope()
    b = self.y_intercept()
    output = ''
    #if b < 0:
    #  return ('y = ' + m + 'x' + abs(b))
    if m < 0:
      output = 'y = -' + str(abs(m)) + ' x'
    elif m == 0:
      output = 'y = ' 

    else:
      output = 'y = ' + str(m) + ' x'
    if b == 0:
      return output
    elif b > 0:
      return (output + ' + ' + str(b))
    elif b < 0:

        return (output + ' - ' + str(abs(b)))


class Circle (object):
  # constructor with default values
  def __init__ (self, radius = 1, x = 0, y = 0):
    self.radius = radius
    self.center = Point (x, y)

  # compute circumference
  def circumference (self):
    return 2.0 * math.pi * self.radius

  # compute area
  def area (self):
    return math.pi * self.radius * self.radius

  # determine if a point is inside the circle
  def is_inside_point (self, p):
    return (self.center.dist (p) < self.radius)
    

  # determine if the other circle is strictly inside self
  def is_inside_circle (self, other):
    distance = self.center.dist(other.center)
    return (distance + other.radius) < self.radius

  # determine if the other circle intersects self
  def does_intersect_circle (self, other):
    distance = self.center.dist (other.center)
    return distance < (self.radius + other.radius)

  # determine if the line intersects circle
  def does_intersect_line (self, line):

      return Line.perp_dist(line,self.center) <= self.radius

    
  # determine if the line is tangent to the circle

  def is_tangent (self, c):

      return Line.perp_dist(self,c.center)  == c.radius



  # string representation of a circle
  
  # Radius: radius, Center: (x, y)

  def __str__ (self):
    return "Radius: " + str(self.radius) + " Center: " + str(self.center)

def main():
    
  # open file "geometry.txt" for reading
  inFile = open ("./geometry.txt", "r")
  
  # read the coordinates of the first Point P
  p1_x, p1_y = readCoord(inFile)
  p1 = Point (p1_x, p1_y)

 # read the coordinates of the second Point Q
  p2_x, p2_y = readCoord(inFile)
  p2 = Point (p2_x, p2_y)

  # print the coordinates of points P and Q
  print ("Coordinates of P:", p1)
  print ("Coordinates of Q:", p2)

  # print distance between P and Q
  print ("Distance between P and Q:", Point.dist(p1, p2))

  # print the slope of the line PQ
  line1 = Line (p1_x, p1_y, p2_x, p2_y)
  print ("Slope of PQ:", Line.slope(line1))

  # print the y-intercept of the line PQ
  print ("Y-Intercept of PQ:", Line.y_intercept(line1))

  # print the x-intercept of the line PQ
  print ("X-Intercept of PQ:", Line.x_intercept(line1))

  # read the coordinates of the third Point A
  p3_x, p3_y = readCoord(inFile)
			 
  # read the coordinates of the fourth Point B
  p4_x, p4_y = readCoord(inFile)


  # print the string representation of the line AB
  line2 = Line (p3_x, p3_y, p4_x, p4_y)
  print ("Line AB:", Line.__str__(line2))

  # print if the lines PQ and AB are parallel or not
  if Line.is_parallel (line1, line2):
    print ("PQ is parallel to AB")
  else:
    print ("PQ is not parallel to AB")

  # print if the lines PQ and AB (or extensions) are perpendicular or not
  if Line.is_perpendicular (line1, line2):
    print ("PQ is perpendicular to AB")
  else:
    print ("PQ is not perpendicular to AB")

  # print coordinates of the intersection point of PQ and AB if not parallel
  if not Line.is_parallel (line1, line2):
    print ("Intersection point of PQ and AB:", Line.intersection_point (line1, line2))

  # read the coordinates of the fifth Point G
  p5_x, p5_y = readCoord(inFile)
  g = Point (p5_x, p5_y)

  # read the coordinates of the sixth Point H
  p6_x, p6_y = readCoord (inFile)
  h = Point (p6_x, p6_y)

  # print if the the points G and H are on the same side of PQ

  if Line.on_same_side(line1,g,h):

    print('G and H are on the same side of PQ')

  else:

    print('G and H are not on the same side of PQ')
  
  # print if the the points G and H are on the same side of AB

  if Line.on_same_side(line2,g,h):

    print('G and H are on the same side of AB')

  else:

    print('G and H are not on the same side of AB')

  # read the radius of the circleA and the coordinates of its center
  circleA = readCoord_circle (inFile)

  calist = []

  for i in circleA:

    if i == 3.0 or i == 2.0 or i == 2.0:

      calist.append(i)
 # create circleA
  CircleA = Circle()

  CircleA.radius = calist[0]

  CircleA.center.x = calist[1]

  CircleA.center.y = calist[2]

  # read the radius of the circleB and the coordinates of its center
  circleB = readCoord_circle (inFile)

  cblist = []

  for i in circleB:

    if i == 1.5 or i == 2.2 or i == 1.8:

      cblist.append(i)
 # create circleB
  CircleB = Circle()

  CircleB.radius = cblist[0]

  CircleB.center.x = cblist[1]

  CircleB.center.y = cblist[2]

  # print the string representation of circleA and circleB
  print ('circleA:', CircleA.__str__())
  print ('circleB:', CircleB.__str__())

  # determine if circleB is inside circleA
  if Circle.is_inside_circle (CircleA, CircleB):
    print ("circleB is inside circleA")
  else:
    print ("circleB is not inside circleA")

  # determine if circleA intersects circleB
  if Circle.does_intersect_circle (CircleA, CircleB):
    print ("circleA does intersect circleB")
  else:
    print ("circleA does not intersect circleB")
    

  # determine if line PQ (or extension) intersects circleA
  if Circle.does_intersect_line (CircleA, line1):
    print ("PQ does intersect circleA")
  else:
    print ("PQ does not intersect circleA")

 

  # determine if line AB (or extension) is tangent to circleB
  if Circle.is_tangent(line2,CircleB):
    print ("AB is a tangent to circleB")
  else:
    print ("AB is not a tangent to circleB")

  # close file "geometry.txt"

   
  inFile.close()

main()
