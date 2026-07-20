class Solution:
    def dfs(self, i:int, j:int, grid: List[List[str]]):
        n=len(grid)
        m=len(grid[0])
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        if i< 0 or j< 0 or i>=n or j>=m or grid[i][j] == "0":
            return
        grid[i][j] = "0"

        for r,c in directions:
            self.dfs(i+r,j+c,grid)
        
         

    def numIslands(self, grid: List[List[str]]) -> int:
        n=len(grid)
        m=len(grid[0])
        islands=0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    islands+=1
                    self.dfs(i,j,grid)
        return islands

