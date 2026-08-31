
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        indegree=[0]*(n+1)
        adj=[[] for _ in range(n+1)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            indegree[v]+=1
            indegree[u]+=1
        q = deque()
        for i in range(1,n+1):
            if indegree[i] == 1:
                q.append(i)
        while q:
            x=q.popleft()
            indegree[x]-=1
            for u in adj[x]:
                indegree[u]-=1
                if indegree[u] == 1:
                    q.append(u)
        for u,v in reversed(edges):
            if indegree[u] > 0 and indegree[v]>0:
                return [u,v]
        return []
         



