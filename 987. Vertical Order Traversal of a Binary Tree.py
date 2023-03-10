# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.levels = defaultdict(list)

    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.helper(root,0,0)
        col = [val for key,val in sorted(self.levels.items())]

        ans = []

        for val in col:
            if len(val)==1:
                ans.append([val[0][1]])
            else:
                ans.append( [key for level,key in sorted(val, key = lambda x:(x[0],x[1]))])

        return ans       


    def helper(self, root, level, pos):
        if root == None:
            return 

        self.levels[pos].append((level,root.val))
        self.helper(root.left,level+1, pos-1)
        self.helper(root.right,level+1, pos+1)
