# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = None
        def rev(prev,curr):
            nonlocal ans
            if not curr :
                ans = prev
                return 

            
            first = curr
            rev(first,first.next)
            first.next = prev
        rev(None,head)
        return ans