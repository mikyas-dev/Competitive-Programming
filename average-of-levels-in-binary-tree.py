# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue=deque([root])
        ans =[]
        while queue:
            qlen=len(queue)
            row =0
            for i in range(qlen):
                node = queue.popleft()
                row += node.val
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            ans.append(row/qlen)
        return ans