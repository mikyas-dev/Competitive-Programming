class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        x = 2**(floor(log2(n))+1) -1
        return n//2 == n^x
