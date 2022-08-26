class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        start=0
        end=0
        maxim=deque()
        mini=deque()
        ans=0
        while end<len(nums):
            while maxim and nums[maxim[-1]]<=nums[end]:
                maxim.pop()
            while mini and nums[mini[-1]]>=nums[end]:
                mini.pop()
            maxim.append(end)
            mini.append(end)
            
            if nums[maxim[0]]-nums[mini[0]]>limit:
                start+=1
                if start>maxim[0] : maxim.popleft()
                if start>mini[0] : mini.popleft() 
            else:
                
                ans=max(ans,end-start+1)
                end+=1
        return ans
