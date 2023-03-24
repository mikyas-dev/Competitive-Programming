# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix = defaultdict(int)
        prefix[0] += 1
        ans = 0

        def treePreOrder(root,tot):
            nonlocal ans,prefix
            if root:
                if root.val + tot - targetSum in prefix:
                    
                    ans+=prefix[root.val+tot-targetSum]
                
                prefix[root.val+tot] += 1

                treePreOrder(root.left,root.val+tot)         
                
                treePreOrder(root.right,root.val+tot)

                prefix[root.val+tot] -= 1

        treePreOrder(root,0)

        return ans

                
