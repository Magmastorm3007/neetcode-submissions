class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=list()
        for i in range(0,n+1):
            cnt=0
            x=i
            while x:
                if x & 1:
                    cnt+=1
                x=x>>1
            ans.append(cnt)
        return ans

