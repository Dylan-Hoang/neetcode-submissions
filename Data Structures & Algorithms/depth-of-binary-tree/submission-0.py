# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def findheight(root):
            if not root:
                return 0
            return max(findheight(root.left),findheight(root.right)) +1
        return findheight(root)
        