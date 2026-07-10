from collections import deque

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



    def dfs(self,start):
        visited=set()
        self.dfs_helper(start,visited)


    def dfs_helper(self,node,visited):
        visited.add(node)
        print(node,end=" ")

        for neighbour in self.graph[node]:
            if neighbour not in visited:
                self.dfs_helper(neighbour,visited)






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

g.dfs(0)