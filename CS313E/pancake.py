def sorted(array):

    count = 0
    length = len(array)-1
    while count < length:
        biggest = 0
        dummy = []
        dummy2 = []
        for i in range(count,length):
            if array[i] > biggest:
                biggest = array[i]
        index = array.index(biggest)
        dummy += array[index:]
        dummy2 += array[count:index]
        dummy.reverse()
        dummy2 += dummy
        dummy2.reverse()
        if len(dummy2) == 2:
            if dummy2[1] > dummy2[0]:
                dummy2.reverse()
        for j in dummy2:
            array.remove(j)
        array += dummy2
        count += 1

    return array

def main():


    array = [23,34,56,78,42,55,21,10,19]

    sorted(array)

    print(array)

  

main()
