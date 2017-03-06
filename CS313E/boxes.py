#  File: Boxes.py

#  Description: Determines the largest subsets of boxes that nest within eachother

#  Student Name: Juanito Taveras # 150

#  Student UT EID: jmt3686

#  Partner Name: Kayne Khoury # 76

#  Partner UT EID: kdk745

#  Course Name: CS 313E

#  Unique Number: 51730

#  Date Created: 2/25/2015

#  Date Last Modified: 2/27/2015




# given l w h of a box

# open file boxes.txt and read file

# first line gives number of boxes, n

# second line gives set of three integers separated by one or more spaces.

# these integers are the dimensions of a box, order of dimensions doesn't matter

# sort dimensions in ascending order

# output will return largest subset of boxes that nest inside eachother
# example:
# Largest Subset of Nesting Boxes
#(2,2,3)
#(5,5,6)
#(6,7,9)

# compare dimensions for each subset to see if they nest within eachother

global master_list
master_list = []
global fitting_boxes
fitting_boxes = []

def check_dim(a):     # a is subset of indices of the masterlist
    for i in range(len(a)-1):
        if master_list[a[i]][0] >= master_list[a[i+1]][0]:

            return False

        elif master_list[a[i]][1] >= master_list[a[i+1]][1]:

            return False

        elif master_list[a[i]][2] >= master_list[a[i+1]][2]:

            return False

    return True
           
# get subsets and compare dimensions within subset using check_subset function           
def subsets (a, b, lo):    # a is idx_list, b subset of indices, lo is zero
    hi = len(a)
    if (lo == hi):
        if check_dim(b):  # append applicable nesting subsets
            fitting_boxes.append(b)
    else:   
        c = b[:]
        b.append (a[lo])
        lo += 1  
        subsets (a, c, lo)   
        subsets (a, b, lo)

def main():
    inFile = open("./boxes.txt", "r")      # read file
    b = []
    num_boxes = inFile.readline()          # read number of boxes
    num_boxes = int(num_boxes.strip())     # save as an integer

    for line in inFile:                   # for every line
        line = line.strip()               # remove white space
        line = line.split()               # split into items and make list
        for i in range(3):                # change items to integers
            line[i] = int(line[i])
        line.sort()                       # sort in ascending order
        master_list.append(line)          # add line to our list of boxes
    inFile.close()                        # close file

    master_list.sort()
    idx_list = []
    
    for i in range (num_boxes): # get list for indices of master_list
      idx_list.append(i)

    subsets(idx_list,b,0) # call functions to determine nesting subsets
    nest_lengths = []
    max_size = 0

    print('Largest Subset of Nesting Boxes')

    for i in fitting_boxes: # output the results for largest subset(s)
        nest_lengths.append(len(i))
        nest_lengths.sort()
        max_size = nest_lengths[-1]

    for i in fitting_boxes:
        if len(i) == max_size:
            for j in i:
                print(master_list[j])
            print('')
   
main()

        

    
