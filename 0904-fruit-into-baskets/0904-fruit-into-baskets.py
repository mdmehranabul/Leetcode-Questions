class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l,tot,res=0,0,0
        hashmap=collections.defaultdict(int)

        for r in range(len(fruits)):
            hashmap[fruits[r]]+=1
            tot+=1
        
            while len(hashmap)>2:
                f=fruits[l]
                hashmap[f]-=1
                tot-=1
                l+=1
                if not hashmap[f]:
                    hashmap.pop(f)
            
            res=max(res,tot)
        
        return res