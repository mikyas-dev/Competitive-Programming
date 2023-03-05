# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 0
        high = n

        while low < n:
            mid = (low+n)//2

            if isBadVersion(mid):
                n = mid-1
            elif not isBadVersion(mid):
                low = mid+1

        return n
