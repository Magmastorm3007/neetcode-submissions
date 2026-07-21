class Solution:
    def solve(self,i:int, nums:List[int],dp):
        if i >= len(nums):
            return 0;
        if dp[i]!=-1:
            return dp[i]
        a=nums[i]+self.solve(i+2,nums,dp)
        b=self.solve(i+1,nums,dp)

        dp[i]=max(a,b)
        return dp[i]

    def rob(self, nums: List[int]) -> int:
        dp=[-1]*len(nums)
        return self.solve(0,nums,dp)