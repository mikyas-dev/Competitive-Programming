class Solution:
    def findComplement(self, num: int) -> int:
        x = floor(log(num)/log(2))+1
        return num ^ (2**x -1)
