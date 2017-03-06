def cube_root(x):

    lo = 0

    hi = x

    tol = 1.0e-20

    while (lo <= hi):

        mid = (hi + lo) / 2

        cube = mid **3

        if abs(x - cube) < tol:

            print(mid)

            break

        
        elif cube > x:

            hi = mid

        else:

            lo = mid



def main():

    cube_root(125)

main()
