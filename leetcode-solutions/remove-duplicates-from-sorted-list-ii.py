# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dic=set()
        ans= head
        while ans and ans.next:
            if ans.val==ans.next.val:
                dic.add(ans.val)
                if ans.next.next:
                    ans.next=ans.next.next
                else:
                    ans.next=None
                continue
            ans=ans.next
        ans = dummy = ListNode(-101 , head)

        while dummy and  dummy.next:
            if dummy.next.val in dic:
                dummy.next = dummy.next.next
                continue
            
            dummy = dummy.next

        return ans.next