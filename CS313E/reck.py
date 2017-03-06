def compute(n):

    if n == 0:

        return 0

    else:

        return n + compute(n-1)

def main():

    print(compute(5))

main()
