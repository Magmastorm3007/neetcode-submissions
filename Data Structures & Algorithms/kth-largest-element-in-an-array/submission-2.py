import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr=[-x for x in nums]
        heapq.heapify(arr)
        while(k-2>=0):
            heapq.heappop(arr)
            k-=1
        return -heapq.heappop(arr)