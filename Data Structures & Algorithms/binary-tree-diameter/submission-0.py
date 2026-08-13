# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        

        global maxDepth

        if not root:
            return 0
        def depth(root):
            if not root:
                return 0
            return 1 + max(depth(root.left),depth(root.right))
        leftdepth = depth(root.left)
        rightdepth = depth(root.right)
        maxDepth = max(leftdepth + rightdepth,self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right))
        return maxDepth

        