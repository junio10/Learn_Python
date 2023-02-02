#implementation of the graph

class Graph:
    def __init__(self, numVertices):
        self.num_vertices = numVertices
        self.vertices = [0 for j in range(self.num_vertices)]
        self.edge = [[0 for j in range(self.num_vertices)] for i in range(self.num_vertices)]
        self.cont = 0
        
        
       
        
    def AddVertex(self, vertex):
        self.vertices[self.cont]= vertex
        self.cont += 1
        
    def AddEdge(self, vertex1, vertex2):
        self.edge[vertex1][vertex2] = 1
        self.edge[vertex2][vertex1] = 1
        
    
    def DisplayVertex(self):
        for vertex in self.vertices:
            print(vertex)
    
    def DisplayEdge(self):
        for i in range(3):
            print(i, end = "")
            for j in len(3):
                print(j)
            
    def tamanho(self):
        return len(self.vertices)
    
        
def main():
    Grafo = Graph(3)
    Grafo.AddVertex('a')
    Grafo.AddVertex('b')
    Grafo.AddVertex('c')
    
    Grafo.DisplayVertex()
    # print("Matriz")
    # Grafo.DisplayEdge()
    
   
    
    Grafo.AddEdge(0,1)
    Grafo.AddEdge(0,2)
    # Grafo.AddEdge(1,2)
    
    #Grafo.DisplayEdge()
    
    
    
    
main()