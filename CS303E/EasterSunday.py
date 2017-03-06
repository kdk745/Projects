# File: EasterSunday.py

# Description:Finding the date of Easter in a given year

# Student Name: Kayne Khoury

# Student UT EID: kdk745

# Course Name: CS 303E

# Unique Number: 52700

# Date Created: 9/21/2014

# Date Last Modified: 9/22/2014

def main():    
 x = eval(input("Enter the year"))
 A = x % 19
 B = x // 100
 C = x % 100
 D = B // 4
 E = B % 4
 G = ((8 * B) + 13) // 25
 H = ((19 * A) + B - D - G + 15) % 30
 M = (A + (11 * H)) // 319
 J = C // 4
 K = C % 4
 L = ((2 * E) + (2 * J) - K - H + M + 32) % 7
 N = (H - M + L + 90) // 25
 P = (H - M + L + N + 19) % 32
 Month = N
 if N == 3:
    print ("In", x , "Easter Sunday is on", P , "March")
 else:
     print ("In", x, "Easter Sunday is on", P , "April")
main()    
 




 
