class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        sort = sorted([(interval[0], idx) for idx, interval in enumerate(intervals)])
        res = [-1]*len(intervals)
        start = [i for i,j in sort]

        for i, val in enumerate(intervals):

            low = bisect_left(start,val[1])
            if low < len(sort):
                res[i] = sort[low][1]
        
        return res
