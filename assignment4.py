class Vertex:
    def __init__(self, id) -> None:
        self.id = id 
        self.edges = []
    
    def add_edge(self, source, destination, weight):
        new_edge = Edge(source, destination, weight)
        self.edges.append(new_edge)

    def __str__(self) -> str:
        return_string = str(self.id) + ", \n" + "my edges are: {"
        for edge in self.edges:
            return_string = return_string + str(edge)
        return_string = return_string + "}"
        return return_string


class Edge:
    def __init__(self, u, v, w) -> None:
        self.u = u
        self.v = v
        self.w = w
    
    def __str__(self) -> str:
        return_str = "[source: " + str(self.u) + ", " + "destination: " + str(self.v) + ", " + "weight: " + str(self.w) + "]"
        return return_str


# string comparison between 2 words to see if they differ by 1 char
def string_comparison(word1, word2) -> bool:
    differ = False
    i = 0
    while i in range(len(word1)):
        if word1[i] == word2[i]:
            i += 1
            continue
        else:
            if differ == True:
                return False
            else:
                i += 1
                differ = True
    return differ


class WordGraph:
    def __init__(self, V) -> None:
        self.vertices = [None] * len(V)

        # creates all vertices in list
        for i in range(len(V)):
            self.vertices[i] = Vertex(V[i])
        
        # check whether to add edges - differ by 1 char
        for i in range(len(V)):
            for j in range(i+1, len(V)):
                if string_comparison(V[i], V[j]):
                    self.vertices[i].add_edge(i, j, 1)
                    self.vertices[j].add_edge(j, i, 1)

    def __str__(self) -> str:
        return_str = ""
        for vertex in self.vertices:
            return_str = return_str + "Vertex " + str(vertex) + "\n"
        return return_str
    
    # Task 1
    def best_start_word(self, target_words):
        pass



if __name__ == "__main__":
    vertices = ["aaa","aad","dad","daa","aca", "acc", "aab", "abb"]
    my_graph = WordGraph(vertices)
    print(my_graph)

