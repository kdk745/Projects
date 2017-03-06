def same(list1,list2):

    sum_list = []

    sum1 = 0

    for row in range (len(list1)):

        sum_list.append([])

        for column in range(len(list1[row])):

            sum1 = list1[row][column] + list2[row][column]

            sum_list[row].append(sum1)

    return sum_list



        
def main():

    matrix1 = [[2,3,4,5,6,7]]

    matrix2 = [[1,2,3,4,5,6]]

    answer = same(matrix1,matrix2)

    print(answer)
            


main()

    
