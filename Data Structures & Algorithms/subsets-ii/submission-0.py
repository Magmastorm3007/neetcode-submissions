class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        temp=list()
        result=list()
        nums.sort()
        def backtrack(i:int, temp:List[int]):
            if i >= n:
                
                result.append(temp[:])
                return
            
            temp.append(nums[i])
            backtrack(i+1,temp)
            temp.pop()
            while i+1< n and nums[i]==nums[i+1]:
                i+=1   
            backtrack(i+1,temp)

        backtrack(0,temp)
        return result