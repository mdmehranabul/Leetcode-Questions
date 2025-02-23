# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        N=len(preorder)
        hashmap={}

        for i,n in enumerate(postorder):
            hashmap[n]=i
        #print(hashmap)

        def build(i1,i2,j1,j2):
            if i1>i2 or j1>j2: return None
            root=TreeNode(preorder[i1])
            if i1<i2:
                
                mid=hashmap[preorder[i1+1]]
                len_left=mid-j1+1

                root.left=build(i1+1,i1+len_left,j1,mid)
                root.right=build(i1+len_left+1,i2,mid+1,j2-1)
            return root
            
        return build(0,N-1,0,N-1)