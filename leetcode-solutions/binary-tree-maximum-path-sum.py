# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float('-inf')
        
        def helper(root):
            nonlocal ans

            if not root:
                return 0
            
            left = helper(root.left)
            right = helper(root.right)

            tot = max(left,right)+root.val
            val = root.val + left + right

            if tot>val:val = tot

            if root.val > val:
        
                ans = max(root.val,ans)
                return root.val

            ans = max(val,ans)

            return max(left,right)+root.val

        helper(root)

        return ans

