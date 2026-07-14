class graph:
    def __init__(self):
        self.graph={}

    def add_edges(self,u,v):
        if u not in self.graph:
            self.graph[u]=[]
        if v not in self.graph:
            self.graph[v]=[]

        self.graph[u].append(v)
        self.graph[v].append(u)

    def display(self):
        for vertex in self.graph:
            print(vertex,"->",self.graph[vertex])

    def cycle_detection(self):
        visited=set()
        for vertex in self.graph:
            if vertex not in visited:
                if self.dfs(visited,vertex,-1):
                    return True
            
        return False
    
    def dfs(self,visited,current,parent):
        visited.add(current)

        for neighbor in self.graph[current]:
            if neighbor not in visited:
                if self.dfs(visited,neighbor,current) :
                    return True
                
            elif parent!=neighbor:
                return True
        return False
    



g=graph()
g.add_edges(0,1)
g.add_edges(0,4)
g.add_edges(1,2)
# g.add_edges(1,4)
g.add_edges(2,3)
g.add_edges(4,5)
g.display()
print(g.cycle_detection())