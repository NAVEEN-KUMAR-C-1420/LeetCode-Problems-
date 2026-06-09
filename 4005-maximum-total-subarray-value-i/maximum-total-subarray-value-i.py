class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        m=max(nums)
        n=min(nums)
        # for i in range(len(nums)-k):
        #     sub=nums[i:i+k]
        #     m+=max(sub)-min(sub)
        return k*(m-n)