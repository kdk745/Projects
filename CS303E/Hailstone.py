#  File: Hailstone.py

#  Description: Determines longest Hailstone Sequence

#  Student Name: Kayne Khoury

#  Student UT EID: kdk745

#  Course Name: CS 303E

#  Unique Number: 52700

#  Date Created: 10 - 8 - 14

#  Date Last Modified: 10 - 10 - 14


def main():


# prompt user to enter range for Hailstone Sequence


    num_1 = eval(input("Enter the starting number of the range:"))

    num_2 = eval(input("Enter the ending number of the range:"))

# error checking for user input range

    while num_1 <= 0:

        num_1 = eval(input("Enter the starting number of the range:"))

    while num_2 <= 0 or num_2 <= num_1:

        num_2 = eval(input("Enter the ending number of the range:"))

    max_length = 0

# Loops for Hailstone Sequence Calculations for user defined range

    for n in range(num_1, num_2+1):

        length = 0 # variable for each sequence length

        num = [n] # variable for each sequence of range for n


        while n != 1:

            num.append(n) # listing each sequence of n
            
            if n % 2 == 0:

                n = n// 2 # for even numbers

            else:

                 n = 3 * n + 1 # for odd numbers

            length += 1


            if n == 1: # steps terminate

                 if length > max_length:

                     max_length = length #longest sequence length

                     maxx = num[0:1] #number with longest Hailstone Sequence
# print the results
            
    print("The number", maxx," has the longest cycle length of", max_length)

               

main()
