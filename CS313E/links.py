class Link (object):
  def __init__ (self, row = 0, col = 0, data = 0, next = None):
    self.row = row
    self.col = col
    self.data = data
    self.next = next

  # returns a String representation of a Link (row, col, data)
  def __str__ (self):
    s = ''
    return s
class LinkedList (object):
  def __init__ (self):
    self.first = None

  def insertLast (self, row, col, data):
    newLink = Link (row, col, data)
    current = self.first

    if (current == None):
      self.first = newLink
      return

    while (current.next != None):
      current = current.next

    current.next = newLink

  # returns a String representation of a LinkedList
  def __str__ (self):
    s = ''
    while self.first != None:

        s += str(self.first.data) + " "

        self.first = self.first.next
   
    return s

class Matrix (object):
  def __init__ (self, row = 0, col = 0):
    self.row = row
    self.col = col
    self.matrix = LinkedList()
  
  # finds the Link having row and col value
  def find (self, row, col):

      current = self.matrix.first

      while current != None:

          if current.row == row and current.col == col:

              return (current.data)

          current = current.next

      return None


  # removes the Link having row and col value
  def delete (self, row, col):
      current = self.matrix.first
      previous = self.matrix.first

      if (current == None):

          return None

      while (current.row != row and current.col != col):

          if (current.next == None):

              return None
          else:

              previous = current

              current = current.next

      if (current == self.matrix.first):

          self.matrix.first = self.matrix.first.next

      else:

          previous.next = current.next

      return current
     
    

  # Performs assignment operation:  matrix[row][col] = data
  def set_element (self, row, col, data):

      current = self.matrix.first

      if current == None:

          return None

      while current != None:

          if current.row == row and current.col == col:

              current.data = data

          current = current.next

      return current
    
  # Adds two sparse matrices 
  def __add__ (self, other):

    if (self.row != other.row) or (self.col != other.col):
        return None

    mat = Matrix(self.row,self.col)

    first = self.matrix.first

    second = other.matrix.first

    while first != None and second != None:

      if first.col == second.col and first.row == second.row:

        mat.matrix.insertLast(first.row,first.col,first.data + second.data)

      else:

        mat.matrix.insertLast(first.row,first.col,first.data)

        mat.matrix.insertLast(second.row,second.col,second.data)

      first = first.next

      second = second.next
        
    return mat

  # Multiplies two sparse matrices 
  def __mul__ (self, other):

    if self.col != other.row:

      return None

    mat = Matrix(self.row,other.col)

    first = self.matrix.first

    second = other.matrix.first

    

    
    return

  # Returns a linked list representing a row
  def getRow (self, n):

    current = self.matrix.first

    mat = LinkedList()

    while current != None:

      if current.row == n:

        mat.insertLast(n,current.col,current.data)

      current = current.next

      
    return mat

  # Returns a linked list representing a column
  def getCol (self, n):
    return

  # Returns a string representation of a matrix
  def __str__ (self):
    return 

def readMatrix (inFile):
  line = inFile.readline().rstrip("\n").split()
  row = int (line[0])
  col = int (line[1])
  mat = Matrix (row, col)

  for i in range (row):
    line = inFile.readline().rstrip("\n").split()
    for j in range (col):
      elt = int(line[j])
      if (elt != 0):
        mat.matrix.insertLast (i, j, elt)
  line = inFile.readline()

  return mat

def main ():
  inFile = open ("matrix.txt", "r")

  print ("Test Matrix Addition")
  matA = readMatrix (inFile)

  matB = readMatrix(inFile)

  matC = matA + matB

  matD = readMatrix(inFile)

  matE = matB.getRow(0)

  print(matE)

  

  

  
  inFile.close()

main()
