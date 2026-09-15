class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        interval=intervals[0]
        start=interval[0]
        end=interval[1]
        ans=list()
        for i in range(len(intervals)):
            x=intervals[i]
            start_i=x[0]
            end_i=x[1]
            if end<=end_i and start_i<=end:
                end=max(end,end_i)
                continue
            
            else:
                if start_i>end and end_i>end:
                    ans.append([start,end])
                    start=start_i
                    end=end_i
        ans.append([start,end])
        return ans
                

            

                
            




