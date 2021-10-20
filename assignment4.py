class WordGraph:

    # take as input a nonempty list of words and construct
    # an appropriate graph from them. The words will contain only lowercase a-z characters, and
    # will all be the same length, which will not be 0.
    def __init__(self, V) -> None:
        self.vertices = [None] * len(V)
        for i in range(len(V)):
            self.vertices[i] = Vertex(V[i])

    def __str__(self) -> str:
        return_str = ""
        for vertex in self.vertices:
            return_str = return_str + "Vertex " + str(vertex) + "\n"
        return return_str
    
class Vertex:
    def __init__(self, id) -> None:
        self.id = id 
        self.edges = []
    
    def __str__(self) -> str:
        return_str = str(self.id)
        return return_str
    
class Edge:
    def __init__(self, u, v, w) -> None:
        self.u = u
        self.v = v
        self.w = w

if __name__ == "__main__":
    vertices = ["aaa","aab","aac","aad","aae"]
    my_graph = WordGraph(vertices)
    print(my_graph)

