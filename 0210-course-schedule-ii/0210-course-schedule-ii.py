class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visit,cycle=set(),set()
        coursemap={i:[] for i in range(numCourses)}
        res=[]

        for crs, pre in prerequisites:
            coursemap[crs].append(pre)

        def dfs(crs):
            if crs in cycle: return False
            if crs in visit: return True

            cycle.add(crs)

            for pre in coursemap[crs]:
                if not dfs(pre): return False
            
            cycle.remove(crs)
            visit.add(crs)
            res.append(crs)
            return True

        
        for crs in range(numCourses):
            if not dfs(crs): return []
        return res