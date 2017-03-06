def bunnyEars(bunnies):

    count = 2

    if bunnies == 0:

        return 0

    else:

        return bunnyEars(bunnies-1) + count



def bunnyEars2(bunnies):

    if bunnies == 0:

        return 0


    else:

        if bunnies % 2 == 0:

            return bunnyEars2(bunnies-1) + 2

        elif bunnies % 3 == 0:

            return bunnyEars2(bunnies-1) + 3


def main():

    print(bunnyEars(1))


    print(bunnyEars2(3))

main()
