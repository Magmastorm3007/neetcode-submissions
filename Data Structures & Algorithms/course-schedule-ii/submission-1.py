class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n=numCourses
        indegree=[0]*n
        adj=[[] for _ in range(n)]
        for u,v in prerequisites:
            adj[v].append(u)
            indegree[u]+=1
        topo=list()
        q=deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        while q:
            x=q.popleft()
            topo.append(x)
            indegree[x]-=1
            for u in adj[x]:
                indegree[u]-=1
                if indegree[u] == 0:
                    q.append(u)
        for i in range(n):
            if indegree[i]>0:
                return []
        return topo
            