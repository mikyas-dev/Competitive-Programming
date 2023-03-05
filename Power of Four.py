class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<1:
            return False
        if  n==1:
            return True
        return self.isPowerOfFour(n/4)
        # ans = log(n)//log(4)
        # return 4**ans==n
        
