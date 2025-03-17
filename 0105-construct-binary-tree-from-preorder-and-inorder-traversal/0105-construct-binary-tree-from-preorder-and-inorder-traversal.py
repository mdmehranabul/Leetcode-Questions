# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder: return
        root=TreeNode(preorder[0])
        interest=inorder.index(preorder[0])
        print(interest)
        root.left=self.buildTree(preorder[1:interest+1],inorder[:interest])
        root.right=self.buildTree(preorder[interest+1:],inorder[interest+1:])

        return root
        