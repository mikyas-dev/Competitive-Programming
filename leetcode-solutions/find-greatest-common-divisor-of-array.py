class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        return self.gcd(nums[0], nums[-1])
    
    def gcd(self, a, b):
        if a == 0:
            return b
        return self.gcd(b % a, a)