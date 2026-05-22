# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        def swap_subtrees(root):
            if not root:
                return
            
            # Swap subtrees
            left_tree = root.left
            root.left = root.right
            root.right = left_tree

            # Recurse
            swap_subtrees(root.left)
            swap_subtrees(root.right)
        
        swap_subtrees(root)

        return root