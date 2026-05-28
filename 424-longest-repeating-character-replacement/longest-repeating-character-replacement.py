class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d=defaultdict(int)
        l=m=0
        for r in range(len(s)):
            d[s[r]]+=1
            mf=max(d.values())
            cur=r-l+1
            if cur-mf>k:
                d[s[l]]-=1
                l+=1
            m=max(m,r-l+1)
        return m
