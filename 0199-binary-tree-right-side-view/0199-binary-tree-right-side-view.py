# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        queue=deque()
        level=0
        res=[]
        if root: queue.append(root)

        while len(queue):
            subset=[]
            for i in range(len(queue)):
                
                curr=queue.popleft()
                subset.append(curr.val)

                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
            level+=1
            res.append(subset[-1])
        return res
        

        