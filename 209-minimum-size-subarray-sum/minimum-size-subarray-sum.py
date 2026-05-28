class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums)<target:
            return 0
        l=s=0
        m=float("inf")
        for r in range(len(nums)):
            s+=nums[r]
            while s>=target:
                m=min(r-l+1,m)
                s-=nums[l]
                l+=1
        return m