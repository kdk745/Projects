#  File: BST_Cipher.py

#  Description: Program that encypts and decrypts strings using a binary search tree.

#  Student Name: Juanito Taveras

#  Student UT EID: jmt3686

#  Partner Name: Kayne Khoury

#  Partner UT EID: kdk745 #76

#  Course Name: CS 313E

#  Unique Number: 51730

#  Date Created: 4/21/2015

#  Date Last Modified: 4/23/2015

class Node (object):
	def __init__ (self, data):
		self.data = data
		self.lChild = None
		self.rChild = None


class Tree (object):
  # the init() function creates the binary search tree with the
  # encryption string. If the encryption string contains any
  # character other than the characters 'a' through 'z' or the
  # space character drop that character.
	def __init__ (self, encrypt_str):
		self.root = None
	#	self.insert('*')
		already_inserted = ''
		for ch in encrypt_str:
			if ((97 <= ord(ch) <= 122) or (ord(ch) == 32)) and ch not in already_inserted:
				self.insert(ch)
				already_inserted += ch




		

  # the insert() function adds a node containing a character in
  # the binary search tree. If the character already exists, it
  # does not add that character. There are no duplicate characters
  # in the binary search tree.
	def insert (self, ch):
		newNode = Node (ch)
		if self.root == None:
			self.root = newNode
		else:
			current = self.root
			parent = self.root
			while current != None:
				parent = current
				if ord(ch) < ord(current.data):
					current = current.lChild
				else:
					current = current.rChild
			if ord(ch) < ord(parent.data):
				parent.lChild = newNode
			else:
				parent.rChild = newNode

  # the search() function will search for a character in the binary
  # search tree and return a string containing a series of lefts
  # (<) and rights (>) needed to reach that character. It will
  # return a blank string if the character does not exist in the tree.
  # It will return * if the character is the root of the tree.
	def search (self, ch):
		st = ''
		current = self.root
		if ch == current.data:
			return '*'

		while current != None and current.data != ch:
			if ord(ch) < ord(current.data):
				current = current.lChild
				st += '<'
			else:
				current = current.rChild
				st += '>'
		if current == None:
			return
		return st

  # the traverse() function will take string composed of a series of
  # lefts (<) and rights (>) and return the corresponding 
  # character in the binary search tree. It will return an empty string
  # if the input parameter does not lead to a valid character in the tree.
	def traverse (self, st):
		current = self.root
		for ch in st:
			if ch == '*':
				return self.root.data
			if ch == '<':
				current = current.lChild
			elif ch == '>':
				current = current.rChild
			if current == None:
				return ''
		return current.data


  # the encrypt() function will take a string as input parameter, convert
  # it to lower case, and return the encrypted string. It will ignore
  # all digits, punctuation marks, and special characters.
	def encrypt (self, st):
	
		st2 = ''
		for ch in st:
			if 65 <= ord(ch) <= 90:                        # converts upper case to lower case
				ch = chr(ord(ch) + 32)                 # by adding ord(32) to upper case characters
			if (97 <= ord(ch) <= 122) or (ord(ch) == 32):  # only adds lower case or space to new string
				st2 += ch
		st = st2
		encrypted = ''
	
		for ch in st:
			encrypted += self.search(ch) + '!'

			

		return encrypted[0:len(encrypted)-1]


  # the decrypt() function will take a string as input parameter, and
  # return the decrypted string.
	def decrypt (self, st):

		current = self.root
		decrypted = ''

		for ch in st: # give directions for adding characters to new string
			if ch == '*':
				current = self.root	
			elif ch == '<':
				current = current.lChild
			elif ch == '>':
				current = current.rChild
			elif ch == '!':
				decrypted += current.data # for characters before end of string
				current = self.root
			elif ch == st[len(st)-1]:
                                             decrypted +=current.data # for very end of string
				
		
		return decrypted


	# in order traversal: left, center, right
	def inOrder (self, node):
		if node != None:
			self.inOrder (node.lChild)
			print (node.data)
			self.inOrder(node.rChild)


def main():


#         open file for encryption and decryption
	f = open('input.txt')
	s = 0
	while(s<8):
                key = f.readline()
                encode = f.readline()
                decode = f.readline()
                skip = f.readline()
                s+=1
                t = Tree(key)
                print(t.encrypt(encode))
                print(t.decrypt(decode))

main()
