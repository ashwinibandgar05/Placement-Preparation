class graph:
    def __init__(self):
        self.graph={}

    def add_edge(self,u,v):
        if u not in self.graph:
            self.graph[u]=[]

        if v not in self.graph:
            self.graph[v]=[]


        self.graph[u].append(v)
        self.graph[v].append(u)

    def display(self):
        for vertex in self.graph:
            print(vertex,"->",self.graph[vertex])


    def has_cycle(self):

        visited = set()

        for vertex in self.graph:
            if vertex not in visited:
                if self.dfs(vertex, visited, -1):
                    return True

        return False

    def dfs(self, node, visited, parent):

        visited.add(node)

        for neighbour in self.graph[node]:

            if neighbour not in visited:

                if self.dfs(neighbour, visited, node):
                    return True

            elif neighbour != parent:
                return True

        return False

    

g=graph()
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,3)
g.add_edge(2,4)
g.add_edge(3,4)
g.add_edge(3,5)
g.add_edge(4,5)
g.add_edge(5,6)

g.display()

g.has_cycle()
print(g.has_cycle())



    
