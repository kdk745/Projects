#  File: DNA.py

#  Description:find longest substring(s) in two given dna strands

#  Student Name: Kayne Khoury

#  Student UT EID:kdk745

#  Course Name: CS 303E

#  Unique Number: 52700

#  Date Created:10/27/2014

#  Date Last Modified:10/29/2014
import string
# define function for determining longest substring(s) present in dna1 and dna2
def substr(dna1,dna2):
    wnd2 = len(dna2)
    printed = False
    comm = 'no common sequence found'
    while wnd2 >0:
        for start_idx in range(0,len(dna2)-wnd2+1):
            slice = dna2[start_idx:start_idx + wnd2]
            if dna1.find(slice) != -1:
                print(slice)
                printed = True
        if printed:
            return                      
        wnd2-=1
    print("No Common Sequence Found")
# begin main     
def main():
  # open file for reading
  in_file = open ("./dna.txt", "r")
  # read number of pairs
  num_pairs = in_file.readline()
  num_pairs = num_pairs.strip()
  num_pairs = int (num_pairs)
  # read pairs of dna strands
  for i in range (num_pairs):
    st1 = in_file.readline()
    st2 = in_file.readline()
    st1 = st1.strip()
    st2 = st2.strip()
    # order strands by size
    if (len(st1) > len (st2)):
      dna1 = st1.upper()
      dna2 = st2.upper()
    else:
      dna1 = st2.upper()
      dna2 = st1.upper()
    # print the results
    print('Pair',i+1,':')
    substr(dna1,dna2)
  # close file
  in_file.close()
main()

     
   


               
  
            




