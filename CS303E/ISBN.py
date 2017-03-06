#  File: ISBN.py

#  Description:determines if an input is a valid ISBN number

#  Student Name: Kayne Khoury

#  Student UT EID:kdk745

#  Course Name: CS 303E

#  Unique Number: 52700

#  Date Created:11/2/2014

#  Date Last Modified:11/3/2014


# begin code

import string

# function of first condition for valid isbn - 'X' is not located in first 9 characters

def valid(a):

    for i in a[0:9]:
        if i == 10:

            return False
    return True

# begin main function
    
def main():

    # open file

    infile = open("isbn.txt")

    # create empty list

    a = []

    # read lines


    for line in infile:
        # modify each line for testing

        line = line.strip()

        line2 = line

        line = line.replace('-','')

        line = line.upper()

        line = ' '.join(line)

        line = line.replace('X','10')

        # create list for each line
        
        a = line.split()

        a = [int(x) for x in a]

        # begin valid isbn test

        if valid(a):

            # create variables and lists for partial sums

            sum1 = 0
            b = []
            sum2 = 0
            c = []

            for i in a:

                sum1 +=i

                b.append(sum1)

                sum2 += sum1

                c.append(sum2)

            # test and print results    

            if c[9] % 11 == 0:

                print(line2,'valid')

            else:

                print(line2,'invalid')

        else:

            print(line2, 'invalid')
# end testing
        
    infile.close()

main()
