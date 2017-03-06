def cube_root(x):

    a = []

    for i in range(0,x+1):

        a.append(i)

    start = 0

    end = len(a)

    last = len(a) -1

    while (start <= end):

        mid = (start + end) // 2

        for num in range(start,end):

            if (a[mid] ** 3) > a[last]:

                end = mid 
                
            elif (a[mid] ** 3) < a[last]:

                start = mid

            else:

                return a[mid]
    return -1
    

def main():

 #   user = eval(input("Enter number to find cubed root"))

    print(cube_root(125))
 



main()
