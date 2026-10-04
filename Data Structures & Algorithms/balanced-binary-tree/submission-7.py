# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def diameter(root):
            if not root:
                return 0
            return max(diameter(root.left),diameter(root.right)) + 1
        if not root:
            return True
        leftheight = diameter(root.left)
        rightheight = diameter(root.right)
        if abs(diameter(root.left) - diameter(root.right)) >1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)