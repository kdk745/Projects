import random

def main():

    matrix = []


    for row in range(3):

        matrix.append([])

        for column in range(5):

            matrix[row].append(random.randint(0,100))

    print(matrix)

        
main()
