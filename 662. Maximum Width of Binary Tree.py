# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.levels = defaultdict(list)
   

    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.helper(root, 0, 0)
        print(self.levels)
        level = 0
        res = 0

        while level in self.levels:
            res = max(res, self.levels[level][-1] - self.levels[level][0])
            level += 1

        return res + 1

    def helper(self, root, level, pos):
        if root == None:
            return 

        self.levels[level].append(pos)
        self.helper(root.left, level+1, 2*pos)
        self.helper(root.right, level+1, 2*pos+1)
