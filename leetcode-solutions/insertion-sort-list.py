# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        dummy.next = head
        node = head
        while node:
            if node.next and node.val > node.next.val:
                not_in = True
                out = node.next
                node.next = node.next.next
                insert = dummy
                while not_in:
                    if out.val <= insert.next.val:
                        out.next = insert.next
                        insert.next = out
                        not_in = False
                    else:
                        insert = insert.next
            else:
                node = node.next
        return dummy.next