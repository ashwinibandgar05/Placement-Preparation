class graph:
    def __init__(self):
        self.graph={}
    
    def add_vertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex]=[]

    def add_edges(self,u,v):
        self.add_vertex(u)
        self.add_vertex(v)

        self.graph[u].append(v)
        self.graph[v].append(u)

    def display(self):
        for i in self.graph:
            print(i ,"->",self.graph[i])


g=graph()

g.add_edges(0,1)
g.add_edges(1,2)
g.add_edges(1,3)
g.add_edges(2,3)
g.add_edges(2,4)


g.display()



