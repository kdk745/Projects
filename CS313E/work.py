#  File: Work.py 

#  Description: find minimum V for Vyasa to write n lines of code with factor k

#  Student Name:  Kayne Khoury

#  Student UT EID:  kdk745 # 76

#  Course Name: CS 313E

#  Unique Number: 51730

#  Date Created: 3/27/2015

#  Date Last Modified: 3/28/2015

def progress(n,k,v,p,summ):

    factor = v//k**p

    if factor == 0:

        return summ >= n
    else:
        # continue adding factor to sum and increasing, p, the number of cups of coffee
        return progress(n,k,v,p+1,summ + factor)

def binary_search (n,k):

    a = []

    lo = 0

    hi = n

    summ = 0

    while lo <= hi:

        mid = (lo + hi) // 2

        # test if mid (V), lets Vyasa finish n lines of code before collapsing

        if progress(n,k,mid,0,summ):

            # track applicable mids

            a.append(mid)
        
            hi = mid -1
        else:

            lo = mid + 1

    # print minimum applicable mid

    print(min(a))

def main():
    in_file = open("./work.txt","r")

    # track test cases


    test_cases = in_file.readline()

    test_cases = test_cases.strip()
    test_cases = int(test_cases)

    # create test cases

    for i in range(test_cases):

        test = in_file.readline()

        test = test.strip()

        test = test.split()

        test[0], test[1] = int(test[0]), int(test[1])

        binary_search(test[0],test[1])
        
    in_file.close()


main()
