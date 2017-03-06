#  File: TestBinaryTree.py

#  Description: test isSimilar(), printLevel(), getHeight(), numNodes(),
#                   and various helper functions

#  Student Name: Kayne Khoury

#  Student UT EID: kdk745 #76

#  Course Name: CS 313E

#  Unique Number: 51730

#  Date Created: 4/19/2015

#  Date Last Modified:4/19/2015
class Queue (object):
  def __init__ (self):
    self.queue = []

  def enqueue (self, item):
    self.queue.append (item)

  def dequeue (self):
    return (self.queue.pop(0))

  def isEmpty (self):
    return (len (self.queue) == 0)

  def size (self):
    return len (self.queue)
class Node (object):
    def __init__ (self, data):
        self.data = data
        self.lChild = None
        self.rChild = None
class Tree (object):
  def __init__ (self):
    self.root = None
    self.size = 0

  # Search for a node with the key
  def search (self, key):
    current = self.root
    while ((current != None) and (current.data != key)):
      if (key < current.data):
        current = current.lChild
      else:
        current = current.rChild
    return current

  # Insert a node in the tree
  def insert (self, val):
    newNode = Node (val)

    if (self.root == None):
      self.root = newNode
    else:
      current = self.root
      parent = self.root
      while (current != None):
        parent = current
        if (val < current.data):
            current = current.lChild
        else:
            current = current.rChild

      if (val < parent.data):
        parent.lChild = newNode
      else:
        parent.rChild = newNode

      self.size +=1

  # In order traversal - left, center, right
  def inOrder (self, aNode):
    if (aNode != None):
      self.inOrder (aNode.lChild)
      print (aNode.data)
      self.inOrder (aNode.rChild)

  # Pre order traversal - center, left, right
  def preOrder (self, aNode):
    if (aNode != None):
      print (aNode.data)
      preOrder (aNode.lChild)
      preOrder (aNode.rChild)

  # Post order traversal - left, right, center
  def postOrder (self, aNode):
    if (aNode != None):
      postOrder (aNode.lChild)
      postOrder (aNode.rChild)
      print (aNode.data)

  # Find the node with the smallest value
  def minimum (self):
    current = self.root
    parent = current
    while (current != None):
      parent = current
      current = current.lChild
    return parent

  # Find the node with the largest value
  def maximum (self):
    current = self.root
    parent = current
    while (current != None):
      parent = current
      current = current.rChild
    return parent

  # Delete a node with a given key
  def delete (self, key):
    deleteNode = self.root
    parent = self.root
    isLeft = False

    # If empty tree
    if (deleteNode == None):
      return False

    # Find the delete node
    while ((deleteNode != None ) and (deleteNode.data != key)):
      parent = deleteNode
      if (key < deleteNode.data):
        deleteNode = deleteNode.lChild
        isLeft = True
      else:
        deleteNode = deleteNode.rChild
        isLeft = False
      
    # If node not found
    if (deleteNode == None):
      return False

    # Delete node is a leaf node
    if ((deleteNode.lChild == None) and (deleteNode.rChild == None)):
      if (deleteNode == self.root):
        self.root = None
      elif (isLeft):
        parent.lChild = None
      else:
        parent.rChild = None

    # Delete node is a node with only left child
    elif (deleteNode.rChild == None):
      if (deleteNode == self.root):
        self.root = deleteNode.lChild
      elif (isLeft):
        parent.lChild = deleteNode.lChild
      else:
        parent.rChild = deleteNode.lChild

    # Delete node is a node with only right child
    elif (deleteNode.lChild == None):
      if (deleteNode == self.root):
        self.root = deleteNode.rChild
      elif (isLeft):
        parent.lChild = deleteNode.rChild
      else:
        parent.rChild = deleteNode.rChild

    # Delete node is a node with both left and right child
    else:
      # Find delete node's successor and successor's parent nodes
      successor = deleteNode.rChild
      successorParent = deleteNode

      while (successor.lChild != None):
        successorParent = successor
        successor = successor.lChild

      # Successor node right child of delete node
      if (deleteNode == self.root):
        self.root = successor
      elif (isLeft):
        parent.lChild = successor
      else:
        parent.rChild = successor

      # Connect delete node's left child to be successor's left child
      successor.lChild = deleteNode.lChild

      # Successor node left descendant of delete node
      if (successor != deleteNode.rChild):
        successorParent.lChild = successor.rChild
        successor.rChild = deleteNode.rChild

    return True
  # Returns true if two binary trees are similar
  def track (self, aNode,lyst):
    if (aNode != None):
      self.track (aNode.lChild,lyst)
      lyst.append(aNode.data) # interpret trees in list form
      self.track (aNode.rChild,lyst)
  def isSimilar (self, pNode):
      t1 = []
      t2  = []
      self.track(self.root,t1) # go through both trees and check if they are the same
      pNode.track(pNode.root,t2)
      return (t1 == t2) # compare order and values of trees 

  def Level (self,current,level,lyst):
      if self.root == None:
          return
      elif level == 1:
          lyst.append(current.data)
      else:
          if current.lChild != None: # account for no lchild
              self.Level(current.lChild,level-1,lyst)
          if current.rChild != None: # account for no rchild
              self.Level(current.rChild,level-1,lyst)
   # Prints out all nodes at the given level
  def printLevel(self,level):
      lyst = []
      self.Level(self.root,level,lyst) # call the helper function to recursively find nodes at level
      st = ''
      for i in lyst:
          st += str(i) + ' '
      print(st)        
  # Returns the height of the tree
  def getHeight (self):
      root = self.root
      if root == None:
          return -1
      else:
          return 1 + max(self.getHeight(),self.getHeight())    
  # subtree count
  def count_tree(self,root):
      if self.root is None:
          return 0
      else:
          if root.lChild == None and root.rChild == None:
              return 1
          else:
              if root.lChild == None: # account for no lchild
                  return 1 + self.count_tree(root.rChild)
              elif root.rChild == None: # account for no rchild
                  return 1 + self.count_tree(root.lChild)
              elif root.rChild != None and root.lChild != None:
                  return 1 + self.count_tree(root.lChild) + self.count_tree(root.rChild)    

  # Returns the number of nodes in the left subtree and
  # the number of nodes in the right subtree
  def numNodes (self,root):
      left = self.count_tree(root.lChild) # call the helper function to recursively find num nodes
      right = self.count_tree(root.rChild)
      return str(left) + '\n' + str(right) # print the left subtree total then the right

def main():
    # Create three trees - two are the same and the third is different
    tree_1 = Tree()
    tree_2 = Tree()
    tree_3 = Tree()
    t12 = [23,43,12,54,24,65,13,67,11,54,32]#<----the list made made into two trees
    for i in t12:
        tree_1.insert(i)
        tree_2.insert(i)
    t3 = [21,12,16,34,23,20,35] #<-----the different tree
    for j in t3:
        tree_3.insert(j)
        
    # Test your method isSimilar()
    print(tree_1.isSimilar(tree_3))
    
    # Print the various levels of two of the trees that are different
    tree_1.printLevel(2)
    tree_1.printLevel(1)
    tree_3.printLevel(3)
    tree_3.printLevel(1)
    
    # Get the height of the two trees that are different
    height_1 = tree_1.getHeight()
    print(height_1) 
    height_2 = tree_3.getHeight()
    print(height_2)

    # Get the number of nodes in the left and right subtree
    nodes = tree_2.numNodes(tree_2.root)
    print(nodes) # left then right subtree totals printed
    node = tree_3.numNodes(tree_3.root)
    print(node)
    lst = 50, 30, 70, 10, 40, 60, 80, 7, 25, 38, 47, 58, 65, 77, 96
    T1 = Tree()

    for i in lst:
      T1.insert(i)

  
    T2 = Tree()
    print(T1.isSimilar(T2)) # check and print the boolean of T1 == T2
    T1.printLevel(3) # print out level 3 of T1
    print(T1.getHeight()) # print the height of T1
    l, r = T1.numNodes()
    print(l) # print number of nodes in left subtree
    print(r) # print number of nodes in right subtree

    

main()
