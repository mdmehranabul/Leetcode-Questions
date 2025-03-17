# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        height=0
        q=deque()
        q.append(root)

        while q:
            for i in range(len(q)):
                curr=q.popleft()

                if curr.left:q.append(curr.left)
                if curr.right:q.append(curr.right)
            height+=1
        return height
        