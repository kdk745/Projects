class Stack (object):
  def __init__ (self):
    self.stack = []

 # add an item to the top of the stack
  def push (self, item):
    self.stack.append ( item )

 # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()

 # check what item is on top of the stack without removing it
  def peek (self):
    return self.stack[len(self.stack) - 1]

 # check if a stack is empty
  def isEmpty (self):
    return (len(self.stack) == 0)

 # return the number of elements in the stack
  def size (self):
    return (len(self.stack))

def operate (oper1, oper2, token):
  if (token == '+'):
    return oper1 + oper2
  elif (token == '-'):
    return oper1 - oper2
  elif (token == '*'):
    return oper1 * oper2
  else:
    return oper1 / oper2


def rpn (s):
  stack = Stack()

  operators = ['+', '-', '*', '/']

  tokens = s.split()

  for item in tokens:
    if (item in operators):
      oper2 = stack.pop()
      print('oper2',oper2)
      oper1 = stack.pop()
      print('oper1',oper1)
      stack.push (operate (oper1, oper2, item))
      print(item)
    else:
      stack.push (float(item))

  return stack.pop()

def main():
  in_file = open ("rpn.txt", "r")
  for line in in_file:
    line = line.strip()
    value = rpn (line)
    print (line, ' = ', value)

  in_file.close()

main()
