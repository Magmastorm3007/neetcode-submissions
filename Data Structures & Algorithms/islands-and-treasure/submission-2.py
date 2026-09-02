class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n=len(grid)
        m=len(grid[0])
        visited=set()
        # def dfs(i,j,sm):
        #     if i <0 or i>=n or j<0 or j>=m or grid[i][j]== -1 or sm>grid[i][j]:
        #         return
            
        #     grid[i][j]=sm
        #     directions=[(0,1),(0,-1),(1,0), (-1,0)]
        #     for dr,dc in directions:
        #         dfs(i+dr,j+dc,sm+1)
            
        # for i in range(n):
        #     for j in range(m):
        #         if grid[i][j] == 0:
        #             dfs(i,j,0)
        q=deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q.append((i,j,0))
        while q:
            x=q.popleft()
            i=x[0]
            j=x[1]
            sm=x[2]
            if i <0 or i>=n or j<0 or j>=m or grid[i][j]== -1 or sm>grid[i][j] or (i,j) in visited:
                 continue
            visited.add((i,j))
            grid[i][j]=sm
            directions=[(0,1),(0,-1),(1,0), (-1,0)]
            for dr,dc in directions:
                q.append((i+dr,j+dc,sm+1))
            
                
            
        
        

       