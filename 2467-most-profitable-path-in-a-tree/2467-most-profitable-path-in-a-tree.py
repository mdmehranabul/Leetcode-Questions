class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        adj=defaultdict(list)
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        bob_times={}

        def dfs(node,prev,time):
            if node==0:
                bob_times[node]=time
                return True

            for nei in adj[node]:
                if nei == prev:
                    continue
                if dfs(nei, node, time+1):
                    bob_times[node]=time
                    return True
            return False
        
        dfs(bob,-1,0)
        print(bob_times)

        q=deque([(0,-1,0,amount[0])])
        res=float("-inf")
        while q:
            node,prev,time, amt=q.popleft()

            for nei in adj[node]:
                if nei == prev: continue

                nei_time=time+1
                nei_amt=amount[nei]
                if nei in bob_times:
                    if nei_time>bob_times[nei]: nei_amt=0
                    if nei_time==bob_times[nei]: nei_amt=nei_amt//2

                q.append((nei,node,time+1,amt+nei_amt))
                if len(adj[nei])==1:
                    res=max(res,amt+nei_amt)
        
        return res