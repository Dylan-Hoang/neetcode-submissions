# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        global diameter
        def height(root):
            if not root:
                return 0
            return 1 + max(height(root.left), height(root.right))
        if not root:
            return 0
        leftdepth = height(root.left)
        rightdepth = height(root.right)
        return max(leftdepth+rightdepth,self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right))
        