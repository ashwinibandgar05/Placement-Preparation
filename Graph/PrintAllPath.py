
from os import path


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


    def printAllPath(self,start ,end):
        visited=[]
        path=[]

        self.dfs(start,end,visited,path)

    def dfs(self,start,end,visited,path):
        visited.append(start)
        path.append(start)
        if start==end:
            print(path)
            
        
        else:
            for neighbor in self.graph[start]:
                if neighbor not in visited:
                    
                    self.dfs(neighbor,end,visited,path)


        path.pop()
        visited.remove(start)

    



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
g.printAllPath(0,5)