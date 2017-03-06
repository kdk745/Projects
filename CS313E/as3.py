#  File: Geometry.py

#  Description:

#  Student Name: Juanito Taveras

#  Student UT EID: jmt3686

#  Partner Name: Kayne

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created: 2/10/2015

#  Date Last Modified: 

import math

def readCoord(inFile):
  line1 = inFile.readline()
  line1 = line1.strip()
  line1 = line1[:10]
  line1 = line1.strip()
  line1 = line1.split(" ")
  coor1 = float(line1[0])
  coor2 = float(line1[-1])
  return (coor1, coor2)


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
      return (self.p2.y - self.p1.y) / (self.p2.x - self.p1.x)

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

    test_line.p1.x = p.y

    if ((p.x > self.p2.x or p.x < self.p2.x) and p.x < self.p1.x):

      test_line.p2.x = self.p1.x

      test_line.p2.y = ((-1/self.slope()) * self.p1.x) + (p.y - ((-1/self.slope()) * p.x))

      

    if ((p.x > self.p1.x or p.x < self.p1.x) and p.x < self.p2.x):

      test_line.p2.x = self.p2.x

      test_line.p2.y = ((-1/self.slope()) * self.p2.x) + (p.y - ((-1/self.slope()) * p.x))



    x_int = (self.y_intercept() - test_line.y_intercept())/((-1/self.slope()) - self.slope())
    y_int = self.slope() * x_int + self.y_intercept()

    return math.hypot (x_int - p.x, y_int - p.y)

    

      

      

    

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
    
    return ("y = " + str(m) + "x + " + str(b))



'''
class Circle (object):
  # constructor with default values
  def __init__ (self, radius = 1, x = 0, y = 0):

  # compute circumference
  def circumference (self):

  # compute area
  def area (self):

  # determine if a point is inside the circle
  def is_inside_point (self, p):

  # determine if the other circle is strictly inside self
  def is_inside_circle (self, other):

  # determine if the other circle intersects self
  def does_intersect_circle (self, other):

  # determine if the line intersects circle
  def does_intersect_line (self, line):

  # determine if the line is tangent to the circle
  def is_tangent (self, line):

  # string representation of a circle
  # Radius: radius, Center: (x, y)
  def __str__ (self):
'''

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
  line2 = Line (p3_x, p3_y,p4_x,p4_y)
              
  print ("Line AB:", line2.__str__())

  print(p3_x,p3_y,p4_x,p4_y)

  # print if the lines PQ and AB are parallel or not
  if Line.is_parallel (line1, line2):
    print ("PQ is parallel to AB")
  else:
    print ("PQ is not parallel to AB")
  '''
  # print if the lines PQ and AB (or extensions) are perpendicular or not
  if Line.is_perpendicular (line1, line2):
    print ("PQ is perpendicular to AB")
  else:
    print ("PQ is not perpendicular to AB")
  '''
  # print coordinates of the intersection point of PQ and AB if not parallel
  if not Line.is_parallel (line1, line2):
    print ("Intersection point of PQ and AB:", Line.intersection_point (line1, line2))

  # read the coordinates of the fifth Point G
  p5_x, p5_y = readCoord(inFile)

  G = Point(p5_x,p5_y)

  # read the coordinates of the sixth Point H
  p6_x, p6_y = readCoord (inFile)

  H = Point(p6_x,p6_y)

  # print if the the points G and H are on the same side of PQ

  if Line.on_same_side(line1,G,H):

    print('Points G and H are on the same side of PQ')

  else:

    print('Points G and H are not on the same side of PQ')


  

  # print if the the points G and H are on the same side of AB

  if Line.on_same_side(line2,G,H):

    print('Points G and H are on the same of AB')

  else:

    print('Points G and H are not on the same side of AB')



  # read the radius of the circleA and the coordinates of its center

  # read the radius of the circleB and the coordinates of its center

  # print the string representation of circleA and circleB

  # determine if circleB is inside circleA

  # determine if circleA intersects circleB

  # determine if line PQ (or extension) intersects circleA

  # determine if line AB (or extension) is tangent to circleB

  # close file "geometry.txt"
  inFile.close()

main()
