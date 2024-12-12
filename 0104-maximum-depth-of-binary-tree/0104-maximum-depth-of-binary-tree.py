# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if not root: return 0

        # height=0

        # queue=deque()
        # queue.append(root)

        # while len(queue)>0:
        #     height+=1
        #     for i in range(len(queue)):
        #         curr=queue.popleft()

        #         if curr.left:
        #             queue.append(curr.left)
        #         if curr.right:
        #             queue.append(curr.right)
        # return height


        if not root: return 0

        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))

        # stack=[[root,1]]
        # res=0

        # while stack:
        #     node,depth=stack.pop()

        #     if node:
        #         stack.append([node.left,depth+1])
        #         stack.append([node.right,depth+1])
        #         res=max(res,depth)
        # return res

# Time Complexity - O(n)
# Space Complexity - O(n)
