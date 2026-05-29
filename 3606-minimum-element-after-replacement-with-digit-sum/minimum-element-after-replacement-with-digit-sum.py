class Solution:
    def minElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            x=str(nums[i])
            s=0
            for j in x:
                s+=int(j)
            nums[i]=s
        return min(nums)