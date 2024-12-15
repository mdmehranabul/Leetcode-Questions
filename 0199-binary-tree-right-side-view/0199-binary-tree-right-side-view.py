# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # global res
        # res=[]
        # def dfs(root,level):
        #     if not root: return

        #     if level==len(res): res.append(root.val)
        #     print(res)
        #     dfs(root.right,level+1)
        #     dfs(root.left,level+1)
        
        # dfs(root,0)
        # return res
        res=[]
        q=deque()
        if root:
            q.append(root)

        while q:
            for i in range(len(q)):
                curr=q.popleft()
                rightside=curr.val

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            if rightside is not None:
                res.append(rightside)
        return res

# Time Complexity - O(n)
# Space Complexity - O(n)
        