class Link (object):
  def __init__(self,data, next = None):
      self.data = data
      self.next = next

def insertion_sort1 (a):
  for i in range (1, len(a)):
    j = i
    while ((j > 0) and (a[j] < a[j - 1])):
      a[j], a[j - 1] = a[j - 1], a[j]
      j += -1
    
class LinkedList (object):
  # get number of links
  def __init__(self):
      self.first = None
  def getNumLinks (self):
      count = 0
      while self.first != None:
          count +=1
          self.first = self.first.next
      return count
  # Add data at the beginning of the list
  def addFirst (self, data):
      newLink = Link(data)
      newLink.next = self.first
      self.first = newLink
  # Add data at the end of a list
  def addLast (self, data):
      newLink = Link(data)
      current = self.first
      if (current == None):
          self.first = newLink
          return
      while (current.next != None):
          current = current.next
      current.next = newLink
  # Add data in an ordered list in ascending order
  def addInOrder (self, data):
      current = self.first
      newLink = Link(data)
      while current != None:
          if current.data < data and current.next.data > data:
              newLink.next = current.next
              current.next = newLink
          current = current.next
  # Search in an unordered list, return None if not found
  def findUnordered (self, data):
      current = self.first
      tol = 1.0e-20
      while current != None:
          if current.data - data < tol:
              return current
          current = current.next
      return 
  # Search in an ordered list, return None if not found
  def findOrdered (self, data):
     current = self.first
     while current != None:
         if current.next.data > data:
             return current
         current = current.next
     return 
  # Delete and return Link from an unordered list or None if not found
  def delete (self, data):
      current = self.first
      previous = self.first
      if current == None:
          return None
      while (current.data != data):
          if (current.next == None):
              return None
          else:
              previous = current
              current = current.next
      if current == self.first:
          self.first = self.first.next
      else:
          previous.next = current.next
      return current
  # String representation of data 10 items to a line, 2 spaces between data
  def __str__ (self):
      current = self.first
      s = ""
      count = 0
      while current != None:
          if count < 10:
              s += str(current.data) + "  "
              current = current.next
              count += 1
          if count == 10:
              s += "\n"
              count = 0
      return s
  # Copy the contents of a list and return new list
  def copyList (self):
     newList = LinkedList()
     current = self.first
     while current != None:
         newList.addLast(current.data)
         current = current.next
     return newList
  # Reverse the contents of a list and return new list
  def reverseList (self):
     newList = LinkedList()
     current = self.first
     while current != None:
         newList.addFirst(current.data)
         current = current.next
     return newList
  # Sort the contents of a list in ascending order and return new list
  def sortList (self):
      current = self.first
      lyst = []
      while current != None:
          lyst.append(current.data)
          current = current.next
      for i in range (1, len(lyst)):
          j = i
          while ((j > 0) and (lyst[j] < lyst[j - 1])):
              lyst[j], lyst[j - 1] = lyst[j - 1], lyst[j]
              j += -1
      newList = LinkedList()
      for i in range(len(lyst)):
          newList.addLast(lyst[i])
      return newList
  # Return True if a list is sorted in ascending order or False otherwise
  def isSorted (self):
      current = self.first
      while current.next != None:
          if current.next.data < current.data:
              return False
          current = current.next
      return True
  # Return True if a list is empty or False otherwise
  def isEmpty (self):
     current = self.first
     while current != None:
         return False
         current = current.next
     return True

  # Merge two sorted lists and return new list in ascending order
 # def mergeList (self, b): 

  # Test if two lists are equal, item by item and return True
 # def isEqual (self, b):

  # Return a new list, keeping only the first occurence of an element
  # and removing all duplicates. Do not change the order of the elements.
  def removeDuplicates (self):
     current = self.first
     tol = 1.0e-20
     while current != None:
         if current.next.data - current.data < tol:
             current.next = current.next.next
         current = current.next
def main():

  #addFirst() __str__()
  print("\nTest methods addFirst() and __str__() by adding more than \n10 items to a list and printing it.\n")
  print("---------")
  Links = LinkedList()

  for i in range(1,11):

      Links.addFirst(i)

  print(Links)
  #addLast()
  print("\nTest method addLast()\n")
  print("----------")

  Links.addLast(0)

  print(Links,"<----- adds 0 to end of list")

  #addInOrder()

  print("\nTest method addInOrder()\n")
  print("----------")

  Links2 = LinkedList()

  for i in range(1,11):

      Links2.addLast(i)

  Links2.addLast(12)

  print(Links2)

  Links2.addInOrder(11)

  print(Links2,"<----- after adding 11 to list")

  #getNumLinks()

  print("\nTest method getNumLinks()\n")
  print("----------")

  print(Links2)

  num_links = Links2.getNumLinks()

  print(num_links,"<----- Number of links for above list")
  #find Unordered()
  print("\nTest method findUnordered()\n")
  print("----------")

  Links3 = LinkedList()

  Links3.addLast(3)

  Links3.addLast(1)

  Links3.addLast(5)

  Links3.addLast(2)

  print(Links3)

  print(Links3.findUnordered(2),"<----- Location of 2")

  print(Links3.findUnordered(3),"<----- Location of 3")
  
 # print("\nConsider two cases - item is there, item is not there\n")
  print("----------")
  #findOrdered()
  print("\nTest method findOrdered()\n")
  print("----------")

  Links4 = LinkedList()

  for i in range(10,21):

      Links4.addLast(i)

  print(Links4)

  eleven = Links4.findOrdered(11)

  twelve = Links4.findOrdered(12)

  print(eleven,"<----- Location of 11 in above list")

  print(twelve,"<----- Location of 12 in above list")

  #Consider two cases - item is there, item is not there

  print("\nTest method delete()\n")

  print("----------")

  print(Links4)

  Links4.delete(10)

  print(Links4,"^----- 10 has been removed from above list")
  
  #print("\nConsider two cases - item is there, item is not there\n")
  print("----------")
  #copyList()
  print("\nTest method copyList()\n")
  print("----------")

  print(Links4)

  Links5 = Links4.copyList()

  print("A copy of above list")

  print(Links5)
  #reverseList()
  print("\nTest method reverseList()\n")
  print("----------")

  print(Links5)

  Links6 = Links5.reverseList()

  print("A reversed version of above list")

  print(Links6)
  #sortList()
  print("\nTest method sortList()\n")
  print("----------")

  print(Links3)

  lyst = Links3.sortList()

  print(lyst)
  #isSorted()
  print("\nTest method isSorted()\n")
  print("----------")

  #Consider two cases - list is sorted, list is not sorted

  print(Links4)

  if Links4.isSorted():
      
      print('above list is sorted')
      
  print(Links3)
  
  if not Links3.isSorted():

      print('above list is not sorted')
  #isEmpty() <------------------This is where I left off for you 
  print("\nTest method isEmpty()\n")
  print("----------")




 
  #print("\nTest method mergeList()\n")
  print("----------")

  #print("\nTest method isEqual()\n")
  print("----------")
  
  #print("\nConsider two cases - lists are equal, lists are not equal\n")
  print("----------")

  #print("\nTest removeDuplicates()\n")
  print("----------")

main()
