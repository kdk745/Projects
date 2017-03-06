#  File: GuessingGame.py

#  Description:Will guess a number between 1 and 100 inclusive in seven attempts or less

#  Student Name:Kayne Khoury

#  Student UT EID:kdk745

#  Course Name: CS 303E

#  Unique Number: 52700

#  Date Created:11/17/2014

#  Date Last Modified:11/17/2014



# Begin Code

def main():

    # create list for binary search 

    a = []

    for i in range (1,101):

        a.append(i)

    # begin Guessing Game

    print('Think of a number between 1 and 100 inclusive.')

    print('And I will guess what it is in 7 tries or less.')

    ready = input('Are you ready? (y/n):')

    while ready!='y' or ready!='n':

        ready = input('Are you ready? (y/n):')

        if ready == 'y' or ready == 'n':

            break
    

    if ready == 'n':

        print('Bye')

    elif ready == 'y':

        # start binary search

        lo = 0

        hi = len(a)

        # loop for binary search

        while lo <= hi:

            # loop for guesses

            for i in range(1,8):

                mid = (lo + hi) // 2

                # print guess 

                print('Guess',i,': The number you thought was',mid)

                # user input for determining if guess is correct/incorrect

                user = int(input('Enter 1 if my guess was high, -1 if low, and 0 if correct:'))

                if user == 0:

                    print('Thank you for playing the Guessing Game')

                    break

                # altering hi and lo parameters for next guess


                elif user == 1:

                    hi = mid 

                elif user == -1:

                    lo = mid 

                if (i == 7 and user == -1) or (i == 7 and user == 1):

                    print('Either your guess is a number out of range or you had an incorrect entry')

            # terminate binary search loop

            break
# end code
                    
main()
