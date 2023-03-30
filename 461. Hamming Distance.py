class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = x^y
        return (count).bit_count()
