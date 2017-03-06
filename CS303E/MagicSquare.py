#  File: MagicSquare.py

#  Description: determines if sequence of numbers is a magic square

#  Student Name: Kayne Khoury

#  Student UT EID: kdk745

#  Course Name: CS 303E

#  Unique Number: 52700

#  Date Created:11/12/14

#  Date Last Modified:11/13/14



def isMagic (a):
  # check dimension of 2-D list
  n = len(a)

  # calculate the canonical sum
  canon_sum = n * (n * n + 1) // 2

  # check sum of each row
  for i in range (len(a)):
    sum_row = 0
    for j in range (len (a[i])):
      sum_row += a[i][j]
    # check that the sum_row is equal to the canonical sum
    if sum_row != canon_sum:
        return False

  # check sum of each column
  for j in range (len(a[0])):
    sum_col = 0
    for i in range (len(a)):
      sum_col += a[i][j]
    # check that the sum_col is equal to the canonical sum
    if sum_row != canon_sum:
        return False

  # check sum of diagonal left to right
  sum_lr = 0
  for i in range (len(a)):
    sum_lr += a[i][i]
  # check that the sum_lr is equal to the canonical sum
  if sum_lr != canon_sum:
      return False

  # check sum of diagonal right to left
  sum_rl = 0
  for i in range (len(a)):
    sum_rl += a[i][len(a) - 1 - i]
  # check that the sum_rl is equal to the canonical sum
  if sum_rl != canon_sum:
      return False

  return True

def main():
  # open file for reading
  in_file = open ("squares.txt", "r")

  # open file for writing
  out_file = open ("results.txt", "w")

  # read number of squares
  num_squares = in_file.readline()
  num_squares = num_squares.strip()
  num_squares = int (num_squares)

  # process each square separately
  for i in range (num_squares):
    # read blank line
    blank = in_file.readline()

    # read the dimension of the square 
    dim = in_file.readline()
    dim = dim.strip()
    dim = int(dim)

    # create 2-D list
    a = []
    trial = []
    for j in range (dim):
      row = in_file.readline()
      row = row.strip()
      trial.append(row)
      b = row.split()
      for k in range (len(b)):
        b[k] = int (b[k])
      a.append (b)
    print(num_squares)
    if isMagic(a):
        print(str(dim) +' '+ "valid")
        for row in trial:
            print(row)
    else:
        print(str(dim) +' '+ "invalid")
        for row in trial:
            print(row)
      

    # check if the 2-D list a is  magic and write out result

    

  # close the files
  in_file.close()
  out_file.close()

main()
