# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length=count=0
        node=head
        while head:
            length+=1
            head=head.next
        while node:
            if count==length//2:
                return node
            count+=1
            node=node.next