class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        
        n=len(board)
        m=len(board[0])
        
        def backtrack(i,j,k):
            if k == len(word):
                return True
            if i<0 or j<0 or i>=n or j>=m or board[i][j]!=word[k] or board[i][j]=="#":
                return False
            
            res=[False]*4
            counter=0
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr,dc in directions:
                board[i][j]="#"
                res[counter]=backtrack(i+dr,j+dc,k+1)
                counter+=1
                board[i][j]=word[k]
                

            board[i][j]=word[k]
            return res[0] or res[1] or res[2] or res[3]
               

            

        
        for i in range(n):
            for j in range(m):
                if backtrack(i, j, 0):
                    return True

        return False
            
        