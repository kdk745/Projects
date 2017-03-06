# File: Deal.py

# Description: The Monty Hall Problem - Let's Make a Deal - and the probability of switching

# Student Name: Kayne Khoury

# Student UT EID: kdk745

# Course Name: CS 303E

# Unique Number:52700

# Date Created: 10/4/2014

# Date Last Modified: 10/5/2014



import random

def main():


    # enter number of plays

    plays = eval(input("Enter number of times you want to play:"))


    # variable for wins


    win = 0

    lose = 0

    # begin table


    print("Prize Guess View New Guess")

    # model the game being played


    for i in range (plays):

    # define each variable


        prize = random.randit (1,4)


        guess = random.randit(1,4)

        view = 0

        switch = 0

        
        if prize != guess:

            if prize != 1 and guess != 1:

                view = 1

            if prize !=2 and guess !=2:

                view = 2

            if prize !=3 and guess !=3:

                view = 3

        else:

            if prize ==1:

                view = random.randit (2,4)

            if prize ==2:

                view = 1 + 2 * random.randit (0,2)

            if prize ==3:

                view = random.randit (1,3)

    

        for switch in range (1,4):


            if guess == 1 and view == 2:

                switch = 3

            if guess == 1 and view ==3:

                switch = 2

            if guess == 2 and view == 1:

                switch = 3

            if guess ==2 and view ==3:

                switch = 1

            if guess ==3 and view ==1:

                switch = 2

            if guess ==3 and view ==2:

                switch = 1

        if switch == prize:

            win+=1

        else:

            lose+= 1

    # print a table showing random numbers for each play    
        



        print(" ", prize,"   ", guess,"   ", view,"   ", switch)

    prob_win = round(win / plays,1)

    prob_lose = 1-prob_win

    probwin = format(prob_win, "10.2f")

    problose = format(prob_lose, "10.2f")

    # print probabilities for switching and not switching



    print("Probability of winning if you switch =",probwin)

    print("Probability of winning if you do not switch =",problose)
  
main ()


 




    

    
