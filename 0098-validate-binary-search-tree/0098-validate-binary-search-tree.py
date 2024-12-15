# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def bin_tree(root,low,high):
            if not root: return True
            if not (root.val>low and root.val<high): return False

            return (bin_tree(root.left,low,root.val) and bin_tree(root.right,root.val,high))
        

        return bin_tree(root,float("-infinity"),float("infinity"))

# Time complexity - O(n)
# Space complexity - O(n)
        