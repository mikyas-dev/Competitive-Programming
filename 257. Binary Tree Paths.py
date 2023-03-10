# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []

        def traverse(root,temp):
            if not root:
                return 
            if not root.left and not root.right:
                ans.append(''.join(temp)+str(root.val))
            else:
                temp.append(str(root.val)+'->')
                traverse(root.left,temp)
                traverse(root.right,temp)
                temp.pop()
        traverse(root,[])
        return ans
