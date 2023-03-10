# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if (root.val>p.val and root.val<q.val) or (root.val>q.val and root.val<p.val):
            return root
        if root.val == p.val or root.val == q.val:
            return root
        if p.val > root.val:
            root = self.lowestCommonAncestor(root.right,p,q)
        else:
            root = self.lowestCommonAncestor(root.left,p,q)
        return self.lowestCommonAncestor(root,p,q)
