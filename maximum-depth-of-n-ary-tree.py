"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        ans = 0
        def dfs(root,count):
            nonlocal ans
            if root:
                if not root.children:
                    ans=max(ans,count)
                    return

                for child in root.children:
                    dfs(child,count+1)
        
        dfs(root,1)
        return ans