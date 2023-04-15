class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0:
            return True
        minima = int(sqrt(c))

        for i in range(1,minima+1):
            temp = c - i**2
            temp = int(sqrt(temp))
            if c == (temp**2 + i**2):
                return True
        
        return False