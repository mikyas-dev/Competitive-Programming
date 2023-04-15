# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = great = ListNode()
        dummy1 = less = ListNode()

        while head:
            if head.val < x:
                less.next = ListNode(head.val)
                less = less.next
            else:
                great.next = ListNode(head.val)
                great = great.next
            head =head.next
        less.next = dummy.next
        return dummy1.next