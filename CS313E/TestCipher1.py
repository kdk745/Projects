#  File: TestCipher.py

#  Description:Cryptography

#  Student Name: Juanito Taveras

#  Student UT EID: jmt3686

#  Student ID Number: 150

#  Partner Name: Kayne Khoury

#  Student ID Number: 76

#  Partner UT EID: kdk745

#  Course Name: CS 313E

#  Unique Number: 51730

#  Date Created: 2/4/2015

#  Date Last Modified: 2/4/2015



def substitution_encode ( strng ):     # strng is string to be encoded from file

    plain = 'abcdefghijklmnopqrstuvwxyz'   

    cipher = ['q','a','z','w','s','x','e','d','c','r','f','v','t','g',\
              'b','y','h','n','u','j','m','i','k','o','l','p']
    output = ''       # empty string for output

    for i in strng:    # for every character in strng

        if i in plain:   # if character is lowercase letter

            idx = ord(i) - 97   # ord('a') = 97

            output += cipher[idx]

        else:

            output += i
    return output    # returns output as string

def substitution_decode ( strng ):

    cipher = ['q','a','z','w','s','x','e','d','c','r','f','v','t','g',\
              'b','y','h','n','u','j','m','i','k','o','l','p']

    plain = 'abcdefghijklmnopqrstuvwxyz'

    output = '' # empty string for output

    for i in strng: # check characters in strng

        if i in plain: # check if character is lowercase letter

            for j in range(len(cipher)):

                if cipher[j] == i:

                    idx = j + 97 # ord('a') = 97

                    output += chr(idx)
        else:
            output += i # returns output as string
    return output

def vigenere_encode ( strng, passwd ):
    output = ''
    plain = 'abcdefghijklmnopqrstuvwxyz' 
    pass_idx = 0
    while pass_idx < len(passwd):   # while 0 is less than 4
        strng_counter = 0
        for i in strng: 
            if i in plain:    # checks if lowercase letter
                idx_num = ord(passwd[pass_idx]) + ord(i) - 97   # ord('a') = 97
                if idx_num > 122:
                    output += chr(idx_num - 26)
                else:
                    output += chr(idx_num)
                if pass_idx == (len(passwd) - 1):
                    pass_idx = 0
                else:
                    pass_idx += 1
            else:
                output += i    # adds it as a space

            strng_counter += 1
        if strng_counter == len(strng):
            return output

def vigenere_decode ( strng, passwd ):
    output = ''
    plain = 'abcdefghijklmnopqrstuvwxyz' 
    pass_idx = 0
    while pass_idx < len(passwd):   # while 0 is less than 4
        strng_counter = 0
        for i in strng: 
            if i in plain:    # checks if lowercase letter
                idx_num = ord(i) + 97 - ord(passwd[pass_idx])   # ord('a') = 97
                if idx_num > 122:
                    output += chr(idx_num - 26)

                elif idx_num < 97:

                    output += chr(idx_num + 26)
                else:
                    output += chr(idx_num)
                if pass_idx == (len(passwd) - 1):
                    pass_idx = 0
                else:
                    pass_idx += 1
            else:
                output += i    # adds it as a space

            strng_counter += 1
        if strng_counter == len(strng):
            return output
def main():
  # open file for reading
  in_file = open ("./cipher.txt", "r")

  # print header for substitution cipher
  print ("Substitution Cipher")
  print ()

  # read line to be encoded
  line = in_file.readline()
  line = line.strip()

  # encode using substitution cipher
  encoded_str = substitution_encode (line)

  # print result
  print ("Plain Text to be Encoded: " + line)
  print ("Encoded Text: " + encoded_str)
  print ()

  # read line to be decoded
  line = in_file.readline()
  line = line.strip()

  # decode using substitution cipher
  decoded_str = substitution_decode (line)

  # print result
  print ("Encoded Text to be Decoded: " + line)
  print ("Decoded Plain Text: " + decoded_str)
  print ()

  # print header for vigenere cipher
  print ("Vigenere Cipher")
  print ()

  # read line to be encoded and pass phrase
  line = in_file.readline()
  line = line.strip()
  passwd = in_file.readline()
  passwd = passwd.strip()

  # encode using vigenere cipher
  encoded_str = vigenere_encode (line, passwd)

  # print result
  print ("Plain Text to be Encoded: " + line)
  print ("Pass Phrase (no spaces allowed): " + passwd)
  print ("Encoded Text: " + encoded_str)
  print ()

  # read line to be decoded and pass phrase
  line = in_file.readline()
  line = line.strip()
  passwd = in_file.readline()
  passwd = passwd.strip()

  # decode using vigenere cipher
  decoded_str = vigenere_decode (line, passwd)

  # print result
  print ("Encoded Text to be Decoded: " + line)
  print ("Pass Phrase (no spaces allowed): " + passwd)
  print ("Decoded Plain Text: " + decoded_str)
  print ()

  # close file
  in_file.close()

main()
