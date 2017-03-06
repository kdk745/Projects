#  File: Books.py

#  Description:Determine if Charles Dickens or Thomas Hardy has the more extended vocabulary.

#  Student Name:Kayne Khoury

#  Student UT EID:kdk745

#  Course Name: CS 303E

#  Unique Number: 52700

#  Date Created:11/30/2014

#  Date Last Modified:12/1/2014


# Create word dictionary from the comprehensive word list 

def create_word_dict ():

    

    words = open("./words.txt","r")

    word_dict = {}

    

    for line in words:

        line = line.strip()

        word_dict[line] = 1

    return word_dict

def parse_string(st):

    s = ''

    for ch in st:

        if (ch.isalpha()) or (ch.isspace()) or (ch == "'"):

            s+=ch
        else:

            s+=' '

    return s


        
# Returns a dictionary of words and their frequencies

#def getWordFreq (file):
  
# Compares the distinct words in two dictionaries
#def wordComparison (author1, freq1, author2, freq2):


def main():
  # Create word dictionary from comprehensive word list
  word_dict = create_word_dict()

  Tale = open("./Tale.txt","r")

  Return = open("./Return.txt","r")

  dict_tale = {}

  dict_return = {}

  list_tale = []

  list_1 = []


  list_return = []

  list_2 = []

  blank_tale = " "

  blank_return = " "

  for line in Tale:

      line = line.strip()

      line = parse_string(line)

      line = line.split()

      for word in line:

          list_tale.append(word)

  for words in list_tale:

      if words[-1] == "s" and words[-2] == "'":

          blank_tale += " "

      else:

          blank_tale += words + " "

  for line in Return:

      line = line.strip()

      line = parse_string(line)

      line = line.split()

      for word in line:

          list_return.append(word)

  for words in list_return:

      if word[-1] == "s" and words[-2] == "'":

          blank_return += " "

      else:

          blank_return += words + " "

  print(blank_return)

          

          

  

  


  

  

      
     

      

      

          
  

        

              

          
  

                    

 

      

  

          
  

  


      

  
  




            

      


  

  
      

          

  


  

  

  

  




  # Enter names of the two books in electronic form
 # book1 = input ("Enter name of first book: ")
 # book2 = input ("Enter name of second book: ")
  #print()

  # Enter names of the two authors
#  author1 = input ("Enter last name of first author: ")
#  author2 = input ("Enter last name of second author: ")
 # print() 
  
  # Get the frequency of words used by the two authors
#  wordFreq1 = getWordFreq (book1)
#  wordFreq2 = getWordFreq (book2)

  # Compare the relative frequency of uncommon words used
  # by the two authors
#  wordComparison (author1, wordFreq1, author2, wordFreq2)

main()
