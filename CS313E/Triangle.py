import math

class Point (object):
  # constructor
  def __init__ (self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get distance to another Point object
  def dist (self, other):
    return math.hypot (self.x - other.x, self.y - other.y)

  # create a string representation of a Point
  def __str__ (self):
    return '(' + str (self.x) + ', ' + str (self.y) + ')'

  # test for equality between two points
  def __eq__ (self, other):
    tol = 1.0e-16
    return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

class Line (object):
  # constructor
  def __init__ (self, p1_x = 0, p1_y = 0, p2_x = 1, p2_y = 1):
    tol = 1.0e-18
    if ((abs(p1_x - p2_x) < tol) and (abs(p1_y - p2_y) < tol)):
      self.p1 = Point (0, 0)
      self.p2 = Point (1, 1)
    else:
      self.p1 = Point (p1_x, p1_y)
      self.p2 = Point (p2_x, p2_y)

  # determine if line is parallel to x axis
  def is_parallel_x (self):
    tol = 1.0e-18
    return (abs (self.p1.y - self.p2.y) < tol)

  # determine if line is parallel to y axis
  def is_parallel_y (self):
    tol = 1.0e-18
    ...

  # determine slope for the line
  def slope (self):
    if (self.is_parallel_y()):
      return float ('inf')
    else:
      return (self.p1.y - self.p2.y) / (self.p1.x - self.p2.x)

  # determine the y-intercept of the line
  def y_intercept (self):
    return (self.p1.y - (self.slope() * self.p1.x))

  # determine the x-intercept of the line
  def x_intercept (self):
    return (-1.0 * self.y_intercept()) / (self.slope())

  # determine if two lines are parallel
  def is_parallel (self, other):
    tol = 1.0e-18
    return (abs (self.slope() - other.slope()) < tol)


class Triangle(object):

    def _init_(self,p1_x = 0,p1_y = 0,p2_x = 1,p2_y = 1,p3_x = 3,p3_y = 0):

        self.l1 = Line(p1_x,p1_y,p2_x,p2_y)

        self.l2 = Line(p1_x,p1_y,p3_x,p3_y)

        self.l3 = Line(p2_x,p2_y,p3_x,p3_y)


def main():

    Tri = Triangle()

    Tri.l1 = Line(0,0,4,0)

    Tri.l2 = Line(0,0,2,2)

    Tri.l3 = Line(2,2,4,0)

main()
