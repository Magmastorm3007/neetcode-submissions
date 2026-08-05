class Solution:
    def solve(self,i,sum_num,nums,target,v:List[int],result):
        if sum_num == target:
            result.append(list(v))
            return
        
        if i >=len(nums) or sum_num > target:
            return
        
        v.append(nums[i])
        self.solve(i,nums[i]+sum_num,nums,target,v,result)
        v.pop()
        self.solve(i+1,sum_num,nums,target,v,result)

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result=[]
        self.solve(0,0,nums,target,[],result)
        return result