class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans=0
        i,j=0,len(height)-1
        while i<j:
            temp=(j-i)*min(height[i],height[j])
            ans=max(ans,temp)
            if height[i]<=height[j]:
                i+=1
            else:
                j-=1
        return ans