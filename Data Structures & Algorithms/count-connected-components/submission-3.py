# class dsu:
#     for i in range
#     def find(i):


class Solution:

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        parent=[0]*n
        def find(i):
            if parent[i] == i:
                return i
            parent[i]=find(parent[i])
            return parent[i]

        def make_union(x,y):
            root_x=find(x)
            root_y=find(y)
            if root_x != root_y:
                parent[root_y] = root_x
        
        for i in range(n):
            parent[i]=i
        for x,y in edges:
            make_union(x,y)
        sorted(edges)
        connectedComponents=0
        for i in range(0,n):
            if parent[i] == i:
                connectedComponents+=1
        return connectedComponents

        


        

        


