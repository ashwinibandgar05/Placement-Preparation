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

    def bfs(self,start):
        visited=set()
        queue=deque()

        visited.add(start)
        queue.append(start)

        while queue:
            node=queue.popleft()
            print(node,end=" ")

            for neighbour in self.graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour )
                    queue.append(neighbour )

                    

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
g.bfs(0)



