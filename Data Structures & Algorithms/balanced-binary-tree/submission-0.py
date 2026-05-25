# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def height_with_balance(root: Optional[TreeNode]) -> (bool, int):
            if not root:
                return (True, 0)
            
            left = height_with_balance(root.left)
            right = height_with_balance(root.right)
            
            is_balanced = left[0] and right[0] and abs(left[1] - right[1]) < 2
            height = 1 + max(left[1], right[1])

            return (is_balanced, height)

        return height_with_balance(root)[0]