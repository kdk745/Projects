def flip(array):

    size = 0

    while size < (len(array) -1):

        dummy = []

        dummy2 = []

        biggest = 0

        for i in range(size,len(array)):

            if array[i] > biggest:

                biggest = array[i]

        index = array.index(biggest)

        #track where max is in given range
        dummy += array[index:]

        #separate anything before max
        dummy2 += array[size:index]

        #reverse max to top

        dummy.reverse()

        #add to range

        dummy2 += dummy

        #remove range from array for future adding

        for j in dummy2:

            array.remove(j)

        #reverse range for correct order, max is now on bottom in correct order

        dummy2.reverse()

        #add new ordered range into array

        array += dummy2

        size +=1

    return array

        

        

def main():

    array = [82,75,76,32,33,44,55,99,100,23,1,2]

    flip(array)

    print(array)

main()
            

            

            

        
