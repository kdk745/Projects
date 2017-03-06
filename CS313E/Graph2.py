#  File: Graph.py

#  Description: Program that manipulates graphs.

#  Student Name: Juanito Taveras

#  Student UT EID: jmt3686

#  Partner Name: Kayne Khoury

#  Partner UT EID: kdk745

#  Course Name: CS 313E

#  Unique Number: 51730

#  Date Created: 4/30/2015

#  Date Last Modified: 5/4/2015




class Stack (object):
	def __init__ (self):
		self.stack = []

	# add an item to the top of the stack
	def push (self, item):
		self.stack.append ( item )

	# remove an item from the top of the stack
	def pop (self):
		return self.stack.pop()

	# check what item is on top of the stack without removing it
	def peek (self):
		return self.stack[len(self.stack) - 1]

	# check if a stack is empty
	def isEmpty (self):
		return (len(self.stack) == 0)

	# return the number of elements in the stack
	def size (self):
		return (len(self.stack))


class Queue (object):
	def __init__ (self):
		self.queue = []

	def enqueue (self, item):
		self.queue.append (item)

	def dequeue (self):
		return (self.queue.pop(0))

	def isEmpty (self):
		return (len (self.queue) == 0)

	def size (self):
		return len (self.queue)

class Vertex (object):
	def __init__ (self, label):
		self.label = label
		self.visited = False

	# determine if vertex was visited
	def wasVisited (self):
		return self.visited 

	# determine the label of the vertex
	def getLabel (self):
		return self.label

	# string representation of the label
	def __str__(self):
		return str (self.label)


class Edge (object):
	def __init__ (self, fromVertex, toVertex, weight = 1):
		self.u = fromVertex
		self.v = toVertex
		self.weight = weight

	# comparison operators
	def __lt__ (self, other):

                return self.weight < other.weight
		

	def __le__ (self, other):

                return self.weight <= other.weight

	def __gt__ (self, other):

                return self.weight > other.weight

	def __ge__ (self, other):

                return self.weight >= other.weight

	def __eq__ (self, other):

                return self.weight == other.weight
	def __ne__ (self, other):

                return self.weight != other.weight




class Graph (object):
	def __init__ (self):
		self.Vertices = []
		self.adjMat = []


	# check if a vertex label already exists
	def hasVertex (self, label):
		for i in range (len(self.Vertices)):
			if label == (self.Vertices[i].label):
				return True
		return False

	# add a Vertex with a given label
	def addVertex (self, label):
		if not self.hasVertex (label):            # there cannot be two of the same label
			self.Vertices.append (Vertex (label))
		
	
			# add a new column in the adjacency matrix for new Vertex
			nVert = len(self.Vertices)
			for i in range (nVert - 1):
				(self.adjMat[i]).append(0)

			# add a new row for the new Vertex in the adjacency matrix
			newRow = []
			for i in range (nVert):
				newRow.append(0)
			self.adjMat.append(newRow)

	# get index from vertex label
	def getIndex (self, label):
		for i in range (len(self.Vertices)):
			if label == (self.Vertices[i].label):
				return i
		return -1

		


	# get edge weight between two vertices
	# return -1 if edge does not exist
	def getEdgeWeight (self, fromVertexLabel, toVertexLabel):
		if 0 < fromVertexLabel <= (len(self.adjMat)) and 0 < toVertexLabel <= (len(self.adjMat)):
			return self.adjMat[fromVertexLabel][toVertexLabel]
		else:
			return -1
		

	# get a list of neighbors that you can go to from a vertex
	# return empty list if there are none
	def getNeighbors (self, label):
		index = self.getIndex(label)
		row = self.adjMat[index]
		lyst = []
		for i in range(len(row)):
			if row[i] > 0:
				lyst.append(self.Vertices[i].label)
		return lyst
		
				

	# get a copy of the list of vertices
	def getVertices (self):
		lyst = []
		for i in range (len(self.Vertices)):
			lyst.append(str((self.Vertices[i]).label))
		
		return lyst

	
	# determine if the graph has a cycle
	def hasCycle (self):
		for vertex in self.vertices:
                        
                        

                        

	# return a list of vertices after a topological sort
	def toposort (self):
		top_sorted = []
		stack = Stack()
		# set all vertices to not visited
		for i in range (len(self.Vertices)):
			self.Vertices[i].visited = False

		# first vertex will be vertex that no edge is pointing at		
		for col in range (len(self.adjMat[0])):
			count = 0
			for row in self.adjMat:
				if row[col] == 0:   # if entire column in adjacency matrix is zero
					count += 1  # that's the correct starting vertex
			if count == len(self.adjMat):
				startVertex = col

		v = self.getIndex(startVertex)
	
		for i in range (len(self.Vertices)):
			if (self.Vertices[i]).visited == False:
				self.dfs_sort(i, stack)

		lyst = []
	#	self.dfs(startVertex)
		return (stack)
		
	def dfs_sort(self, v, stack):
		self.Vertices[v].visited = True
		lyst = self.getNeighbors (self.Vertices[v].label)
		for label in lyst:
			idx = self.getIndex(label)
			if self.Vertices[idx].visited == False:
				self.dfs_sort(idx, stack)
		stack.push(v)
	

	# prints a list of edges in ascending order of their weights
	# list is in the form [v1 - v2, v2 - v3, ..., vm - vn]
	def edgeList (self):
		edgelist = []
		row = []
		created = []
		for i in range (len(self.adjMat)):
			for j in range (len(self.adjMat[i])):
				weight = self.adjMat[i][j]
				if weight > 0:
					fromVertex = self.Vertices[i].label
					toVertex = self.Vertices[j].label	
					edge = (fromVertex + "--" + toVertex + " " + str(weight))
					if edge not in edgelist:
						edgelist.append(edge)

		# sort list in ascending order
		for i in range (1, len(edgelist)):
			j = i
			while (j > 0) and (int(edgelist[j][-1]) < int(edgelist[j - 1][-1])):
				edgelist[j], edgelist[j - 1] = edgelist[j - 1], edgelist[j]
				j -= 1

		return edgelist

	def getEdgeWeight (self, fromVertexLabel, toVertexLabel):
                vertices = self.getVertices()

                if fromVertexLabel in vertices and toVertexLabel in vertices:

                        if self.adjMat[self.getIndex(fromVertexLabel)][self.getIndex(toVertexLabel)] == 0:

                                return -1
                        else:

                                return self.adjMat[self.getIndex(fromVertexLabel)][self.getIndex(toVertexLabel)]

                else:

                        return -1


	# determine shortest path from a single vertex
	def shortestPath(self,fromVertexLabel):
                vertices = self.getVertices()
                weights = self.adjMat[self.getIndex(fromVertexLabel)]
                results = []
                included = []
                for i in range(len(self.Vertices)):
                        included.append(True)
                for vertex in vertices:
                        if vertex == fromVertexLabel:
                                results.append([vertex,0,None])
                        for weight in weights:
                                if weight > 0 and weights.index(weight) == self.getIndex(vertex):
                                        results.append([vertex,weight,fromVertexLabel])
                                        included[self.getIndex(vertex)] = False
                        if included[self.getIndex(vertex)] != False and vertex != fromVertexLabel :
                                results.append([vertex,float('inf'),None])
                                included[self.getIndex(vertex)] = False
                while False in included:
                        dists = []
                        for vertex in results:
                                if included[self.getIndex(vertex[0])] == False:
                                        dists.append(vertex[1])
                        minn = min(dists)
                        for vertex in results:
                                if vertex[1] == minn:
                                        F = vertex
                                        included[self.getIndex(F[0])] = True
                                        weights = self.adjMat[self.getIndex(F[0])]
                                        
                                        for vertex in results:
                                     
                                                for weight in weights:
                                                        if weight > 0 and weights.index(weight) == self.getIndex(vertex[0]) and (F[1] + weight < vertex[1]):
                                                                vertex[1] = F[1] + weight
                                                                vertex[2] = F[0]
                return results

	# delete an edge from the adjacency matrix
#	def deleteEdge (self, fromVertexLabel, toVertexLabel):

	# delete a vertex from the vertex list and all edges from and
	# to it in the adjacency matrix
#	def deleteVertex (self, vertexLabel):

	# add weighted undirected edge to graph
	def addUndirectedEdge (self, start, finish, weight = 1):
		self.adjMat[start][finish] = weight
		self.adjMat[finish][start] = weight
		edge = Edge (start, finish, weight)



	def addDirectedEdge (self, start, finish, weight = 1):
		self.adjMat[start][finish] = weight
	
	
	# does a depth first search in a graph
	def dfs (self, v):     # v is index of vertex
		# create a stack
		theStack = Stack ()
		
		# mark the vertex as visited and push onto the stack
		(self.Vertices[v]).visited = True     # mark first vertex as visited
		theStack.push(v)                      # add vertex to stack
		print (self.Vertices[v])              # print vertex that you just added
		while not theStack.isEmpty():         # while stack is not empty
			# get an adjacent unvisited vertex
			u = self.getAdjUnvisitedVertex (theStack.peek())    
			if u == -1:
				u = theStack.pop()
			else:
				(self.Vertices[u]).visited = True
				theStack.push(u)
				print (self.Vertices[u])

	# Choose any city and do depth-first search with a stack
	# Change all flags to flase when you're done
		for i in range (len(self.Vertices)):
			self.Vertices[i].visited = False

	# return an unvisited vertex adjacent to v
	def getAdjUnvisitedVertex (self, v):
		for i in range (len(self.Vertices)):
			if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).wasVisited()):
				return i
		return -1

	def bfs (self, v):
		# create a queue
		theQueue = Queue ()
		
		# mark the vertex as visited and enqueue
		(self.Vertices[v]).visited = True
		theQueue.enqueue(v)
		print (self.Vertices[v])
		
		while (not theQueue.isEmpty()):
			# get the vertex at the front
			v1 = theQueue.dequeue()
			# get an adjacent unvisited vertex
			v2 = self.getAdjUnvisitedVertex (v1)
			while v2 != -1:
				(self.Vertices[v2]).visited = True
				print (self.Vertices[v2])
				theQueue.enqueue(v2)
				v2 = self.getAdjUnvisitedVertex (v1)

		# reset flags
		for i in range (len(self.Vertices)):
			self.Vertices[i].visited = False
	
def main():

	# create a Graph object
	cities = Graph()

	# open file for reading
	inFile = open ("./graph.txt", "r")
	# read the vertices
	numVertices = int((inFile.readline()).strip())
	
	for i in range (numVertices):
		city = (inFile.readline()).strip()
		cities.addVertex(city)

	# read the edges
	numEdges = int((inFile.readline()).strip())

	for i in range (numEdges):
		edge = (inFile.readline()).strip()
		edge = edge.split()
		start = int (edge[0])
		finish = int (edge[1])
		weight = int (edge[2])
		cities.addDirectedEdge (start, finish, weight)

	# read the starting vertex for dfs
	startVertex = (inFile.readline()).strip()

	
	# close file
	inFile.close()

	# test depth first search
	print ("BFS from", startVertex + ":")
	v = cities.getIndex(startVertex)
	cities.bfs(v) # write function here
	print()

	# test breadth first search
	print ("DFS from", startVertex + ":")
	cities.dfs(v)
	print()

	# test topological sort
	print ("Topological Sort:")
	stack = cities.toposort()
	for i in range (stack.size()):
		idx = stack.pop()
		city = cities.Vertices[idx].label
		print (city)
		
	print()

	# test edge list in ascending order of weights
	print ("Ascending Edges:")
	lyst = cities.edgeList()
	for item in lyst:
		print(item)
	print()

	# test single source shortest path algorithm
	print ("SSSP from", startVertex + ":")
	result = cities.shortestPath('Dallas')
	for i in result:
                if i[0] != 'Dallas':
                        print('Dallas->',i[0],':',i[1])
                








main()

