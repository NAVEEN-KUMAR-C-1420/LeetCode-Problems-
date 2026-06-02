class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        ans = float('inf')
        n = len(landStartTime)
        m = len(waterStartTime)
        for i in range(n):
            for j in range(m):
                l= landStartTime[i] + landDuration[i]
                f1 = max(l, waterStartTime[j]) + waterDuration[j]
                w = waterStartTime[j] + waterDuration[j]
                f2 = max(w, landStartTime[i]) + landDuration[i]
                ans = min(ans, f1, f2)
        return ans