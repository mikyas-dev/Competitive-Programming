class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums=[x for x in range(1,n+1)]
    
        def winner(start,leave):
            if len(nums)==1:
                return nums[-1]
            if start+leave<len(nums):
                nums.pop(start+leave)
                return winner(start+leave,leave)
            else:
                mul=math.floor((start+leave)/len(nums))
                b=start+leave-len(nums)*mul
                nums.pop(b)
                return winner(b,leave)
        return winner(0,k-1)
