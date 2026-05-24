# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def depth(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            
            return max(1 + depth(root.left), 1 + depth(root.right))
        
        return max(1 + depth(root.left), 1 + depth(root.right))
