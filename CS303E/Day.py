#  File: Day.py

#  Description:Determines day of the week for given month of years in range (1900, 2100)

#  Student Name:Kayne Khoury

#  Student UT EID:kdk745

#  Course Name: CS 303E

#  Unique Number: 52700

#  Date Created:9/27/2014

#  Date Last Modified:9/28/2014




def main():
    year = int(input("Enter year:"))
    while year < 1900 or year > 2100:
        year = int(input("Enter year:"))

    month = int(input("Enter month:"))
    while month < 1 or month > 12:
        month = int(input("Enter month:"))
    if month == 1:
     actualmonth = month + 10
    elif month == 2:
        actualmonth = month + 10
    else:
        actualmonth = (month + 10) % 12
    month = actualmonth

    day = int(input("Enter day:"))
    while day < 1 and day > 31:
        day = int(input("Enter day:"))
    
    while month == 12 and (year % 100 !=0 and year % 4 ==0 or year % 400 == 0) and day > 29:
        day = int(input("Enter day:"))
        
    
        
    
    


    a = month

    b = day

    c = year % 100

    d = year // 100

    w = (13 * a - 1) // 5

    x = c // 4

    y = d // 4

    z = w + x + y + b + c - 2 * d

    r = z % 7

    r = (r + 7) % 7

    if month == 11:
        if (r == 0):
         print ("The day is Friday")
        if (r == 1):
         print ("The day is Saturday")
        if (r == 2):
         print ("The day is Sunday")
        if (r == 3):
         print ("The day is Monday")
        if (r == 4):
         print ("The day is Tuesday")
        if (r == 5):
         print ("The day is Wednesday")
        if (r == 6):
         print ("The day is Thursday")
    elif month == 12:
        if (r == 0):
         print ("The day is Friday")
        if (r == 1):
         print ("The day is Saturday")
        if (r == 2):
         print ("The day is Sunday")
        if (r == 3):
         print ("The day is Monday")
        if (r == 4):
         print ("The day is Tuesday")
        if (r == 5):
         print ("The day is Wednesday")
        if (r == 6):
         print ("The day is Thursday")
        
    else:
        if (r == 0):
         print ("The day is Sunday")
        if (r == 1):
         print ("The day is Monday")
        if (r == 2):
         print ("The day is Tuesday")
        if (r == 3):
         print ("The day is Wednesday")
        if (r == 4):
         print ("The day is Thursday")
        if (r == 5):
         print ("The day is Friday")
        if (r == 6):
         print ("The day is Saturday")
         
 
main()
