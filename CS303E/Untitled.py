import random

def main():

    input1 = int(input("Enter number of rolls you want to play:"))

    print("If you get an even roll, you win a dollar, if you get an odd roll you lose a dollar")

    

    roll_list = []

    even = 0

    odd = 0

    for rolls in range(input1):

        roll_list.append(random.randint(1,6))

    for results in roll_list:

        if results % 2 == 0:

            even += 1

        else:

            odd += 1

    freq_even = even//input1

    freq_odd = odd//input1

    freq_even = round(freq_even,1)

    freq_odd = round(freq_odd,1)

    ev = freq_even *(1) + freq_odd *(-1)

    ev = round(ev,1)

    print("you won",even,"number of times","you lost",odd,"number of times")

    print("you win",ev)


main()

         

    
