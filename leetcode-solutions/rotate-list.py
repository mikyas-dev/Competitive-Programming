# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        fast = head
        count = 0

        while fast:
            fast = fast.next
            count+=1
        
        k %= count

        if count == 1 or k == 0:
            return head

        temp = None
        ans = head

        for _ in range(count-k-1):
            ans = ans.next
        
        temp = ans.next
        ans.next = None
        sol = temp

        while temp and temp.next:
            temp = temp.next
        
        if temp:
            temp.next = head

        return sol



        
