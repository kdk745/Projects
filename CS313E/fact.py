def fact (n):

    if (n==0):

        return 1

    else:

        return n * fact(n-1)


def fib(n):

    if (n == 1) or (n == 2):

        return 1

    else:

        return fib (n-1) + fib(n-2)
    


def main():


    print(fib(21))
    

    

main()
