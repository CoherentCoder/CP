# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
      
        small = big = prev = None

        def inorder(r):
            nonlocal small, big, prev
            if not r:
                return
            
            inorder(r.left)
            if prev and prev.val > r.val:
                small = r
                if not big:
                    big = prev
            prev = r
            inorder(r.right)
        
        inorder(root)
        small.val, big.val = big.val, small.val
      
