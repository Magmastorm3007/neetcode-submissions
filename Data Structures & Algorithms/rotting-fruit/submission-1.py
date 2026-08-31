class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        q=deque()
        freshCount = 0
        minutecount=0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]== 1:
                    freshCount+=1
                if grid[i][j] == 2:
                    q.append((i,j,0))
        while q:
            x=q.popleft()
            i=x[0]
            j=x[1]
            minutes=x[2]
            minutecount=minutes
            directions=[(0,1),(0,-1),(1,0),(-1,0)]
            for dr,dc in directions:
                x=i+dr
                y=j+dc
                if x<0 or x>=n or y<0 or y>=m or grid[x][y] == 0 or grid[x][y]==2:
                    continue
                else:
                    grid[x][y]=2
                    freshCount-=1
                    q.append((x,y,minutes+1))
        if freshCount>0:
            return -1
        return minutecount

        
        