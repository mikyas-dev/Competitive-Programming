# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.counter = defaultdict(int)

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.helper(root)
        maxVal = max(self.counter.values())
        return [key for key,value in self.counter.items() if value == maxVal]

    def helper(self,root):

        if root:
            self.counter[root.val] = 1 + self.counter.get(root.val,0)
            self.helper(root.left)
            self.helper(root.right)

        
