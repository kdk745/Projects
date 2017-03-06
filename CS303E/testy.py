def main():

    
        dna2 = 'abcde'


        wnd = len(dna2)

        while(wnd>0):

         for start_idx in range(0,len(dna2)-wnd+ 1):

             slice1 = dna2[start_idx:start_idx+wnd]

             print(slice1)

         wnd -= 1


main()

