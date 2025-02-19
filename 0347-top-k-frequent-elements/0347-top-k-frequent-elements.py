class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count,res={},[]
        freq=[[] for i in range(len(nums)+1)]

        for n in nums:
            count[n]=1+count.get(n,0)
        
        for val,cnt in count.items():
            freq[cnt].append(val)
        
        for i in range(len(freq)-1,-1,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k: return res
# Time Complexity - O(n)
# Space Complexity - O(n)
