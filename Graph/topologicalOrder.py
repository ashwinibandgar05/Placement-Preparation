class graph:
    def __init__(self):
        self.graph={}

    def add_edge(self,u,v):
        if u not in self.graph:
            self.graph[u]=[]

        if v not in self.graph:
            self.graph[v]=[]


        self.graph[u].append(v)



    def topo_sort(self):
        stack=[]
        visited=set()

        for vertex in self.graph:
            if vertex not in visited:
                self.dfs(vertex,visited,stack)

        stack.reverse()
        print("stack")
        print(stack)


    def dfs(self,node,visited,stack):
        visited.add(node)

        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self.dfs(neighbor,visited,stack)

        stack.append(node)



    def display(self):
        print("all the element of graph edgewisee")
        for i in self.graph:
            print(i,"->",self.graph[i])




g=graph()


g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)


g.display()
g.topo_sort()