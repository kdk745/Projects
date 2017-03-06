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
	def __str__(self):
		return str(self.data)



class CircularList(object):
	# Constructor
	def __init__ ( self ):

                self.first = Link(None,None)

                self.first.next = self.first

	
		

	

	# Insert an element in the list
	def insert ( self, item):

                newLink = Link(item)

                newLink.next = self.first

                self.first = newLink

                
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
		current = self.first   # make new variable, "current", equal to self.first
		previous = self.first
		if current == None:
			return None
		while current.data != data:
			if current.next == None:
				return None
			else:
				previous = current
				current = current.next

		if current == self.first:
			self.first = self.first.next
		else:
			previous.next = current.next

		return current

	# Delete the nth link starting from the Link start 
	# Return the next link from the deleted Link
	def deleteAfter ( self, start, n ):
                current = self.find(start) # returns current, which is first person
                probe = self.find(start)#	first = current.data
                count = n
                count2 = n

                while count > 1 and current.data != None:
                        probe = probe.next
                        count -=1
                while count2 > 0 and probe.data != None:
                        current = current.next
                        count2 -= 1
                        probe.next = current.next

	# Return a string representation of a Circular List
	def __str__ ( self ):
		current = self.first

		while current.data != None:

                        print(current.data)

                        current = current.next
		
		'''	
		while self != None:
			print (self.first)
			self = self.next
		'''
	def __len__ (self):
		current = self.first
		length = 0
		if current == None:
			return None
		while current != None:
			length += 1
			current = current.next
		return length



#		return str(self.first)



def main():
	inFile = open ("./josephus.txt", "r")
	num_sold = inFile.readline()
	num_sold = int(num_sold.strip())
	first_sold = inFile.readline()
	first_sold = int(first_sold.strip())
	elim_num = inFile.readline()
	elim_num = int(elim_num.strip())
	
	lyst = CircularList()
	for sold in range (1, num_sold+1):
		lyst.insert(sold)

	start = str (lyst.find (first_sold))

	'''
	while len(lyst) > 1:
		next_delete = (int(str(start)) + elim_num)
		current = lyst.find (next_delete)
		print (current)
		lyst.delete(current)
		self.first = 
	'''
	lyst.deleteAfter(1,3)

	print(lyst)


	

	
	

main()
