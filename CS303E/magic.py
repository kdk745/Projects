def is_magic (a):
    # check dimension of 2-D list a
    n = len(a)
    
    # compute canonical sum

    canon_sum = n * (n*n+1)//2

    print(canon_sum)

    # check sum of each row

    for i in range(len(a)):
        
        sum_row = 0
        
        for j in range (len(a[i])): # length of row 1
            
            sum_row += a[i][j]

            print(sum_row)

            # check if sum_row == canon_sum

            #will return False, return True at very end when all tests are done

            if sum_row != canon_sum:
                return False
            else:
                continue
        
    # check sum of each column
    for j in range(len(a[0])):

        sum_col = 0

        for i in range(len(a)):

            sum_col+=a[i][j]

            print(sum_col)

            # check if sum_col == canon_sum
            if sum_col != canon_sum:
                return False
           

    # check sum of diagonal left to right

    sum_lr = 0

    for i in range(len(a)):
        
        sum_lr += a[i][i]
        
        print(sum_lr)
        
        # check sum_lr == canon_sum
        
        if sum_lr != canon_sum:
            return False
       
            
    # check sum of diagnal right to left
    sum_rl = 0
    
    for i in range(len(a)):
        
        sum_rl += a[i][len(a)-1-i]
        print(sum_rl)
        # check sum_rl == canon_sum
        if sum_rl != canon_sum:
            return False
      
    return True


def main():
    # open file for reading
    in_file = open("./squares.txt","r")

    # out file for writing
 #   out_file = open("squares.txt","w")
        
    # read line for number of squares
    num_squares = in_file.readline()

    num_squares = num_squares.strip()

    num_squares = int(num_squares)


    

    # read blank lines for removal
    for i in range(num_squares):
        #read blank lines
        
        blank = in_file.readline()

        # read dimension of square
        dim = in_file.readline()
        dim = dim.strip()
        dim = int(dim)

        # create 2-D list
        a = []

        for j in range(dim):

            row = in_file.readline()
            row = row.strip()
            b = row.split()
            for k in range(len(b)):
                b[k] = int(b[k])
            a.append(b)

            print(a)

        if is_magic(a):
            print("valid")
        if not is_magic(a):
            print("invalid")
        

    in_file.close()
 #   out_file.close()
main()
        


 


   
 
