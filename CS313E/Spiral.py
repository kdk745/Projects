#  File: Spiral.py

#  Description:Infinite Spiral of Numbers

#  Student Name: Juanito Taveras

#  Student UT EID: jmt3686

#  Partner Name:Kayne Khoury

#  Partner UT EID: kdk745

#  Course Name: CS 313E

#  Unique Number: 51730

#  Date Created: 1/26/2015

#  Date Last Modified:1/31/2015

def makeperimeter(dim):
  spiral = []
  # makes first row and copies it to all rows
  for i in range (dim):    # 0 - 4
    lyst = []
    for j in range ((dim**2) - (dim-1), (dim**2 + 1)):
      lyst.append(j)
    spiral.append(lyst)

  # makes first column
  for k in range (len(spiral)):
    l = spiral[0][0] - k
    spiral[k][0] = l

  # makes bottom row
  for m in range (len(spiral)):  # 0 - 5
    n = spiral[-1][0] - m
    spiral[-1][m] = n

  # makes last column    
  for o in range (1, len(spiral)):  
    p = spiral[-1][-1] - o + 1      
    spiral[-o][-1] = p

  return (spiral)


def innerloop(spiral, dim):   # spiral is 2D list
  num = 0
  while num < ((dim-1)//2):
    # makes inner first row
    for i in range (1, len(spiral) - num * 2):
      j = spiral[1 + num][-1 - num] - i + 1
      spiral[1 + num][-i - num] = j
    # makes inner first column
    for k in range (1, len(spiral) - 1 - num*2):
      l = spiral[1 + num][-len(spiral) + 1 + num] - k + 1
      spiral[k + num][-len(spiral) + 1 + num] = l
    # makes inner bottom row
    for m in range (len(spiral) - 2 - num*2):
      n = spiral[-2 - num][1 + num] - m
      spiral[-2 - num][m+1 + num] = n

    # makes last column
    for o in range (1, len(spiral)-2 - num*2):
      p = spiral[-2 - num][-2 - num] - o + 1
      spiral[-o -1 - num][-2 - num] = p

    num += 1




def main():

  inFile = open ("./spiral.txt", "r") # open spiral file
  num_1 = inFile.readline()           # reads first number in file
  num_1 = num_1.strip()               # removes white space
  num_1 = int(num_1)                  # converts to integer
  if num_1 % 2 == 0:                  # if this number is even
    num_1 += 1                        # add one to it
  num_2 = inFile.readline()           # reads second number in file
  num_2 = num_2.strip()               # removes white space
  num_2 = int(num_2)                  # converts to integer
  if num_2 < 1 or num_2 > (num_1 ** 2):
    print ("Number not in Range")
  inFile.close()
  dim = num_1


  spiral = makeperimeter(dim)
  spiral2 = innerloop (spiral, dim)

  # print mini number grid around chosen number
  row_count = 0
  for row in spiral:  # row then column
    col_count = 0
    for col in row:
      if num_2 == col:
        r, c = row_count, col_count  # index of num_2
        if r == (len(spiral)-1) or r == 0 or c == (len(spiral)-1) or c == 0:
          print ("Number on Outer Edge", "r=", r, "c=", c)
        else:
          print (str(spiral[r-1][c-1]) + " " + str(spiral[r-1][c]) + " " + str(spiral[r-1][c+1]))
          print (str(spiral[r][c-1]) + " " + str(spiral[r][c]) + " " + str(spiral[r][c+1]))
          print (str(spiral[r+1][c-1]) + " " + str(spiral[r+1][c]) + " " + str(spiral[r+1][c+1]))
      col_count += 1
    row_count += 1


  # center number
  spiral[(dim-1)//2][(dim-1)//2] = 1

  for row in spiral:
    print (str(row))
  



main()
