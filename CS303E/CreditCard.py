#  File: CreditCard.py

#  Description:Determines type of credit card and whether or not the user input number is a valid credit card number

#  Student Name:Kayne Khoury

#  Student UT EID:kdk745

#  Course Name: CS 303E

#  Unique Number: 52700

#  Date Created: 10/20/2014

#  Date Last Modified: 10/20/2014



# prompt user to enter CC number

n = eval(input('Enter 15 or 16 - digit credit card number:'))



# define function for reversing digits

def rev_digits(n):

    rev_num=0

    while(n>0):

        rev_num = rev_num*10+(n%10)

        n=n//10

    return rev_num
 
   
rev_digits(n) # end function



creditcard = rev_digits(n) # variable for creditcard number reversed

cc = str(creditcard) # variable for string of reversed creditcard number



# define function for a valid CC number

def is_valid(cc):

    Sum = 0

    if len(cc) == 16: # for CC lengths of 16

        d1,d3,d5,d7,d9,d11,d13,d15 = int(cc[1]),int(cc[3]),int(cc[5]),int(cc[7]),int(cc[9]),int(cc[11]),int(cc[13]), int(cc[15])

        d0,d2,d4,d6,d8,d10,d12,d14 = int(cc[0]),int(cc[2]),int(cc[4]),int(cc[6]),int(cc[8]),int(cc[10]),int(cc[12]),int(cc[14])

        s1 = d0+d2+d4+d6+d8+d10+d12+d14

        p1,p3,p5,p7,p9,p11,p13,p15 = 2*d1,2*d3,2*d5,2*d7,2*d9,2*d11,2*d13,2*d15

        if len(str(p1))==2:

             st1 = str(p1)

             p1 = int(st1[0]) + int(st1[1])
        if len(str(p3))==2:

             st3 = str(p3)

             p3 = int(st3[0]) + int(st3[1])
        if len(str(p5))==2:

             st5 = str(p5)

             p5 = int(st5[0]) + int(st5[1])
        if len(str(p7))==2:

             st7 = str(p7)

             p7 = int(st7[0]) + int(st7[1])
       
        if len(str(p9))==2:

             st9 = str(p9)

             p9 = int(st9[0]) + int(st9[1])
        if len(str(p11))==2:

             st11 = str(p11)

             p11 = int(st11[0]) + int(st11[1])
        if len(str(p13))==2:

             st13 = str(p13)

             p13 = int(st13[0]) + int(st13[1])

        if len(str(p15))==2:

             st15 = str(p15)

             p15 = int(st15[0]) + int(st15[1])

        s2 = p1+p3+p5+p7+p9+p11+p13+p15

        Sum = s1+s2

    if len(cc) == 15: # for CC lengths of 15

        d1,d3,d5,d7,d9,d11,d13 = int(cc[1]),int(cc[3]),int(cc[5]),int(cc[7]),int(cc[9]),int(cc[11]),int(cc[13])

        d0,d2,d4,d6,d8,d10,d12,d14 = int(cc[0]),int(cc[2]),int(cc[4]),int(cc[6]),int(cc[8]),int(cc[10]),int(cc[12]),int(cc[14])

        s1 = d0+d2+d4+d6+d8+d10+d12+d14

        p1,p3,p5,p7,p9,p11,p13 = 2*d1,2*d3,2*d5,2*d7,2*d9,2*d11,2*d13

        if len(str(p1))==2:

             st1 = str(p1)

             p1 = int(st1[0]) + int(st1[1])
        if len(str(p3))==2:

             st3 = str(p3)

             p3 = int(st3[0]) + int(st3[1])
        if len(str(p5))==2:

             st5 = str(p5)

             p5 = int(st5[0]) + int(st5[1])
        if len(str(p7))==2:

             st7 = str(p7)

             p7 = int(st7[0]) + int(st7[1])
       
        if len(str(p9))==2:

             st9 = str(p9)

             p9 = int(st9[0]) + int(st9[1])
        if len(str(p11))==2:

             st11 = str(p11)

             p11 = int(st11[0]) + int(st11[1])
        if len(str(p13))==2:

             st13 = str(p13)

             p13 = int(st13[0]) + int(st13[1])

        s2 = p1+p3+p5+p7+p9+p11+p13

        Sum = s1+s2


    if Sum % 10 == 0: # Final Result

        return True

    else:

        return False

               

    
is_valid(cc) # end function

# Define function for type of CC input by user

def cc_type(n):

    amex = 'American Express'

    disc = 'Discover'

    mc = 'MasterCard'

    v = 'Visa'

    blank = ''

    sn = str(n) # put user input CC into string format

    # splitting CC string for CC type check

    d0 = int(sn[0])

    d1 = int(sn[1])

    d2 = int(sn[2])

    d3 = int(sn[3])

    if (d0 == 3 and d1 == 1) or (d0 == 3 and d1 == 7):

        return amex

    elif (d0 == 6 and d1 == 0 and d2 == 1 and d3 == 1) or (d0 == 6 and d1 == 4 and d2 == 4) or (d0 == 6 and d1 == 5):

        return disc

    elif (d0 == 5 and d1 == 0) or (d0 == 5 and d1 == 5):

        return mc

    elif (d0 == 4):

        return v

    else:

        return blank
    


cc_type(n) # end function

# main function for output


def main():

  

    if is_valid(cc) and cc_type(n):

        print("Valid", cc_type(n), "credit card number")

    elif len(str(n))<15 or len(str(n))>16:

        print("Not a 15 or 16-digit number")    

    else:

        print("Invalid credit card number")

    
main() # end of code file - yay!! :)
    


    
