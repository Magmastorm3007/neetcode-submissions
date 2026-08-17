
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        res=0
        dp=dict()
        def solve(i:int,csum):
            if csum == amount:
                return 1
            
            if i>=n or csum > amount:
                return 0
            if (i,csum) in dp:
                return dp[(i,csum)]
            # skip
            a=solve(i+1,csum)
               
            b=solve(i,csum+coins[i])
            dp[(i,csum)]=a+b
            return dp[(i,csum)]
        return solve(0,0)
            