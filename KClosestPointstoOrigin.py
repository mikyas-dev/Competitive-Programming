class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        point=[]
        def distance(val):
            return val[0]**2+val[1]**2
        points.sort(key=distance)
        for i in range(k):
            point.append(points[i])

        return point
        
