# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        ans = defaultdict(int)

        def helper(root):
            if not root:
                return 0

            left = helper(root.left)
            right = helper(root.right)

            tot = root.val + left + right

            ans[tot]+=1

            return tot
        helper (root)
        maxValue = max(ans.values())
        res = [key for key,val in ans.items() if val == maxValue]

        return res


