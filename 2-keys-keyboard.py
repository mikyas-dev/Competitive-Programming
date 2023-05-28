class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        res = 0
        for i in range(2, n + 1):
            while n % i == 0:
                res += i
                n = n // i
            if n == 1:
                break
        return res