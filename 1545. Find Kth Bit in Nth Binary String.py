class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if k == 1:
            return '0'
        if (2**n)/2 == k:
            return '1'
        if k < 2**n/2:
            return self.findKthBit(n-1,k)
        return str (1-int(self.findKthBit(n-1,2**n-k)))
