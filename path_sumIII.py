# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_sum = defaultdict(int)
        ans = 0
        prefix_sum[0] = 1

        def dfs(root,tot):
            nonlocal ans
            if not root:
                return
            tot += root.val
            if tot - targetSum in prefix_sum:
                ans += prefix_sum[tot -  targetSum]
            prefix_sum[tot] += 1
            dfs(root.left,tot)
            dfs(root.right,tot)
            prefix_sum[tot] -= 1
        
        dfs(root,0)
        return ans


        
