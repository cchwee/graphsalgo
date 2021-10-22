class Vertex:
    def __init__(self, id) -> None:
        self.id = id 
        self.edges = []
    
    def add_edge(self, tuple):
        source = tuple[0]
        destination = tuple[1]
        weight = tuple[2]

        # create and add new edge
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
        self.words = V

        # creates all vertices in list
        for i in range(len(V)):
            self.vertices[i] = Vertex(V[i])
        
        # check whether to add edges - differ by 1 char
        self.build_word_ladder(V)

    # for Task 1 -> weight = 1 if differ by one char
    def build_word_ladder(self, V):
        for i in range(len(V)):
            for j in range(i+1, len(V)):
                if string_comparison(V[i], V[j]):
                    self.vertices[i].add_edge((i, j, 1))
                    self.vertices[j].add_edge((j, i, 1))

    def __str__(self) -> str:
        return_str = ""
        for vertex in self.vertices:
            return_str = return_str + "Vertex " + str(vertex) + "\n"
        return return_str
    
    # Task 1 
    def best_start_word(self, target_words):
        
        # unique case where there's only one word
        if len(target_words) == 1:
            return target_words[len(target_words)-1]
        
        memo = self.floyd_warshall(self.words) 
        res = []

        # go through vertical column of index memo
        for i in range(len(self.words)):
            dist = [] 
            for index in target_words:

                # get all ladder
                dist.append(memo[index][i])
            
            # get all longest word ladder for target words
            res.append(max(dist))

        # choose shortest among all longest
        if min(res) != 0 and min(res) != float("inf"):
            return res.index(min(res))
        else:
            return -1
            

    def floyd_warshall(self, V): 
        # initalise matrix with inf values
        memo_matrix = [[float("inf") for _ in range(len(V))] for _ in range(len(V))]

        # vertex[i][i] = 0 --> ie, vertex A to A has no edges
        for i in range(len(V)):
            memo_matrix[i][i] = 0
        
        # insert all other edges
        for i in range(len(V)):
            for edges in self.vertices[i].edges:
                memo_matrix[edges.u][edges.v] = edges.w

        # run algo for min distance
        for k in range(len(V)):
            for i in range(len(V)):
                for j in range(len(V)):
                    memo_matrix[i][j] = min(memo_matrix[i][j], memo_matrix[i][k] + memo_matrix[k][j])
        
        return memo_matrix



if __name__ == "__main__":
    words = ["aaa","aad","dad","daa","aca", "acc", "aab", "abb"]
    # words = ['aaa','bbb','bab','aaf','aaz','baz','caa','cac','dac','dad','ead','eae','bae','abf','bbf']
    g = WordGraph(words)
    print(g)
    print(g.best_start_word([2,7,5]))

