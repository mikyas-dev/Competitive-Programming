# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans=temp=ListNode()
        valu=0
        while l1 or l2:          
            if l1 and l2:
                mod=(l1.val+l2.val+valu)%10
                temp.next=ListNode(mod)
                valu=(l1.val+l2.val+valu)//10
                l1,l2=l1.next,l2.next
            elif l1:
                mod=(l1.val+valu)%10
                temp.next=ListNode(mod)
                
                valu=(l1.val+valu)//10
                l1=l1.next
            else:
                mod=(l2.val+valu)%10
                temp.next=ListNode(mod)
                
                valu=(l2.val+valu)//10
                l2=l2.next
            temp=temp.next
        if valu!=0:
            temp.next=ListNode(valu)  
        return ans.next