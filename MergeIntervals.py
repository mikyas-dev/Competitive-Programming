class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        def fun(val):
            return val[0]
        intervals.sort(key=fun)
        sol=[]
        sol.append(intervals[0])
        for i in range(1,len(intervals)):
            if intervals[i][0]<=sol[-1][1]:
                sol[-1][1]=max(sol[-1][1],intervals[i][1])
            else:
                sol.append(intervals[i])
        return sol
