#  File: Josephus.py

#  Description:

#  Student Name: Juanito Taveras

#  Student UT EID: jmt3686

#  Partner Name: Kayne Khoury

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created: 4/2/2015

#  Date Last Modified: 4/2/2015

class Link(object):
	def __init__ (self, data, next = None):
		self.data = data
		self.next = next




class CircularList(object):
	# Constructor
	def __init__ ( self ): 
		self.first = None
		self.last = None

	# Insert an element in the list
	def insert ( self, item ):
		newLink = Link (item)
		newLink.next = self.first
		self.first = newLink

	# Find the link with the given key
	def find (self, data):
		current = self.first
		if current == None:
			return None
		while (current.data != data):
			if (current.next == None):
				return None
			else:
				current = current.next
		return current

	# Delete a link with a given key
	def delete (self, data):
		current = self.first
		previous = self.first
		if current == None:
			return None
		while current.data != data:
			if current.next == None:
				return None
			else:
				previous = current
				current = current.next
		if current = self.first:
			self.first = self.first.next
		else:
			previous.next = current.next
		return current

	# Delete the nth link starting from the Link start 
	# Return the next link from the deleted Link
	def deleteAfter ( self, start, n ):


	# Return a string representation of a Circular List
	def __str__ ( self ):



def main():
	inFile = open ("./josephus.txt", "r")
	num_sold = inFile.readline()
	num_sold = int(num_sold.strip())
	first_sold = inFile.readline()
	first_sold = int(first_sold.strip())
	elim_num = inFile.readline()
	elim_num = int(elim_num.strip())

	lyst = CircularList()

	for i in range (1, num_sold):
		lyst.insert(i)

	print (lyst)
	
	

main()
