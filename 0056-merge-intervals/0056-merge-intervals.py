class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda i:i[0])
        output=[intervals[0]]
        
        for start,end in intervals[1:]:
            if start<=output[-1][1]: output[-1][1]=max(end,output[-1][1])
            else: output.append([start,end])
        return output

# Time Complexity - O(nlogn)
# Space Complexity - O(n) or O(1) depending on the sorting algorithm
        