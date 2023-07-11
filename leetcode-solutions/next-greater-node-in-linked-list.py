# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack=[]
        ans=[]
        a=0
        while head:
            while stack and head.val>stack[-1][1]:
                ans[stack[-1][0]]=head.val
                stack.pop()
            stack.append([a,head.val])
            ans.append(0)
            a+=1
            head=head.next
        return ans
                
        