def reverse_row(list1):

    rev_list = []

    for row in reversed(list1):


        rev_list.append(row)

    return rev_list

def main():

    list1 = [[2,3,4,5],[3,5,6,7]]

    answer = reverse_row(list1)


    print(answer)

main()

            
