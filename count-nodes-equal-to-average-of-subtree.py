# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def helper(root):
            nonlocal res

            if not root:
                return 0,0


            totleft,countleft = helper(root.left)
            totright,countright = helper(root.right)

            val = root.val + totleft + totright
            count = 1 + countleft + countright

            if val//count == root.val:
    
                res += 1

            return val,count

        helper(root)
      
        return res