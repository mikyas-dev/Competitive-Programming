class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        ans=[]
        for i in nums1:
            for j in range(len(nums2)-1,-1,-1):
                if i>nums2[j]:continue
                if i==nums2[j]:break
                if stack:stack.pop()
                stack.append(nums2[j])
            if not stack:ans.append(-1)
            else:
                ans.append(stack[-1])
                stack.pop()
        return ans
