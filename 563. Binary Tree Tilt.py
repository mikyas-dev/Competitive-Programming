# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def tree(root):
            nonlocal ans
            
            if not root:
                return 0

            left = tree(root.left)
            right = tree(root.right)

            ans= ans + abs( left- right)

            return root.val + left + right

        tree(root)
        return ans
            
