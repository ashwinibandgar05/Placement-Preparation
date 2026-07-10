class graph:
    def __init__(self):
        self.edge=[]

    def add_edges(self,u,v):
        self.edge.append((u,v))

    def display(self):
        print("all the element of graph edgewisee")
        for i in self.edge:
            print(i)




g=graph()


g.add_edges(0,1)
g.add_edges(0,2)
g.add_edges(1,3)
g.add_edges(2,4)
g.add_edges(3,4)
g.add_edges(3,5)
g.add_edges(4,5)
g.add_edges(5,6)

g.display()