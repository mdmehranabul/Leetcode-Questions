# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root: return False

        if self.sametree(root,subRoot): return True

        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
    
    def sametree(self,p,q):
        if not p and not q: return True

        if not p or not q or p.val!=q.val: return False

        return self.sametree(p.left,q.left) and self.sametree(p.right,q.right)


# Time Complexity : O(m*n)
# Space Complexity : O(m+n)