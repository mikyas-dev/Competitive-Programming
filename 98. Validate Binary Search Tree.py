# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = None
        def inOrder(root):
            nonlocal prev
            left = right = True
            if root:
                left = inOrder(root.left)

                if prev != None and prev >= root.val:
                    return False
                prev = root.val
                right = inOrder(root.right)
                
            return left and right
        return inOrder(root)
