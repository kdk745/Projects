	def hasCycle (self):
                N = len(self.Vertices)
                while N > 0:
                        for vertex in self.Vertices:
                                lyst = self.getNeighbors(vertex.label)
                                if len(lyst) == 0:
                                        self.deleteVertex(vertex.label)
                        N -=1
                return (len(self.Vertices) > 0)
